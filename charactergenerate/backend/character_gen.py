"""
character_gen.py
Core logic for the Character Generation app.
Refactored from CharacterImageGeneration.py with:
  - progress callbacks for SSE streaming
  - get_scenario_summaries() — RAG-derived scenario dropdown
  - generate_prompt_for_scenario() — single call for one scene
"""

import os
import json
import urllib.request
import urllib.parse
from pathlib import Path

# Load prompts from JSON
PROMPTS_FILE = Path(__file__).parent / "prompts.json"
def load_prompts():
    if PROMPTS_FILE.exists():
        with open(PROMPTS_FILE, "r") as f:
            return json.load(f)
    return {}

PROMPTS = load_prompts()

from dotenv import load_dotenv

try:
    from ollama import Client as OllamaClient
except ImportError:
    OllamaClient = None

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

try:
    from anthropic import Anthropic
except ImportError:
    Anthropic = None

try:
    from google import genai
except ImportError:
    genai = None

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

try:
    import ebooklib
    from ebooklib import epub
    from bs4 import BeautifulSoup
except ImportError:
    ebooklib = None
    epub = None
    BeautifulSoup = None

# Load .env from the repo root (two directories above this file: backend/ -> CharacterGenerate/ -> repo root)
_REPO_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(_REPO_ROOT / ".env")

# ---------------------------------------------------------------------------
# Configuration — all values come from .env with fallback defaults
# ---------------------------------------------------------------------------
OLLAMA_MODEL              = os.getenv("OLLAMA_MODEL",              "Gemma4E4B:latest")
OLLAMA_HOST               = os.getenv("OLLAMA_HOST",               "http://localhost:11434")
EMBEDDING_MODEL           = os.getenv("EMBEDDING_MODEL",           "all-MiniLM-L6-v2")
CHUNK_SIZE                = int(os.getenv("CHUNK_SIZE",            "1000"))
CHUNK_OVERLAP             = int(os.getenv("CHUNK_OVERLAP",         "200"))
RAG_TOP_K                 = int(os.getenv("RAG_TOP_K",             "6"))
CHROMA_PERSIST_DIR_PREFIX = os.getenv("CHROMA_PERSIST_DIR_PREFIX", "chroma_db")

LLM_PROVIDER              = os.getenv("LLM_PROVIDER",              "ollama").lower()
OPENAI_MODEL              = os.getenv("OPENAI_MODEL",              "gpt-4o")
ANTHROPIC_MODEL           = os.getenv("ANTHROPIC_MODEL",           "claude-3-5-sonnet-20241022")
GEMINI_MODEL              = os.getenv("GEMINI_MODEL",              "gemini-2.5-flash-lite")


def generate_text(prompt: str, provider: str = None, model: str = None) -> str:
    """Generate text using the configured LLM provider."""
    provider = (provider or LLM_PROVIDER).lower()
    
    if provider == "openai":
        if OpenAI is None:
            raise RuntimeError("openai package is not installed. Run: pip install openai")
        
        kwargs = {"api_key": os.getenv("OPENAI_API_KEY")}
        if os.getenv("OPENAI_BASE_URL"):
            kwargs["base_url"] = os.getenv("OPENAI_BASE_URL")
            
        client = OpenAI(**kwargs)
        response = client.chat.completions.create(
            model=(model or OPENAI_MODEL),
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    elif provider == "anthropic":
        if Anthropic is None:
            raise RuntimeError("anthropic package is not installed. Run: pip install anthropic")
            
        kwargs = {"api_key": os.getenv("ANTHROPIC_API_KEY")}
        if os.getenv("ANTHROPIC_BASE_URL"):
            kwargs["base_url"] = os.getenv("ANTHROPIC_BASE_URL")
            
        client = Anthropic(**kwargs)
        response = client.messages.create(
            model=(model or ANTHROPIC_MODEL),
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.content[0].text.strip()
    elif provider == "gemini":
        if genai is None:
            raise RuntimeError("google-genai package is not installed. Run: pip install google-genai")
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY or GOOGLE_API_KEY environment variable is missing")
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=(model or GEMINI_MODEL),
            contents=prompt
        )
        return response.text.strip()
    elif provider == "ollama":
        if OllamaClient is None:
            raise RuntimeError("ollama package is not installed. Run: pip install ollama")
        client = OllamaClient(host=OLLAMA_HOST)
        response = client.generate(model=(model or OLLAMA_MODEL), prompt=prompt)
        return response["response"].strip()
    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: {provider}")


# ---------------------------------------------------------------------------
# 1. Wikipedia — major character names
# ---------------------------------------------------------------------------

def get_major_character_names(book_title: str, llm_provider: str = None, llm_model: str = None) -> list[str]:
    """Query Wikipedia for the book and extract major character names via LLM."""
    try:
        search_query = urllib.parse.quote(book_title)
        search_url = (
            f"https://en.wikipedia.org/w/api.php?action=query&list=search"
            f"&srsearch={search_query}&utf8=&format=json"
        )
        req = urllib.request.Request(search_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as response:
            search_data = json.loads(response.read().decode("utf-8"))

        if not search_data["query"]["search"]:
            return []

        page_title = search_data["query"]["search"][0]["title"]
        content_query = urllib.parse.quote(page_title)
        content_url = (
            f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts"
            f"&explaintext=1&titles={content_query}&format=json"
        )
        req2 = urllib.request.Request(content_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req2) as response:
            content_data = json.loads(response.read().decode("utf-8"))

        pages = content_data["query"]["pages"]
        page_id = list(pages.keys())[0]
        content = pages[page_id].get("extract", "")
        if not content:
            return []

        prompt = PROMPTS.get("wikipedia_extract_characters", "").format(
            book_title=book_title,
            content=content[:15000]
        )
        text_response = generate_text(prompt, provider=llm_provider, model=llm_model)
        major_characters = [n.strip() for n in text_response.split(",") if n.strip()]
        return major_characters

    except Exception as e:
        print(f"[Wikipedia] Error: {e}")
        return []


# ---------------------------------------------------------------------------
# 2. Vector index
# ---------------------------------------------------------------------------

import sqlite3 as _sqlite3
import shutil as _shutil


def _chroma_db_is_healthy(persist_directory: str) -> bool:
    """
    Pre-validate the chroma.sqlite3 file using Python's own sqlite3 module
    BEFORE ChromaDB's Rust layer opens it.

    ChromaDB's Rust/pyo3 SQLite binding raises a thread-killing panic (not a
    catchable Python exception) when the schema version doesn't match — e.g.
    after a ChromaDB upgrade.  We catch that here by querying the expected
    tables ourselves first.
    """
    db_path = os.path.join(persist_directory, "chroma.sqlite3")
    if not os.path.exists(db_path):
        return False
    try:
        con = _sqlite3.connect(db_path, timeout=5)
        cur = con.cursor()
        # These tables must exist in any healthy ChromaDB ≥ 0.4 store
        for table in ("collections", "embeddings", "embedding_metadata"):
            cur.execute(f"SELECT 1 FROM {table} LIMIT 1")
        con.close()
        return True
    except Exception as e:
        print(f"[Chroma] Pre-validation failed for '{db_path}': {e}")
        return False


def extract_text_from_epub(epub_path: str) -> str:
    """Extract and clean plain text from an EPUB file."""
    if epub is None or BeautifulSoup is None:
        raise ImportError("ebooklib and beautifulsoup4 are required for EPUB support. Run: pip install ebooklib beautifulsoup4")
    
    book = epub.read_epub(epub_path)
    text_parts = []
    
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # item.get_content() returns bytes (HTML), BeautifulSoup cleans it
            soup = BeautifulSoup(item.get_content(), "html.parser")
            # Get text and remove unnecessary whitespace
            text = soup.get_text(separator=" ", strip=True)
            if text:
                text_parts.append(text)
    
    return "\n\n".join(text_parts)


def build_book_index(txt_filepath: str, progress_cb=None, persist_directory: str = None):
    """
    Build (or load) a Chroma vector index for the book.
    progress_cb(stage, n, total, message) is called at each step.

    If the existing index fails pre-validation (e.g. ChromaDB version mismatch
    that would cause a Rust/SQLite panic), the stale directory is automatically
    deleted and the index is rebuilt from scratch.
    """
    if persist_directory is None:
        book_name = os.path.splitext(os.path.basename(txt_filepath))[0]
        persist_directory = os.path.join(
            os.path.dirname(os.path.abspath(txt_filepath)),
            f"{CHROMA_PERSIST_DIR_PREFIX}_{book_name}",
        )

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    if os.path.exists(persist_directory) and any(os.scandir(persist_directory)):
        if _chroma_db_is_healthy(persist_directory):
            if progress_cb:
                progress_cb("loading_existing", 1, 1, "Loading existing vector index…")
            return Chroma(persist_directory=persist_directory, embedding_function=embeddings)
        else:
            print(
                f"[Chroma] Stale or incompatible DB at '{persist_directory}' — "
                "deleting and rebuilding from scratch."
            )
            _shutil.rmtree(persist_directory, ignore_errors=True)
            if progress_cb:
                progress_cb(
                    "rebuilding",
                    0,
                    1,
                    "Vector index was outdated — rebuilding from scratch…",
                )

    if progress_cb:
        progress_cb("loading_text", 0, 1, "Loading book text…")

    # Support for .txt and .epub
    ext = os.path.splitext(txt_filepath)[1].lower()
    if ext == ".epub":
        content = extract_text_from_epub(txt_filepath)
        docs = [Document(page_content=content, metadata={"source": txt_filepath})]
    else:
        loader = TextLoader(txt_filepath, encoding="utf-8")
        docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    splits = text_splitter.split_documents(docs)
    total = len(splits)

    vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

    batch_size = 50
    for i in range(0, total, batch_size):
        batch = splits[i : i + batch_size]
        vectorstore.add_documents(batch)
        done = min(i + batch_size, total)
        if progress_cb:
            progress_cb("embedding", done, total, f"Embedding chunks {done} / {total}…")

    return vectorstore


# ---------------------------------------------------------------------------
# 3. RAG retrieval
# ---------------------------------------------------------------------------

def get_character_situations(vectorstore, character_name: str, k: int = 6) -> list[str]:
    """Retrieve the top-k chunks most relevant to scenes featuring `character_name`."""
    query = PROMPTS.get("character_situation_query", "").format(
        character_name=character_name
    )
    relevant_docs = vectorstore.similarity_search(query, k=k)
    return [doc.page_content for doc in relevant_docs]


def get_group_situations(vectorstore, character_names: list[str], k: int = 6) -> list[str]:
    """Retrieve chunks where multiple characters appear together."""
    names_str = " and ".join(character_names)
    query = PROMPTS.get("group_situation_query", "").format(
        names_str=names_str
    )
    
    # Fetch more and filter
    relevant_docs = vectorstore.similarity_search(query, k=k*3)
    
    import re
    valid_scenes = []
    for doc in relevant_docs:
        content = doc.page_content
        all_found = True
        for name in character_names:
            # Check if name (or any significant word in it) exists in the chunk
            words = [w for w in name.split() if len(w) > 2]
            if not words: words = [name]
            
            char_found = False
            for word in words:
                if re.search(rf"\b{re.escape(word)}\b", content, re.IGNORECASE):
                    char_found = True
                    break
            
            if not char_found:
                all_found = False
                break
        
        if all_found:
            valid_scenes.append(content)
            if len(valid_scenes) >= k:
                break
                
    return valid_scenes


def get_scenario_summaries(vectorstore, character_name: str, llm_provider: str = None, llm_model: str = None) -> list[dict]:
    """
    Retrieve k=6 RAG scenes for the character and ask the LLM to distill each
    into a short one-sentence label.
    Returns: [{"label": str, "context": str}, ...]
    """
    situations = get_character_situations(vectorstore, character_name, k=RAG_TOP_K)
    summaries = []
    for ctx in situations:
        prompt = PROMPTS.get("scenario_summary", "").format(
            character_name=character_name,
            ctx=ctx[:2000]
        )
        resp_text = generate_text(prompt, provider=llm_provider, model=llm_model)
        label = resp_text.strip('"').strip("'")
        summaries.append({"label": label, "context": ctx})
    return summaries


# ---------------------------------------------------------------------------
# 4. Character analysis
# ---------------------------------------------------------------------------

def analyze_character(book_text: str, character_name: str, llm_provider: str = None, llm_model: str = None) -> str:
    """Extract a structured character description from a book excerpt."""
    prompt = PROMPTS.get("character_analysis", "").format(
        character_name=character_name,
        book_text=book_text[:15000]
    )
    return generate_text(prompt, provider=llm_provider, model=llm_model)


# ---------------------------------------------------------------------------
# 5. Actor casting
# ---------------------------------------------------------------------------

def cast_character_with_actor(
    character_name: str, 
    character_description: str, 
    industry: str = "hollywood",
    genre: str = "",
    decade: str = "2026",
    llm_provider: str = None, 
    llm_model: str = None
) -> str:
    """Suggest a real-world actor from the given industry and decade to portray the character in a specific genre."""
    genre_context = f"This is for a {genre} adaptation." if genre else ""
    decade_context = f"The production is set in/filmed during the {decade}s." if decade and decade != "2026" else "The production is modern (2026)."

    prompt = PROMPTS.get("actor_casting", "").format(
        character_name=character_name,
        character_description=character_description,
        genre_context=genre_context,
        decade_context=decade_context,
        industry=industry
    )
    return generate_text(prompt, provider=llm_provider, model=llm_model)


# ---------------------------------------------------------------------------
# 6. Prompt generation
# ---------------------------------------------------------------------------

def generate_prompt_for_scenario(
    character_name: str,
    description: str,
    scenario_context: str,
    actor_name: str = "",
    genre: str = "",
    decade: str = "2026",
    gender: str = "",
    race: str = "",
    age: str = "",
    prompt_type: str = "image",
    llm_provider: str = None, 
    llm_model: str = None
) -> str:
    """
    Build a Z-Image-Turbo / Stable Diffusion / LTX Video prompt for one character scene.
    Uses the (possibly user-edited) description and actor name.
    """

    # Create override block
    overrides = []
    if gender: overrides.append(f"Gender: {gender}")
    if race: overrides.append(f"Race/Ethnicity: {race}")
    if age: overrides.append(f"Age: {age}")
    override_text = "\n".join(overrides)

    # Extract scene-specific details with genre adaptation for visuals
    genre_context = f" (Adapted specifically for the {genre} genre)" if genre else ""
    extract_prompt = PROMPTS.get("scene_detail_extraction", "").format(
        genre_context=genre_context,
        character_name=character_name,
        genre=genre if genre else "realistic",
        scenario_context=scenario_context
    )
    scene_details = generate_text(extract_prompt, provider=llm_provider, model=llm_model)

    actor_instruction = (
        f"The character's face should closely resemble the actor: {actor_name}."
        if actor_name
        else ""
    )

    genre_instruction = f"Genre: {genre}" if genre else ""
    decade_instruction = f"Visual Style: {decade}s cinematography and fashion" if decade and decade != "2026" else "Visual Style: Modern cinematic hyper-realistic"

    template_key = "final_video_prompt" if prompt_type == "video" else "final_image_prompt"
    prompt_template = PROMPTS.get(template_key, "").format(
        character_name=character_name,
        genre_instruction=genre_instruction,
        decade_instruction=decade_instruction,
        actor_instruction=actor_instruction,
        override_text=override_text if override_text else "None",
        description=description,
        genre=genre,
        scene_details=scene_details
    )

    return generate_text(prompt_template, provider=llm_provider, model=llm_model)


def generate_group_media_prompts(
    combined_descriptions: str,
    scenario_context: str,
    genre: str = "",
    llm_provider: str = None, 
    llm_model: str = None
) -> dict:
    """
    Generate both an image prompt and a video prompt for a multi-character scene.
    """
    image_template = PROMPTS.get("group_image_prompt", "").format(
        combined_descriptions=combined_descriptions,
        scenario_context=scenario_context,
        genre=genre if genre else "realistic"
    )
    
    video_template = PROMPTS.get("group_video_prompt", "").format(
        combined_descriptions=combined_descriptions,
        scenario_context=scenario_context,
        genre=genre if genre else "realistic"
    )
    
    image_prompt = generate_text(image_template, provider=llm_provider, model=llm_model)
    video_prompt = generate_text(video_template, provider=llm_provider, model=llm_model)
    
    return {"image_prompt": image_prompt, "video_prompt": video_prompt}


# ---------------------------------------------------------------------------
# 7. Location extraction & analysis
# ---------------------------------------------------------------------------

def extract_prominent_locations(vectorstore, llm_provider: str = None, llm_model: str = None) -> list[str]:
    """
    Sample a broad set of RAG chunks and ask the LLM to identify prominent
    named locations / buildings / places in the book.
    """
    # Broad query to pull location-heavy passages
    query = "prominent locations buildings places settings landmarks described in the book"
    docs = vectorstore.similarity_search(query, k=12)
    combined = "\n\n---\n\n".join(d.page_content for d in docs)

    prompt = PROMPTS.get("extract_locations", "").format(content=combined[:18000])
    result = generate_text(prompt, provider=llm_provider, model=llm_model)
    locations = [loc.strip() for loc in result.split(",") if loc.strip()]
    return locations


def analyze_location(vectorstore, location_name: str, llm_provider: str = None, llm_model: str = None) -> str:
    """
    Retrieve RAG chunks most relevant to the location and produce a vivid
    visual description covering architecture, atmosphere, and time-of-day.
    """
    query = PROMPTS.get("location_situation_query", "").format(location_name=location_name)
    docs = vectorstore.similarity_search(query, k=6)
    book_excerpts = "\n\n---\n\n".join(d.page_content for d in docs)

    prompt = PROMPTS.get("location_analysis", "").format(
        location_name=location_name,
        book_excerpts=book_excerpts[:12000]
    )
    return generate_text(prompt, provider=llm_provider, model=llm_model)


def generate_landscape_prompt(
    location_name: str,
    description: str,
    genre: str = "",
    decade: str = "2026",
    time_of_day: str = "",
    weather: str = "",
    llm_provider: str = None,
    llm_model: str = None
) -> str:
    """
    Build a Z-Image Turbo landscape / architectural prompt for a book location.
    """
    genre_context = f"Genre / Style: {genre}" if genre else "Genre / Style: Cinematic Realism"
    decade_context = (
        f"Visual Style: {decade}s cinematography and architecture"
        if decade and decade != "2026"
        else "Visual Style: Modern cinematic hyper-realistic"
    )
    tod_context = f"Time of Day: {time_of_day}" if time_of_day else ""
    weather_context = f"Weather & Atmosphere: {weather}" if weather else ""

    prompt = PROMPTS.get("landscape_image_prompt", "").format(
        location_name=location_name,
        description=description,
        genre_context=genre_context,
        decade_context=decade_context,
        tod_context=tod_context,
        weather_context=weather_context,
    )
    return generate_text(prompt, provider=llm_provider, model=llm_model)

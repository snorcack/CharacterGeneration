"""
main.py — FastAPI backend for the Character Generation app.

Endpoints:
  POST /api/load-book                 start background indexing job
  GET  /api/status                    SSE stream of job progress
  GET  /api/characters                return cached character list
  POST /api/character-details         analyze character + get RAG scenarios
  POST /api/cast-actor                cast an actor for the character
  POST /api/generate-prompt           build the final Z-Image-Turbo prompt
  POST /api/comfyui/test              verify ComfyUI is reachable
  POST /api/comfyui/generate          queue + stream SSE progress for image gen
  GET  /api/comfyui/image/{prompt_id} proxy-fetch the finished image
"""
import os
import asyncio
import threading
import json
import uuid
from pathlib import Path
from typing import Any, Optional
import urllib.request
import urllib.parse
import urllib.error
import re

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, Response
from pydantic import BaseModel

# Load .env from the repo root (two directories above this file)
_REPO_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(_REPO_ROOT / ".env")

# ---------------------------------------------------------------------------
# Configuration — all values come from .env with fallback defaults
# ---------------------------------------------------------------------------
BACKEND_HOST        = os.getenv("BACKEND_HOST",         "0.0.0.0")
BACKEND_PORT        = int(os.getenv("BACKEND_PORT",     "8000"))
BACKEND_RELOAD      = os.getenv("BACKEND_RELOAD",       "true").lower() == "true"
COMFYUI_POLL_LIMIT  = int(os.getenv("COMFYUI_POLL_LIMIT",    "100"))
COMFYUI_POLL_INTERVAL = float(os.getenv("COMFYUI_POLL_INTERVAL", "2"))

from character_gen import (
    generate_text,
    get_major_character_names,
    build_book_index,
    get_scenario_summaries,
    analyze_character,
    get_character_situations,
    get_group_situations,
    cast_character_with_actor,
    generate_prompt_for_scenario,
    extract_prominent_locations,
    analyze_location,
    generate_landscape_prompt,
    PROMPTS,
)
from comfyui import (
    inject_prompt_into_workflow,
    queue_prompt,
    poll_until_done,
    get_output_image_bytes,
    test_connection,
)

# ---------------------------------------------------------------------------
# Persistence setup
# ---------------------------------------------------------------------------
LIBRARY_FILE = "library.json"
OUTPUT_DIR = Path("output_images")
OUTPUT_DIR.mkdir(exist_ok=True)

def load_library():
    if os.path.exists(LIBRARY_FILE):
        try:
            with open(LIBRARY_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_library(library):
    with open(LIBRARY_FILE, "w") as f:
        json.dump(library, f, indent=4)

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------

app = FastAPI(title="Character Generation API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Shared in-memory state (single-user dev app — no auth needed)
# ---------------------------------------------------------------------------

state: dict[str, Any] = {
    "job_status": "idle",   # idle | running | done | error
    "stage": "",
    "progress": 0,
    "total": 0,
    "message": "",
    "characters": [],
    "vectorstore": None,
    "book_title": "",
    "error": None,
    "agent_status": "idle",
    "agent_message": "",
    "agent_progress": 0,
    "agent_total": 0,
    "agent_abort": False,
}


# ---------------------------------------------------------------------------
# Background indexing thread
# ---------------------------------------------------------------------------

def load_book_task(book_path: str, book_name: str, llm_provider: str = None, llm_model: str = None) -> None:
    """Runs in a daemon thread; writes progress into `state`."""
    try:
        state["job_status"] = "running"
        state["characters"] = []
        state["vectorstore"] = None
        state["book_title"] = book_name
        state["error"] = None

        library = load_library()
        book_info = library.get(book_name, {})

        # Step 1 — Wikipedia characters
        state["stage"] = "wikipedia"
        state["progress"] = 0
        state["total"] = 1
        
        if "characters" in book_info and book_info["characters"]:
            state["message"] = f"Loading cached characters for '{book_name}'…"
            characters = book_info["characters"]
        else:
            state["message"] = f"Fetching major characters from Wikipedia for '{book_name}'…"
            characters = get_major_character_names(book_name, llm_provider, llm_model)
            
        state["characters"] = characters
        state["progress"] = 1
        state["message"] = f"Found {len(characters)} characters. Building vector index…"

        # Step 2 — Vector index with live progress
        def prog_cb(stage: str, n: int, total: int, msg: str) -> None:
            state["stage"] = stage
            state["progress"] = n
            state["total"] = total
            state["message"] = msg

        vectorstore = build_book_index(book_path, progress_cb=prog_cb)
        state["vectorstore"] = vectorstore
        
        # Save to library (preserve existing descriptions)
        existing = library.get(book_name, {})
        library[book_name] = {
            "book_path": book_path,
            "characters": characters,
            "descriptions": existing.get("descriptions", {}),
        }
        save_library(library)
        
        state["job_status"] = "done"
        state["message"] = (
            f"Ready! Indexed the book and found {len(characters)} characters."
        )

    except Exception as exc:
        import traceback
        traceback.print_exc()
        state["job_status"] = "error"
        state["error"] = str(exc)
        state["message"] = f"Error: {exc}"


# ---------------------------------------------------------------------------
# Request / response models
# ---------------------------------------------------------------------------

class LoadBookRequest(BaseModel):
    book_path: str
    book_name: str
    llm_provider: Optional[str] = None
    llm_model: Optional[str] = None


class CharacterDetailsRequest(BaseModel):
    character_name: str
    llm_provider: Optional[str] = None
    llm_model: Optional[str] = None
    force_regenerate: Optional[bool] = False


class DeleteCharacterDataRequest(BaseModel):
    book_name: str
    character_name: str
    delete_prompts_only: bool = False


class CastActorRequest(BaseModel):
    character_name: str
    description: str
    industry: str = "hollywood"
    genre: str = ""
    decade: str = "2026"
    llm_provider: Optional[str] = None
    llm_model: Optional[str] = None


class GeneratePromptRequest(BaseModel):
    character_name: str
    description: str
    scenario_context: str
    actor_name: str = ""
    genre: str = ""
    decade: str = "2026"
    gender: str = ""
    race: str = ""
    age: str = ""
    prompt_type: str = "image"
    llm_provider: Optional[str] = None
    llm_model: Optional[str] = None


class ComfyUITestRequest(BaseModel):
    comfy_url: str


class ComfyUIGenerateRequest(BaseModel):
    comfy_url: str
    workflow_json: str          # raw JSON string (API-format)
    prompt_text: str
    node_id: Optional[str] = None


class GeminiImageRequest(BaseModel):
    prompt_text: str
    model: Optional[str] = None


class SavePromptRequest(BaseModel):
    book_name: str
    character_name: str
    prompt: str


class GroupScenesRequest(BaseModel):
    character_names: list[str]
    llm_provider: Optional[str] = None
    llm_model: Optional[str] = None


class GenerateGroupPromptRequest(BaseModel):
    character_names: list[str]
    scenario_context: str
    genre: str = ""
    llm_provider: Optional[str] = None
    llm_model: Optional[str] = None


class BatchAnalyzeRequest(BaseModel):
    character_names: list[str]
    use_casting: bool = False
    genre: Optional[str] = ""
    decade: Optional[str] = "2026"
    industry: Optional[str] = "hollywood"
    llm_provider: Optional[str] = None
    llm_model: Optional[str] = None


class BatchImageRequest(BaseModel):
    character_names: list[str]
    images_per_character: int = 1
    generator_type: str = "comfyui" # comfyui | gemini
    comfy_url: Optional[str] = None
    workflow_json: Optional[str] = None
    node_id: Optional[str] = None
    gemini_model: Optional[str] = None


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/api/books")
async def get_books():
    return load_library()


@app.post("/api/load-book")
async def load_book(req: LoadBookRequest):
    if state["job_status"] == "running":
        raise HTTPException(status_code=409, detail="A book is already being loaded.")

    if not os.path.exists(req.book_path):
        # Fallback: try relative to two levels up (project root often has data/ folder)
        alt_path = os.path.join("..", "..", req.book_path)
        if os.path.exists(alt_path):
            req.book_path = alt_path
        else:
            raise HTTPException(
                status_code=400, 
                detail=f"Book file not found. Checked: {req.book_path} and {alt_path}"
            )

    t = threading.Thread(
        target=load_book_task,
        args=(req.book_path, req.book_name, req.llm_provider, req.llm_model),
        daemon=True,
    )
    t.start()
    return {"status": "started"}


@app.get("/api/status")
async def get_status():
    """SSE stream — the client polls this after starting a load-book job."""
    async def event_generator():
        last_snapshot: dict = {}
        while True:
            snapshot = {
                "status": state["job_status"],
                "stage": state["stage"],
                "progress": state["progress"],
                "total": state["total"],
                "message": state["message"],
                "characters": state["characters"],
            }
            if snapshot != last_snapshot:
                yield f"data: {json.dumps(snapshot)}\n\n"
                last_snapshot = dict(snapshot)

            if state["job_status"] in ("done", "error"):
                break

            await asyncio.sleep(0.5)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


@app.get("/api/characters")
async def get_characters():
    return {
        "characters": state["characters"],
        "status": state["job_status"],
    }


@app.get("/api/agent-status")
async def get_agent_status():
    """SSE stream for the batch analysis agent."""
    async def event_generator():
        last_snapshot: dict = {}
        while True:
            snapshot = {
                "status": state["agent_status"],
                "message": state["agent_message"],
                "progress": state["agent_progress"],
                "total": state["agent_total"],
            }
            if snapshot != last_snapshot:
                yield f"data: {json.dumps(snapshot)}\n\n"
                last_snapshot = dict(snapshot)

            if state["agent_status"] in ("done", "error"):
                break

            await asyncio.sleep(0.5)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


@app.get("/api/character-descriptions/{book_name:path}")
async def get_character_descriptions(book_name: str):
    """Return all cached character descriptions (and image prompt_ids) for a book."""
    library = load_library()
    book_info = library.get(book_name, {})
    return {
        "descriptions": book_info.get("descriptions", {})
    }


@app.post("/api/character-details")
async def character_details(req: CharacterDetailsRequest):
    if state["vectorstore"] is None:
        raise HTTPException(
            status_code=400,
            detail="No book loaded. Call /api/load-book first.",
        )

    try:
        book_name = state["book_title"]
        library = load_library()
        book_info = library.get(book_name, {})
        cached_descriptions = book_info.get("descriptions", {})

        # --- Return cached description + scenarios if available ---
        if not req.force_regenerate and req.character_name in cached_descriptions:
            cached = cached_descriptions[req.character_name]
            return {
                "description": cached["description"],
                "scenarios": cached["scenarios"],
                "prompts": cached.get("prompts", []),
                "cached": True,
            }

        # --- Otherwise generate from LLM ---
        # Retrieve scenes for baseline description
        situations = get_character_situations(
            state["vectorstore"], req.character_name, k=10
        )
        
        # Verify if the character is actually in the retrieved chunks
        words = [w for w in req.character_name.split() if len(w) > 2]
        if not words:
            words = [req.character_name] # fallback for short names
            
        found = False
        for text in situations:
            for word in words:
                if re.search(rf"\b{re.escape(word)}\b", text, re.IGNORECASE):
                    found = True
                    break
            if found:
                break
                
        if not situations or not found:
            raise ValueError(f"Character '{req.character_name}' was not found in the book.")

        full_context = "\n\n---\n\n".join(situations)
        description = analyze_character(full_context, req.character_name, req.llm_provider, req.llm_model)

        # Get RAG-derived scenario list (6 scenes, each summarised)
        scenarios = get_scenario_summaries(state["vectorstore"], req.character_name, req.llm_provider, req.llm_model)

        # --- Persist to library ---
        cached_descriptions[req.character_name] = {
            "description": description,
            "scenarios": scenarios,
            "image_prompt_ids": [],
            "prompts": []
        }
        if book_name not in library:
            library[book_name] = {"characters": [], "descriptions": {}}
        library[book_name]["descriptions"] = cached_descriptions
        save_library(library)

        return {"description": description, "scenarios": scenarios, "prompts": [], "cached": False}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"LLM analytics failed: {exc}")


@app.post("/api/delete-character-data")
async def delete_character_data(req: DeleteCharacterDataRequest):
    """Delete a character's description/prompts/images or clear just prompts/images."""
    library = load_library()
    book_info = library.get(req.book_name)
    if not book_info:
        raise HTTPException(status_code=404, detail="Book not found")
        
    descriptions = book_info.get("descriptions", {})
    if req.character_name not in descriptions:
        raise HTTPException(status_code=404, detail="Character not found")
        
    if req.delete_prompts_only:
        descriptions[req.character_name]["prompts"] = []
        descriptions[req.character_name]["image_prompt_ids"] = []
    else:
        del descriptions[req.character_name]
        
    save_library(library)
    return {"status": "success"}


@app.post("/api/character-descriptions/set-image")
async def set_character_image(body: dict):
    """Store the prompt_id of a generated image against a character in the library."""
    book_name = body.get("book_name") or state["book_title"]
    character_name = body.get("character_name")
    prompt_id = body.get("prompt_id")
    if not character_name or not prompt_id:
        raise HTTPException(status_code=400, detail="character_name and prompt_id are required")
    library = load_library()
    book_info = library.setdefault(book_name, {"characters": [], "descriptions": {}})
    desc_entry = book_info.setdefault("descriptions", {}).setdefault(character_name, {
        "description": "", "scenarios": [], "image_prompt_ids": []
    })
    
    # Initialize list if it was old singular format or missing
    if "image_prompt_ids" not in desc_entry:
        desc_entry["image_prompt_ids"] = []
        if desc_entry.get("image_prompt_id"):
            desc_entry["image_prompt_ids"].append(desc_entry["image_prompt_id"])
            del desc_entry["image_prompt_id"]

    if prompt_id not in desc_entry["image_prompt_ids"]:
        desc_entry["image_prompt_ids"].append(prompt_id)
    save_library(library)
    return {"ok": True}


@app.post("/api/save-prompt")
async def save_prompt(req: SavePromptRequest):
    """Save an edited or generated prompt to the character's list in the library."""
    library = load_library()
    book_info = library.get(req.book_name)
    if not book_info:
        raise HTTPException(status_code=404, detail="Book not found")
    
    desc_entry = book_info.get("descriptions", {}).get(req.character_name)
    if not desc_entry:
        raise HTTPException(status_code=404, detail="Character description not found. Analyze character first.")
    
    if "prompts" not in desc_entry:
        desc_entry["prompts"] = []
    
    if req.prompt not in desc_entry["prompts"]:
        desc_entry["prompts"].append(req.prompt)
    
    save_library(library)
    return {"status": "success", "prompts": desc_entry["prompts"]}


@app.post("/api/find-group-scenes")
async def find_group_scenes(req: GroupScenesRequest):
    """Retrieve scenes where multiple characters appear together and summarize them."""
    if state["vectorstore"] is None:
        raise HTTPException(status_code=400, detail="No book loaded. Call /api/load-book first.")
        
    scenes = get_group_situations(state["vectorstore"], req.character_names, k=5)
    
    if not scenes:
        return {
            "scenes": [], 
            "message": f"No scenes found containing all characters: {', '.join(req.character_names)}"
        }
        
    # Summarize each scene using LLM for the dropdown/list
    summaries = []
    for ctx in scenes:
        prompt = PROMPTS.get("group_scene_summary", "").format(
            character_names=", ".join(req.character_names),
            ctx=ctx[:2000]
        )
        label = generate_text(prompt, provider=req.llm_provider, model=req.llm_model)
        summaries.append({
            "label": label.strip('"').strip("'").strip(),
            "context": ctx
        })
        
    return {"scenes": summaries}


def batch_analyze_task(
    character_names: list[str], 
    use_casting: bool = False,
    genre: str = "",
    decade: str = "2026",
    industry: str = "hollywood",
    llm_provider: str = None, 
    llm_model: str = None
):
    """Background task to analyze multiple characters with casting and prompts."""
    try:
        state["agent_status"] = "running"
        state["agent_total"] = len(character_names)
        state["agent_progress"] = 0
        
        book_name = state["book_title"]
        if not book_name:
            raise ValueError("No book title in state. Load a book first.")
            
        library = load_library()
        book_info = library.get(book_name, {})
        cached_descriptions = book_info.get("descriptions", {})
        
        for i, char_name in enumerate(character_names):
            if state.get("agent_abort"):
                state["agent_message"] = f"Aborted. Finished {i} characters."
                break
                
            state["agent_message"] = f"Analyzing {char_name} ({i+1}/{len(character_names)})…"
            
            # 1. RAG Situations
            situations = get_character_situations(state["vectorstore"], char_name, k=10)
            
            # Simple check if found
            words = [w for w in char_name.split() if len(w) > 2]
            if not words: words = [char_name]
            found = any(re.search(rf"\b{re.escape(word)}\b", text, re.IGNORECASE) 
                        for text in situations for word in words)
            
            if not situations or not found:
                state["agent_message"] = f"Skipping {char_name}: Not found in text."
                state["agent_progress"] = i + 1
                continue
                
            # 2. Analyze
            full_context = "\n\n---\n\n".join(situations)
            description = analyze_character(full_context, char_name, llm_provider, llm_model)
            
            # 3. Scenarios
            scenarios = get_scenario_summaries(state["vectorstore"], char_name, llm_provider, llm_model)
            
            # 4. Casting (Optional)
            actor_name = ""
            if use_casting:
                state["agent_message"] = f"Casting actor for {char_name}…"
                actor_name = cast_character_with_actor(
                    char_name, description, industry, genre=genre, decade=decade,
                    llm_provider=llm_provider, llm_model=llm_model
                )
            
            # 5. Generate at least 2 prompts
            prompts = []
            num_prompts = min(2, len(scenarios))
            for j in range(num_prompts):
                state["agent_message"] = f"Generating prompt {j+1}/2 for {char_name}…"
                p = generate_prompt_for_scenario(
                    char_name, description, scenarios[j]["context"],
                    actor_name=actor_name, genre=genre, decade=decade,
                    llm_provider=llm_provider, llm_model=llm_model
                )
                prompts.append(p)
            
            # 6. Save
            cached_descriptions[char_name] = {
                "description": description,
                "scenarios": scenarios,
                "image_prompt_ids": [],
                "prompts": prompts
            }
            
            state["agent_progress"] = i + 1
            
        # Final save
        if book_name not in library:
            library[book_name] = {"characters": [], "descriptions": {}}
        library[book_name]["descriptions"] = cached_descriptions
        save_library(library)
        
        state["agent_status"] = "done"
        if not state.get("agent_abort"):
            state["agent_message"] = f"Successfully analyzed {len(character_names)} characters with casting and prompts."
        
    except Exception as exc:
        import traceback
        traceback.print_exc()
        state["agent_status"] = "error"
        state["agent_message"] = f"Agent Error: {exc}"
        
    import time
    time.sleep(5)
    if state["agent_status"] in ("done", "error"):
        state["agent_status"] = "idle"


@app.post("/api/batch-analyze-characters")
async def batch_analyze_characters(req: BatchAnalyzeRequest):
    if state["vectorstore"] is None:
        raise HTTPException(status_code=400, detail="No book loaded.")
        
    if state["agent_status"] == "running":
        raise HTTPException(status_code=409, detail="Agent is already busy.")
        
    state["agent_status"] = "running"
    state["agent_total"] = len(req.character_names)
    state["agent_progress"] = 0
    state["agent_message"] = "Initializing character analysis..."
    
    t = threading.Thread(
        target=batch_analyze_task,
        args=(
            req.character_names, req.use_casting, req.genre, 
            req.decade, req.industry, req.llm_provider, req.llm_model
        ),
        daemon=True
    )
    t.start()
    state["agent_abort"] = False
    return {"status": "started"}


@app.post("/api/abort-agent")
async def abort_agent():
    """Request the current background agent task to stop."""
    if state["agent_status"] == "running":
        state["agent_abort"] = True
        state["agent_message"] = "Abort requested..."
        return {"status": "aborting"}
    return {"status": "idle"}


@app.post("/api/cast-actor")
async def cast_actor(req: CastActorRequest):
    try:
        actor = cast_character_with_actor(
            req.character_name, 
            req.description, 
            req.industry,
            genre=req.genre,
            decade=req.decade,
            llm_provider=req.llm_provider,
            llm_model=req.llm_model
        )
        return {"actor_name": actor}
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"Casting failed: {exc}")

@app.post("/api/generate-prompt")
async def generate_prompt(req: GeneratePromptRequest):
    try:
        result = generate_prompt_for_scenario(
            req.character_name,
            req.description,
            req.scenario_context,
            actor_name=req.actor_name,
            genre=req.genre,
            decade=req.decade,
            gender=req.gender,
            race=req.race,
            age=req.age,
            prompt_type=req.prompt_type,
            llm_provider=req.llm_provider,
            llm_model=req.llm_model
        )
        return {"prompt": result}
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"Prompt generation failed: {exc}")


@app.post("/api/generate-group-prompt")
async def generate_group_prompt(req: GenerateGroupPromptRequest):
    try:
        library = load_library()
        book_info = library.get(state.get("book_title"), {})
        descriptions = book_info.get("descriptions", {})
        
        char_desc_texts = []
        for name in req.character_names:
            if name in descriptions and descriptions[name].get("description"):
                char_desc_texts.append(f"{name}:\n{descriptions[name]['description']}")
            else:
                char_desc_texts.append(f"{name}:\n(No description available - try analyzing this character first)")
                
        combined_descriptions = "\n\n".join(char_desc_texts)
        
        from character_gen import generate_group_media_prompts
        result = generate_group_media_prompts(
            combined_descriptions,
            req.scenario_context,
            genre=req.genre,
            llm_provider=req.llm_provider,
            llm_model=req.llm_model
        )
        return result
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"Group prompt generation failed: {exc}")


# ---------------------------------------------------------------------------
# Image Generation Helpers (Refactored for batch use)
# ---------------------------------------------------------------------------

async def generate_single_image_comfy(comfy_url: str, workflow_json: str, prompt_text: str, node_id: Optional[str] = None) -> str:
    """Helper to generate one image on ComfyUI and return prompt_id."""
    workflow = json.loads(workflow_json)
    modified_wf, used_node = await asyncio.get_event_loop().run_in_executor(
        None, lambda: inject_prompt_into_workflow(workflow, prompt_text, node_id)
    )
    prompt_id = await asyncio.get_event_loop().run_in_executor(
        None, queue_prompt, comfy_url, modified_wf
    )
    
    poll_count = 0
    while poll_count < COMFYUI_POLL_LIMIT:
        poll_count += 1
        history_entry = await asyncio.get_event_loop().run_in_executor(
            None, lambda: _single_poll(comfy_url, prompt_id)
        )
        if history_entry is not None:
            break
        await asyncio.sleep(COMFYUI_POLL_INTERVAL)
    else:
        raise RuntimeError(f"ComfyUI timeout after {COMFYUI_POLL_LIMIT} polls")
        
    img_bytes, filename = await asyncio.get_event_loop().run_in_executor(
        None, get_output_image_bytes, comfy_url, history_entry
    )
    
    # Persist to disk with a unique name based on prompt_id
    ext = filename.rsplit(".", 1)[-1] if "." in filename else "png"
    unique_filename = f"{prompt_id}.{ext}"
    filepath = OUTPUT_DIR / unique_filename
    with open(filepath, "wb") as f:
        f.write(img_bytes)
        
    comfy_image_store[prompt_id] = (img_bytes, unique_filename)
    return prompt_id


async def generate_single_image_gemini(prompt_text: str, model: str = None) -> str:
    """Helper to generate one image on Gemini and return prompt_id."""
    prompt_id = f"gemini_{uuid.uuid4().hex[:8]}"
    
    def do_gen():
        from google import genai
        from google.genai import types
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key: raise RuntimeError("Missing Gemini API Key")
        client = genai.Client(api_key=api_key)
        m = model or os.getenv("GEMINI_IMAGE_MODEL", "gemini-3.1-flash-image-preview")
        result = client.models.generate_images(
            model=m,
            prompt=prompt_text,
            config=types.GenerateImagesConfig(number_of_images=1, output_mime_type="image/jpeg")
        )
        if not result.generated_images: raise RuntimeError("Gemini returned no images")
        return result.generated_images[0].image.image_bytes
        
    img_bytes = await asyncio.get_event_loop().run_in_executor(None, do_gen)
    
    # Persist to disk
    filename = f"{prompt_id}.jpg"
    filepath = OUTPUT_DIR / filename
    with open(filepath, "wb") as f:
        f.write(img_bytes)
        
    comfy_image_store[prompt_id] = (img_bytes, filename)
    return prompt_id


def batch_image_gen_task(req_dict: dict):
    """Background task for batch image generation."""
    # We use a dict here because of threading/asyncio complexity in a simple way
    char_names = req_dict["character_names"]
    count = req_dict["images_per_character"]
    gen_type = req_dict["generator_type"]
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        state["agent_status"] = "running"
        state["agent_total"] = len(char_names) * count
        state["agent_progress"] = 0
        
        book_name = state["book_title"]
        library = load_library()
        book_info = library.get(book_name, {})
        descriptions = book_info.get("descriptions", {})
        
        total_idx = 0
        for char_name in char_names:
            if state.get("agent_abort"):
                state["agent_message"] = f"Aborted by user. Finished {total_idx} images."
                break
                
            desc_entry = descriptions.get(char_name)
            if not desc_entry or not desc_entry.get("prompts"):
                state["agent_message"] = f"Skipping {char_name}: No prompts found."
                total_idx += count
                state["agent_progress"] = total_idx
                continue
                
            prompts = desc_entry["prompts"]
            
            for i in range(count):
                # Rotate through available prompts for variety
                prompt_text = prompts[i % len(prompts)]
                state["agent_message"] = f"Generating image {i+1}/{count} for {char_name}…"
                
                try:
                    if gen_type == "comfyui":
                        p_id = loop.run_until_complete(generate_single_image_comfy(
                            req_dict["comfy_url"], req_dict["workflow_json"], 
                            prompt_text, req_dict["node_id"]
                        ))
                    else:
                        p_id = loop.run_until_complete(generate_single_image_gemini(
                            prompt_text, req_dict.get("gemini_model")
                        ))
                    
                    # Update library: append to list
                    if "image_prompt_ids" not in desc_entry:
                        desc_entry["image_prompt_ids"] = []
                    if p_id not in desc_entry["image_prompt_ids"]:
                        desc_entry["image_prompt_ids"].append(p_id)
                except Exception as e:
                    print(f"Error generating for {char_name}: {e}")
                    state["agent_message"] = f"Error for {char_name}: {str(e)[:50]}"
                
                if state.get("agent_abort"):
                    break
                    
                total_idx += 1
                state["agent_progress"] = total_idx
                
        save_library(library)
        state["agent_status"] = "done"
        if not state.get("agent_abort"):
            state["agent_message"] = f"Finished generating {total_idx} images."
    except Exception as exc:
        state["agent_status"] = "error"
        state["agent_message"] = f"Image Agent Error: {exc}"
    finally:
        loop.close()
        
    import time
    time.sleep(5)
    if state["agent_status"] in ("done", "error"):
        state["agent_status"] = "idle"


@app.post("/api/batch-generate-images")
async def batch_generate_images(req: BatchImageRequest):
    if state["agent_status"] == "running":
        raise HTTPException(status_code=409, detail="Agent is already busy.")
        
    state["agent_status"] = "running"
    state["agent_total"] = len(req.character_names) * req.images_per_character
    state["agent_progress"] = 0
    state["agent_message"] = "Initializing image generation..."
    
    req_dict = req.dict()
    t = threading.Thread(target=batch_image_gen_task, args=(req_dict,), daemon=True)
    t.start()
    state["agent_abort"] = False
    return {"status": "started"}


# ---------------------------------------------------------------------------
# Batch Location Image Generation Agent
# ---------------------------------------------------------------------------

class BatchLocationImageRequest(BaseModel):
    location_names: list[str]
    images_per_location: int = 1
    generator_type: str = "gemini"   # "comfyui" | "gemini"
    comfy_url: str = "http://localhost:8188"
    workflow_json: str = ""
    node_id: str = ""
    gemini_model: Optional[str] = None


def batch_location_image_task(req_dict: dict):
    """Background task: generates images for selected locations."""
    loc_names  = req_dict["location_names"]
    count      = req_dict["images_per_location"]
    gen_type   = req_dict["generator_type"]

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        state["agent_status"]   = "running"
        state["agent_total"]    = len(loc_names) * count
        state["agent_progress"] = 0

        book_name = state["book_title"]
        library   = load_library()
        book_info = library.get(book_name, {})
        locations = book_info.setdefault("locations", {})

        total_idx = 0
        for loc_name in loc_names:
            if state.get("agent_abort"):
                state["agent_message"] = f"Aborted after {total_idx} images."
                break

            loc_entry = locations.get(loc_name)
            if not loc_entry or not loc_entry.get("prompts"):
                state["agent_message"] = f"Skipping {loc_name}: no saved prompts."
                total_idx += count
                state["agent_progress"] = total_idx
                continue

            prompts = loc_entry["prompts"]

            for i in range(count):
                if state.get("agent_abort"):
                    break
                prompt_text = prompts[i % len(prompts)]
                state["agent_message"] = f"Generating image {i+1}/{count} for {loc_name}…"
                try:
                    if gen_type == "comfyui":
                        p_id = loop.run_until_complete(generate_single_image_comfy(
                            req_dict["comfy_url"], req_dict["workflow_json"],
                            prompt_text, req_dict["node_id"]
                        ))
                    else:
                        p_id = loop.run_until_complete(generate_single_image_gemini(
                            prompt_text, req_dict.get("gemini_model")
                        ))
                    ids = loc_entry.setdefault("image_prompt_ids", [])
                    if p_id not in ids:
                        ids.append(p_id)
                except Exception as e:
                    state["agent_message"] = f"Error for {loc_name}: {str(e)[:60]}"

                total_idx += 1
                state["agent_progress"] = total_idx

        save_library(library)
        state["agent_status"]  = "done"
        if not state.get("agent_abort"):
            state["agent_message"] = f"Finished generating {total_idx} location images."
    except Exception as exc:
        state["agent_status"]  = "error"
        state["agent_message"] = f"Location Agent Error: {exc}"
    finally:
        loop.close()
        
    import time
    time.sleep(5)
    if state["agent_status"] in ("done", "error"):
        state["agent_status"] = "idle"


@app.post("/api/batch-generate-location-images")
async def batch_generate_location_images(req: BatchLocationImageRequest):
    if state["agent_status"] == "running":
        raise HTTPException(status_code=409, detail="Agent is already busy.")
        
    state["agent_status"] = "running"
    state["agent_total"] = len(req.location_names) * req.images_per_location
    state["agent_progress"] = 0
    state["agent_message"] = "Initializing location image generation..."
    
    req_dict = req.dict()
    t = threading.Thread(target=batch_location_image_task, args=(req_dict,), daemon=True)
    t.start()
    state["agent_abort"] = False
    return {"status": "started"}


# ---------------------------------------------------------------------------
# Locations Endpoints
# ---------------------------------------------------------------------------

class LocationAnalysisRequest(BaseModel):
    location_name: str
    llm_provider: Optional[str] = None
    llm_model: Optional[str] = None

class LocationPromptRequest(BaseModel):
    book_name: str
    location_name: str
    description: str
    genre: str = ""
    decade: str = "2026"
    time_of_day: str = ""
    weather: str = ""
    llm_provider: Optional[str] = None
    llm_model: Optional[str] = None

class SaveLocationPromptRequest(BaseModel):
    book_name: str
    location_name: str
    prompt: str

class DeleteLocationDataRequest(BaseModel):
    book_name: str
    location_name: str
    delete_prompts_only: bool = True


@app.post("/api/extract-locations")
async def extract_locations(req: LocationAnalysisRequest):
    """Use RAG + LLM to extract prominent locations from the loaded book."""
    if state["vectorstore"] is None:
        raise HTTPException(status_code=400, detail="No book loaded.")
    try:
        locations = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: extract_prominent_locations(
                state["vectorstore"],
                req.llm_provider,
                req.llm_model
            )
        )
        return {"locations": locations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/analyze-location")
async def analyze_location_endpoint(req: LocationAnalysisRequest):
    """Use RAG + LLM to describe a specific location from the book."""
    if state["vectorstore"] is None:
        raise HTTPException(status_code=400, detail="No book loaded.")
    try:
        description = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: analyze_location(
                state["vectorstore"],
                req.location_name,
                req.llm_provider,
                req.llm_model
            )
        )
        # Persist the description to library
        book_name = state.get("book_title", "")
        if book_name:
            library = load_library()
            book_info = library.setdefault(book_name, {"characters": [], "descriptions": {}})
            locs = book_info.setdefault("locations", {})
            if req.location_name not in locs:
                locs[req.location_name] = {"description": description, "prompts": [], "image_prompt_ids": []}
            else:
                locs[req.location_name]["description"] = description
            save_library(library)
        return {"description": description}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/generate-landscape-prompt")
async def generate_landscape_prompt_endpoint(req: LocationPromptRequest):
    """Generate a Z-Image Turbo landscape prompt for a book location."""
    if not req.description:
        raise HTTPException(status_code=400, detail="Description is required.")
    try:
        prompt = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: generate_landscape_prompt(
                req.location_name,
                req.description,
                req.genre,
                req.decade,
                req.time_of_day,
                req.weather,
                req.llm_provider,
                req.llm_model
            )
        )
        return {"prompt": prompt}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/save-location-prompt")
async def save_location_prompt(req: SaveLocationPromptRequest):
    """Append a prompt to a location's library entry."""
    library = load_library()
    book_info = library.setdefault(req.book_name, {"characters": [], "descriptions": {}})
    locs = book_info.setdefault("locations", {})
    entry = locs.setdefault(req.location_name, {"description": "", "prompts": [], "image_prompt_ids": []})
    if req.prompt not in entry["prompts"]:
        entry["prompts"].append(req.prompt)
    save_library(library)
    return {"prompts": entry["prompts"]}


@app.post("/api/save-location-image")
async def save_location_image(book_name: str, location_name: str, prompt_id: str):
    """Associate a generated image with a location entry."""
    library = load_library()
    book_info = library.setdefault(book_name, {"characters": [], "descriptions": {}})
    locs = book_info.setdefault("locations", {})
    entry = locs.setdefault(location_name, {"description": "", "prompts": [], "image_prompt_ids": []})
    if prompt_id not in entry["image_prompt_ids"]:
        entry["image_prompt_ids"].append(prompt_id)
    save_library(library)
    return {"ok": True}


@app.get("/api/locations/{book_name}")
async def get_locations(book_name: str):
    """Return the locations dictionary for the given book."""
    library = load_library()
    book_info = library.get(book_name, {})
    return {"locations": book_info.get("locations", {})}


@app.post("/api/delete-location-data")
async def delete_location_data(req: DeleteLocationDataRequest):
    """Delete prompts/images or the full entry for a location."""
    library = load_library()
    book_info = library.get(req.book_name, {})
    locs = book_info.get("locations", {})
    if req.location_name not in locs:
        raise HTTPException(status_code=404, detail="Location not found.")
    if req.delete_prompts_only:
        locs[req.location_name]["prompts"] = []
        locs[req.location_name]["image_prompt_ids"] = []
    else:
        del locs[req.location_name]
    save_library(library)
    return {"ok": True}


# ---------------------------------------------------------------------------
# Debug / Diagnostics Endpoints
# ---------------------------------------------------------------------------

@app.get("/api/debug/system-test")
async def system_test():
    """Run a suite of diagnostic tests for the backend systems."""
    results = {
        "library": {"status": "pending", "message": ""},
        "vectorstore": {"status": "pending", "message": ""},
        "llm": {"status": "pending", "message": ""},
        "character_gen": {"status": "pending", "message": ""}
    }
    
    # 1. Library Persistence Test
    try:
        lib = load_library()
        test_key = f"__debug_test_{uuid.uuid4().hex[:6]}"
        lib[test_key] = "test_value"
        save_library(lib)
        
        reloaded = load_library()
        if reloaded.get(test_key) == "test_value":
            results["library"] = {"status": "ok", "message": "Read/Write successful"}
        else:
            results["library"] = {"status": "error", "message": "Data verification failed"}
            
        # Cleanup
        del reloaded[test_key]
        save_library(reloaded)
    except Exception as e:
        results["library"] = {"status": "error", "message": f"Library failed: {str(e)}"}

    # 2. Vectorstore Test
    if state["vectorstore"] is None:
        results["vectorstore"] = {"status": "warning", "message": "No book loaded yet"}
    else:
        try:
            # Simple similarity search test
            docs = state["vectorstore"].similarity_search("test", k=1)
            results["vectorstore"] = {"status": "ok", "message": f"Search active (found {len(docs)} docs)"}
        except Exception as e:
            results["vectorstore"] = {"status": "error", "message": f"Search failed: {str(e)}"}

    # 3. LLM Connectivity Test
    try:
        resp = generate_text("Hello, this is a diagnostic test. Please reply with only the word 'OK'.")
        if "OK" in resp.upper():
            results["llm"] = {"status": "ok", "message": f"LLM responded: {resp}"}
        else:
            results["llm"] = {"status": "warning", "message": f"LLM responded but failed check: {resp}"}
    except Exception as e:
        results["llm"] = {"status": "error", "message": f"LLM failed: {str(e)}"}

    # 4. Character Gen Logic Test
    try:
        dummy_context = "Alice is a tall woman with red hair and a kind smile."
        char_desc = analyze_character(dummy_context, "Alice")
        if char_desc and len(char_desc) > 10:
            results["character_gen"] = {"status": "ok", "message": "Character analysis logic verified"}
        else:
            results["character_gen"] = {"status": "error", "message": "Empty analysis returned"}
    except Exception as e:
        results["character_gen"] = {"status": "error", "message": f"CharacterGen failed: {str(e)}"}

    return results


# ---------------------------------------------------------------------------
# ComfyUI endpoints
# ---------------------------------------------------------------------------

# In-memory store: prompt_id -> image bytes (single-user dev app)
comfy_image_store: dict[str, tuple[bytes, str]] = {}


@app.post("/api/comfyui/test")
async def comfyui_test(req: ComfyUITestRequest):
    """Verify that a ComfyUI instance is reachable."""
    try:
        stats = await asyncio.get_event_loop().run_in_executor(
            None, test_connection, req.comfy_url
        )
        return {"ok": True, "stats": stats}
    except Exception as exc:
        raise HTTPException(status_code=503, detail=str(exc))


@app.post("/api/comfyui/generate")
async def comfyui_generate(req: ComfyUIGenerateRequest):
    """
    Inject the prompt into the workflow, queue it on ComfyUI, poll for
    completion, cache the image, and stream SSE progress events.

    SSE event shapes:
      {"status": "queued",     "prompt_id": "...", "message": "..."}
      {"status": "polling",   "prompt_id": "...", "message": "..."}
      {"status": "done",      "prompt_id": "...", "message": "..."}
      {"status": "error",     "message": "..."}
    """
    async def event_stream():
        try:
            # Parse workflow
            try:
                workflow = json.loads(req.workflow_json)
            except json.JSONDecodeError as e:
                yield f"data: {json.dumps({'status': 'error', 'message': f'Invalid workflow JSON: {e}'})}\n\n"
                return

            # Inject prompt
            try:
                modified_wf, used_node = await asyncio.get_event_loop().run_in_executor(
                    None,
                    lambda: inject_prompt_into_workflow(workflow, req.prompt_text, req.node_id),
                )
            except ValueError as e:
                yield f"data: {json.dumps({'status': 'error', 'message': str(e)})}\n\n"
                return

            yield f"data: {json.dumps({'status': 'injecting', 'message': f'Prompt injected into node {used_node}. Queueing…'})}\n\n"

            # Queue
            try:
                prompt_id = await asyncio.get_event_loop().run_in_executor(
                    None, queue_prompt, req.comfy_url, modified_wf
                )
            except RuntimeError as e:
                yield f"data: {json.dumps({'status': 'error', 'message': str(e)})}\n\n"
                return

            yield f"data: {json.dumps({'status': 'queued', 'prompt_id': prompt_id, 'message': f'Queued as {prompt_id[:8]}… Waiting for ComfyUI…'})}\n\n"

            # Poll
            poll_count = 0
            while poll_count < COMFYUI_POLL_LIMIT:
                poll_count += 1
                yield f"data: {json.dumps({'status': 'polling', 'prompt_id': prompt_id, 'message': f'Generating image… (poll #{poll_count})'})}\n\n"
                try:
                    history_entry = await asyncio.get_event_loop().run_in_executor(
                        None,
                        lambda: _single_poll(req.comfy_url, prompt_id),
                    )
                    if history_entry is None:  # not done yet
                        await asyncio.sleep(COMFYUI_POLL_INTERVAL)
                        continue
                except RuntimeError as e:
                    yield f"data: {json.dumps({'status': 'error', 'message': str(e)})}\n\n"
                    return
                break
            else:
                yield f"data: {json.dumps({'status': 'error', 'message': f'Polling timed out after {COMFYUI_POLL_LIMIT} attempts.'})}\n\n"
                return

            # Fetch image
            yield f"data: {json.dumps({'status': 'fetching', 'prompt_id': prompt_id, 'message': 'Downloading image from ComfyUI…'})}\n\n"
            try:
                img_bytes, filename = await asyncio.get_event_loop().run_in_executor(
                    None, get_output_image_bytes, req.comfy_url, history_entry
                )
            except RuntimeError as e:
                yield f"data: {json.dumps({'status': 'error', 'message': str(e)})}\n\n"
                return

            # Persist to disk
            filepath = OUTPUT_DIR / filename
            with open(filepath, "wb") as f:
                f.write(img_bytes)

            # Cache and signal done
            comfy_image_store[prompt_id] = (img_bytes, filename)
            yield f"data: {json.dumps({'status': 'done', 'prompt_id': prompt_id, 'filename': filename, 'message': 'Image ready!'})}\n\n"

        except Exception as exc:
            yield f"data: {json.dumps({'status': 'error', 'message': f'Unexpected error: {exc}'})}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


def _single_poll(comfy_url: str, prompt_id: str) -> dict:
    """
    One-shot poll of /history/{prompt_id}.
    Returns the history entry if done, returns None if still running,
    raises RuntimeError on error.
    """
    url = comfy_url.rstrip("/") + f"/history/{prompt_id}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception:
        return None

    if prompt_id not in data:
        return None

    entry = data[prompt_id]
    status = entry.get("status", {})
    msgs = status.get("messages", [])
    for msg_type, msg_data in msgs:
        if msg_type == "execution_error":
            raise RuntimeError(f"ComfyUI execution error: {msg_data}")
    if status.get("completed", False) or "outputs" in entry:
        return entry
    return None


@app.post("/api/gemini/generate-image")
async def gemini_generate_image(req: GeminiImageRequest):
    """
    Queue an image generation request to Gemini and return an SSE stream.
    SSE event shapes:
      {"status": "queued", "prompt_id": "...", "message": "..."}
      {"status": "done", "prompt_id": "...", "filename": "...", "message": "..."}
      {"status": "error", "message": "..."}
    """
    async def event_stream():
        try:
            prompt_id = f"gemini_{uuid.uuid4().hex[:8]}"
            yield f"data: {json.dumps({'status': 'queued', 'prompt_id': prompt_id, 'message': 'Calling Gemini API...'})}\n\n"
            
            def do_gen():
                try:
                    from google import genai
                    from google.genai import types
                except ImportError:
                    raise RuntimeError("google-genai package is not installed. Run: pip install google-genai")
                
                api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
                if not api_key:
                    raise RuntimeError("GEMINI_API_KEY or GOOGLE_API_KEY environment variable is missing")
                
                client = genai.Client(api_key=api_key)
                model = req.model or os.getenv("GEMINI_IMAGE_MODEL", "gemini-3.1-flash-image-preview")
                result = client.models.generate_images(
                    model=model,
                    prompt=req.prompt_text,
                    config=types.GenerateImagesConfig(
                        number_of_images=1,
                        output_mime_type="image/jpeg",
                        aspect_ratio="1:1"
                    )
                )
                if not result.generated_images:
                    raise RuntimeError("Gemini API returned no images")
                return result.generated_images[0].image.image_bytes
            
            img_bytes = await asyncio.get_event_loop().run_in_executor(None, do_gen)
            
            filename = f"{prompt_id}.jpg"
            filepath = OUTPUT_DIR / filename
            with open(filepath, "wb") as f:
                f.write(img_bytes)

            comfy_image_store[prompt_id] = (img_bytes, filename)
            
            yield f"data: {json.dumps({'status': 'done', 'prompt_id': prompt_id, 'filename': filename, 'message': 'Image ready!'})}\n\n"
        except Exception as exc:
            yield f"data: {json.dumps({'status': 'error', 'message': f'Gemini error: {exc}'})}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.get("/api/image/{prompt_id}")
@app.get("/api/comfyui/image/{prompt_id}")
async def fetch_image(prompt_id: str):
    """Serve the cached image for a completed job."""
    # 1. Check in-memory cache
    if prompt_id in comfy_image_store:
        img_bytes, filename = comfy_image_store[prompt_id]
    else:
        # 2. Check disk (output_images folder)
        # Look for .png or .jpg with this prompt_id as name
        match = None
        for ext in ["png", "jpg", "jpeg"]:
            p = OUTPUT_DIR / f"{prompt_id}.{ext}"
            if p.exists():
                match = p
                break
        
        if not match:
            raise HTTPException(status_code=404, detail="Image not found. Generate first.")
            
        with open(match, "rb") as f:
            img_bytes = f.read()
        filename = match.name

    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else "png"
    media_type = "image/jpeg" if ext in ("jpg", "jpeg") else "image/png"
    return Response(content=img_bytes, media_type=media_type)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host=BACKEND_HOST, port=BACKEND_PORT, reload=BACKEND_RELOAD)

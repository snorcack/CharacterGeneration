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
from typing import Any, Optional
import urllib.request
import urllib.parse
import urllib.error

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, Response
from pydantic import BaseModel

from character_gen import (
    get_major_character_names,
    build_book_index,
    get_scenario_summaries,
    analyze_character,
    get_character_situations,
    cast_character_with_actor,
    generate_prompt_for_scenario,
)
from comfyui import (
    inject_prompt_into_workflow,
    queue_prompt,
    poll_until_done,
    get_output_image_bytes,
    test_connection,
)

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
}


# ---------------------------------------------------------------------------
# Background indexing thread
# ---------------------------------------------------------------------------

def load_book_task(book_path: str, book_name: str) -> None:
    """Runs in a daemon thread; writes progress into `state`."""
    try:
        state["job_status"] = "running"
        state["characters"] = []
        state["vectorstore"] = None
        state["book_title"] = book_name
        state["error"] = None

        # Step 1 — Wikipedia characters
        state["stage"] = "wikipedia"
        state["progress"] = 0
        state["total"] = 1
        state["message"] = f"Fetching major characters from Wikipedia for '{book_name}'…"

        characters = get_major_character_names(book_name)
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


class CharacterDetailsRequest(BaseModel):
    character_name: str


class CastActorRequest(BaseModel):
    character_name: str
    description: str
    industry: str = "hollywood"
    genre: str = ""
    decade: str = "2026"


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


class ComfyUITestRequest(BaseModel):
    comfy_url: str


class ComfyUIGenerateRequest(BaseModel):
    comfy_url: str
    workflow_json: str          # raw JSON string (API-format)
    prompt_text: str
    node_id: Optional[str] = None


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

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
        args=(req.book_path, req.book_name),
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


@app.post("/api/character-details")
async def character_details(req: CharacterDetailsRequest):
    if state["vectorstore"] is None:
        raise HTTPException(
            status_code=400,
            detail="No book loaded. Call /api/load-book first.",
        )

    try:
        # Retrieve a top scene for baseline description
        situations = get_character_situations(
            state["vectorstore"], req.character_name, k=1
        )
        context_text = situations[0] if situations else ""
        description = analyze_character(context_text, req.character_name)

        # Get RAG-derived scenario list (6 scenes, each summarised)
        scenarios = get_scenario_summaries(state["vectorstore"], req.character_name)

        return {"description": description, "scenarios": scenarios}
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"LLM analytics failed: {exc}")


@app.post("/api/cast-actor")
async def cast_actor(req: CastActorRequest):
    try:
        actor = cast_character_with_actor(
            req.character_name, 
            req.description, 
            req.industry,
            genre=req.genre,
            decade=req.decade
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
            age=req.age
        )
        return {"prompt": result}
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"Prompt generation failed: {exc}")


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
            poll_limit = 100
            while poll_count < poll_limit:
                poll_count += 1
                yield f"data: {json.dumps({'status': 'polling', 'prompt_id': prompt_id, 'message': f'Generating image… (poll #{poll_count})'})}\n\n"
                try:
                    history_entry = await asyncio.get_event_loop().run_in_executor(
                        None,
                        lambda: _single_poll(req.comfy_url, prompt_id),
                    )
                    if history_entry is None:  # not done yet
                        await asyncio.sleep(2)
                        continue
                except RuntimeError as e:
                    yield f"data: {json.dumps({'status': 'error', 'message': str(e)})}\n\n"
                    return
                break
            else:
                yield f"data: {json.dumps({'status': 'error', 'message': f'Polling timed out after {poll_limit} attempts.'})}\n\n"
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


@app.get("/api/comfyui/image/{prompt_id}")
async def comfyui_image(prompt_id: str):
    """Serve the cached image for a completed ComfyUI job."""
    if prompt_id not in comfy_image_store:
        raise HTTPException(status_code=404, detail="Image not found. Generate first.")
    img_bytes, filename = comfy_image_store[prompt_id]
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else "png"
    media_type = "image/jpeg" if ext in ("jpg", "jpeg") else "image/png"
    return Response(content=img_bytes, media_type=media_type)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

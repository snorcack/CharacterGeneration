"""
comfyui.py
----------
Helper module for interacting with a local ComfyUI instance.

Public API
----------
inject_prompt_into_workflow(workflow, prompt_text, node_id=None) -> dict
queue_prompt(comfy_url, workflow) -> str
poll_until_done(comfy_url, prompt_id, timeout=180) -> dict
get_output_image_bytes(comfy_url, history_entry) -> bytes
randomize_seeds(workflow) -> None
"""

import json
import time
import uuid
import urllib.request
import urllib.parse
import urllib.error
from typing import Optional


# ---------------------------------------------------------------------------
# 1. Inject the SD prompt into the workflow JSON
# ---------------------------------------------------------------------------

def _find_prompt_node(workflow: dict) -> Optional[str]:
    """
    Auto-detect the best node to inject the positive prompt into.

    Priority order:
      1. Node whose class_type == "CLIPTextEncode" and whose text contains
         any of the trigger keywords (positive, pos, prompt) — case-insensitive
         match on the node's _meta.title if present.
      2. First CLIPTextEncode node with the longest existing text
         (heuristic: positive prompt is usually longer than the negative).
      3. First CLIPTextEncode found.
    """
    clip_nodes: list[tuple[str, dict]] = []
    for node_id, node in workflow.items():
        if isinstance(node, dict) and node.get("class_type") == "CLIPTextEncode":
            clip_nodes.append((node_id, node))

    if not clip_nodes:
        return None

    # Priority 1 — meta title hint
    positive_keywords = {"positive", "pos", "prompt", "text"}
    for nid, node in clip_nodes:
        title = (node.get("_meta") or {}).get("title", "").lower()
        if any(kw in title for kw in positive_keywords):
            return nid

    # Priority 2 — longest text (positive prompts tend to be verbose)
    clip_nodes.sort(key=lambda x: len(x[1].get("inputs", {}).get("text", "")), reverse=True)
    return clip_nodes[0][0]


def inject_prompt_into_workflow(
    workflow: dict,
    prompt_text: str,
    node_id: Optional[str] = None,
) -> tuple[dict, str]:
    """
    Replace the 'text' input of the target CLIPTextEncode node with `prompt_text`.

    Returns (modified_workflow, used_node_id).
    Raises ValueError if no suitable node can be found.
    """
    import copy
    wf = copy.deepcopy(workflow)

    target_id = node_id or _find_prompt_node(wf)
    if target_id is None:
        raise ValueError(
            "No CLIPTextEncode node found in the workflow. "
            "Please specify a node_id manually."
        )

    if target_id not in wf:
        raise ValueError(f"Node '{target_id}' not found in workflow.")

    wf[target_id]["inputs"]["text"] = prompt_text
    
    # Also randomize seeds to ensure variety in batch generation
    randomize_seeds(wf)
    
    return wf, target_id


def randomize_seeds(workflow: dict) -> None:
    """
    Find any node inputs named 'seed' or 'noise_seed' that are 
    currently set to a numeric value, and randomize them.
    """
    import random
    for node_id, node in workflow.items():
        if not isinstance(node, dict):
            continue
        inputs = node.get("inputs", {})
        for key in inputs:
            if key in ("seed", "noise_seed"):
                # Only randomize if it's a number (not a link/list)
                if isinstance(inputs[key], (int, float)):
                    inputs[key] = random.randint(0, 0xffffffffffffffff)


# ---------------------------------------------------------------------------
# 2. Queue the prompt / POST to ComfyUI
# ---------------------------------------------------------------------------

def queue_prompt(comfy_url: str, workflow: dict) -> str:
    """
    POST the workflow to ComfyUI's /prompt endpoint.
    Returns the prompt_id (UUID string).
    """
    client_id = str(uuid.uuid4())
    payload = json.dumps({"prompt": workflow, "client_id": client_id}).encode("utf-8")
    url = comfy_url.rstrip("/") + "/prompt"

    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"ComfyUI /prompt failed ({e.code}): {body}") from e

    prompt_id = data.get("prompt_id")
    if not prompt_id:
        raise RuntimeError(f"No prompt_id in ComfyUI response: {data}")

    return prompt_id


# ---------------------------------------------------------------------------
# 3. Poll /history until done
# ---------------------------------------------------------------------------

def poll_until_done(
    comfy_url: str,
    prompt_id: str,
    timeout: int = 180,
    poll_interval: float = 1.5,
) -> dict:
    """
    Poll GET /history/{prompt_id} until the job appears in history.
    Returns the history entry for the completed prompt.
    Raises TimeoutError if `timeout` seconds elapse.
    """
    base = comfy_url.rstrip("/")
    url = f"{base}/history/{prompt_id}"
    deadline = time.time() + timeout
    req = urllib.request.Request(url, headers={"Accept": "application/json"})

    while time.time() < deadline:
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except Exception:
            time.sleep(poll_interval)
            continue

        if prompt_id in data:
            entry = data[prompt_id]
            status = entry.get("status", {})
            if status.get("completed", False) or "outputs" in entry:
                return entry
            # Check for error
            msgs = status.get("messages", [])
            for msg_type, msg_data in msgs:
                if msg_type == "execution_error":
                    raise RuntimeError(f"ComfyUI execution error: {msg_data}")

        time.sleep(poll_interval)

    raise TimeoutError(
        f"ComfyUI job {prompt_id} did not complete within {timeout}s."
    )


# ---------------------------------------------------------------------------
# 4. Retrieve the output image bytes
# ---------------------------------------------------------------------------

def get_output_image_bytes(comfy_url: str, history_entry: dict) -> tuple[bytes, str]:
    """
    Extract the first output image from a history entry and fetch its bytes.
    Returns (image_bytes, filename).
    """
    base = comfy_url.rstrip("/")
    outputs = history_entry.get("outputs", {})

    for _node_id, node_output in outputs.items():
        images = node_output.get("images", [])
        for img in images:
            filename = img.get("filename", "")
            subfolder = img.get("subfolder", "")
            img_type = img.get("type", "output")

            params = urllib.parse.urlencode({
                "filename": filename,
                "subfolder": subfolder,
                "type": img_type,
            })
            view_url = f"{base}/view?{params}"
            req = urllib.request.Request(view_url)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read(), filename

    raise RuntimeError("No output images found in ComfyUI history entry.")


# ---------------------------------------------------------------------------
# 5. Quick connectivity test
# ---------------------------------------------------------------------------

def test_connection(comfy_url: str) -> dict:
    """
    GET /system_stats to verify ComfyUI is reachable.
    Returns parsed JSON on success, raises on failure.
    """
    url = comfy_url.rstrip("/") + "/system_stats"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise ConnectionError(f"Cannot reach ComfyUI at {comfy_url}: {e.reason}") from e

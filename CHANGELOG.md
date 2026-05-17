# Changelog

All notable changes to this project will be documented in this file.

---

## [Unreleased]

### Added

#### 📍 Locations Tab
- New **Locations** tab in the main UI alongside Character Studio, AI Agents, and Character Gallery.
- **RAG-powered location extraction** — scans book passages and uses the LLM to identify prominent named locations, buildings, and landmarks automatically.
- Manual location entry via a text input field.
- **Location analysis** — retrieves relevant book passages via RAG and generates a vivid visual description of each location (architecture, atmosphere, mood).
- **Landscape prompt generation** with configurable parameters:
  - Genre / Style (e.g. Gothic, Steampunk, Pastoral)
  - Decade (period cinematography style)
  - Time of Day (golden hour, blue hour, night, stormy, etc.)
  - Weather & Atmosphere (fog, rain, snow, heat haze, etc.)
- **Gemini image generation** for locations with 16:9 landscape aspect ratio.
- Swipeable **16:9 image carousel** per location (supports multiple generated images).
- Prompt save, copy, and re-use workflow per location.
- Clear media and full delete options per location entry.
- Location data (descriptions, prompts, image IDs) persisted to `library.json`.

#### 🖼️ Character Gallery — Multi-Image Carousel
- Gallery now displays a **swipeable image carousel** per character instead of a single static image.
- Navigation arrows and animated dot indicators shown on hover.
- Each new batch-generated image is **appended** to the character's image list rather than overwriting it.
- Library schema updated: `image_prompt_id` (singular) migrated to `image_prompt_ids` (list) with backward-compatible reading of old data.
- Gallery layout changed to a responsive grid (`repeat(auto-fill, minmax(600px, 1fr))`).
- Lightbox support for full-screen image viewing.

#### 🤖 Agent Abort
- **Abort button** added to both the **Character Analysis Agent** (Multi-Character Agent panel) and the **Batch Image Generation Agent**.
- New `/api/abort-agent` backend endpoint sets a global abort flag checked between each character/image iteration.
- Abort flag is automatically reset when a new agent task is started.
- The agent reports how many items were completed before the abort.

#### 🎲 Batch Image Generation — Seed Randomization & Prompt Rotation
- Each image in a batch now uses a **randomized seed** (injected into the ComfyUI workflow's `seed` / `noise_seed` nodes) to guarantee unique outputs.
- **Prompt rotation** — if a character has multiple saved prompts, the batch agent cycles through them instead of repeating the first one.
- Generated images are saved with **unique filenames** based on the ComfyUI `prompt_id`, preventing file collisions.

### Changed

- `comfyui.py`: `inject_prompt_into_workflow` now also calls `randomize_seeds` on every workflow injection.
- `comfyui.py`: Added new `randomize_seeds(workflow)` helper that randomizes all numeric `seed` / `noise_seed` inputs in the workflow graph.
- `character_gen.py`: Added `extract_prominent_locations`, `analyze_location`, and `generate_landscape_prompt` functions.
- `prompts.json`: Added `extract_locations`, `location_analysis`, `location_situation_query`, and `landscape_image_prompt` prompt templates.
- `main.py`: Library schema uses `image_prompt_ids: []` (list) for both characters and locations. Old `image_prompt_id` entries are auto-migrated on read.
- `main.py`: Batch image generation endpoint now resets `agent_abort` to `False` on each new run.
- `BatchImageGenerator.jsx`: Agent status box shows a red **Abort Generation** button while running.
- `GroupSceneFinder.jsx`: Agent status box shows a red **Abort Analysis** button while running.
- `DescriptionCarousel.jsx`: Updated to read `image_prompt_ids[0]` (new list format) for the sidebar thumbnail, with fallback to legacy `image_prompt_id`.

### Fixed

- Batch image generation no longer produces identical images — seeds are randomized per image in the loop.
- Characters with a single saved prompt no longer fail batch generation when `images_per_character > 1`.
- Gallery cards no longer appear outside the visible area — layout corrected with proper grid and sizing.

---

## [0.1.0] — Initial Release

- Book loading from `.txt` and `.epub` files with RAG vector index (ChromaDB + HuggingFace embeddings).
- Wikipedia-assisted character name extraction.
- Character description generation via RAG + LLM (Ollama, OpenAI, Anthropic, Gemini).
- Scenario selector with RAG-derived scene summaries.
- Image and video prompt generation via Z-Image Turbo / LTX Video templates.
- Actor casting suggestion per character and industry (Hollywood, Bollywood, etc.).
- ComfyUI integration — workflow injection, queue, polling, and image serving.
- Gemini image generation integration (`gemini-3.1-flash-image-preview`).
- Multi-character group scene finder with shared scene detection.
- Batch character analysis agent with SSE progress streaming.
- Batch image generation agent.
- Character Gallery tab.
- Prompt Studio with multi-prompt management (save, edit, delete per character).
- Prompt history panel in the right sidebar.
- Dark glassmorphism UI (Outfit font, purple/gold palette).
- Task Manager widget and Lightbox for full-screen image preview.
- Collapsible sidebars.
- ComfyUI Debugger / diagnostics view.

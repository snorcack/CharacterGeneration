# 🎭 Character Portrait Generator

A powerful, AI-driven pipeline for generating cinematic character portraits directly from literary works. This application uses Retrieval-Augmented Generation (RAG) to analyze books, identify major characters, and generate context-aware image prompts for local ComfyUI instances.

![Project Preview](https://img.shields.io/badge/Aesthetics-Glassmorphism-blueviolet?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/Tech-FastAPI%20%7C%20React%20%7C%20LangChain-blue?style=for-the-badge)
![AI Model](https://img.shields.io/badge/LLM-Ollama%20(Gemma4E4B)-orange?style=for-the-badge)

## ✨ Features

- **📖 Intelligent Book Parsing**: Automatically load `.txt` books and build a high-performance vector index using ChromaDB and HuggingFace Embeddings.
- **🔍 Wikipedia Augmentation**: Scrapes Wikipedia to identify major characters and establish baseline personas before the book analysis even begins.
- **🤖 Deep RAG Analysis**: Retrieves specific scenes from the book to understand character appearance, clothing, and environment in different contexts.
- **🎬 AI Casting Director**: Suggests real-world actors (Hollywood, Bollywood, etc.) to serve as the visual "base" for the character, with support for specific decades (e.g., 1920s Noir, 1980s Sci-Fi).
- **🎭 Genre Adaptation**: Dynamically modifies clothing, hairstyles, and cinematic styles to fit genres (Horror, Cyberpunk, Fantasy, etc.) while preserving the character's core identity (age, ethnicity, facial features).
- **🖼️ ComfyUI Integration**: Seamlessly connect to your local ComfyUI server. Inject prompts into API-format workflows, track generation progress via Server-Sent Events (SSE), and preview images instantly.
- **✨ Premium UI**: A sleek, dark glassmorphism dashboard built with React and Vite for a modern, responsive feel.

## 🛠️ Technology Stack

- **Backend**: Python 3.10+, FastAPI, LangChain
- **Vector DB**: ChromaDB
- **Embeddings**: HuggingFace (`all-MiniLM-L6-v2`)
- **LLM**: Ollama (`Gemma4E4B:latest` or similar)
- **Frontend**: React, Vite, Vanilla CSS
- **Image Gen**: ComfyUI (Local Instance)

## 🚀 Getting Started

### Prerequisites

1.  **Ollama**: Install [Ollama](https://ollama.com/) and pull the required model:
    ```bash
    ollama pull Gemma4E4B:latest
    ```
2.  **ComfyUI**: Have a local [ComfyUI](https://github.com/comfyanonymous/ComfyUI) instance running.
3.  **Python & Node**: Ensure you have Python 3.10+ and Node.js installed.

### Installation

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/CharacterGenerationFromBook.git
    cd CharacterGenerationFromBook
    ```

2.  **Backend Setup**:
    ```bash
    cd backend
    pip install -r requirements.txt
    ```

3.  **Frontend Setup**:
    ```bash
    cd ../frontend
    npm install
    ```

### Running the App

You can start both services with a single command on Windows:
```bash
./run_app.bat
```

Alternatively, run them manually:
- **Backend**: `cd backend && python main.py` (Runs on port 8000)
- **Frontend**: `cd frontend && npm run dev` (Runs on port 5173)

## 📖 How to Use

1.  **Load a Book**: Point the app to a `.txt` file of a novel. The system will build a vector index and fetch character names from Wikipedia.
2.  **Choose a Character**: Select a character from the identified list.
3.  **Analyze & Customize**: The AI will generate a description and retrieve several scenes (scenarios). You can cast an actor to ground the visual appearance.
4.  **Configure Generation**: Select a genre, decade, and image generation parameters.
5.  **Generate**: Connect to ComfyUI, paste your API workflow JSON, and hit generate. Watch the progress in real-time until your portrait appears!

## 📁 Project Structure

```text
CharacterGenerationFromBook/
├── backend/            # FastAPI Server
│   ├── character_gen.py # RAG & LLM Logic
│   ├── comfyui.py      # ComfyUI API Integration
│   └── main.py          # API Endpoints
├── frontend/           # Vite + React UI
│   ├── src/            # Components & Styles
│   └── index.html
└── run_app.bat         # Windows Launcher
```

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

*Wowed by the portraits? Star the repo!* 🌟

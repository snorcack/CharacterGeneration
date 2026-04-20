
import sys
import json

backend_path = r'k:\UnityProjects\AgenticAiProjects\LLM_annotate\CharacterGenerationFromBook\backend'
if backend_path not in sys.path:
    sys.path.append(backend_path)

from character_gen import get_major_character_names

book_name = "Mistborn" # Famous book with wiki page
try:
    print(f"Testing Wikipedia character extraction for '{book_name}'...")
    chars = get_major_character_names(book_name)
    print(f"Found characters: {chars}")
except Exception as e:
    import traceback
    traceback.print_exc()


import os
import sys

# Add backend to path
backend_path = r'k:\UnityProjects\AgenticAiProjects\LLM_annotate\CharacterGenerationFromBook\backend'
if backend_path not in sys.path:
    sys.path.append(backend_path)

from character_gen import build_book_index

def progress_cb(stage, n, total, msg):
    print(f"[{stage}] {n}/{total} - {msg}")

# Use a sample file if available or just check if it fails on a non-existent one
test_file = r'k:\UnityProjects\AgenticAiProjects\LLM_annotate\CharacterGenerationFromBook\backend\test_book.txt'
with open(test_file, 'w', encoding='utf-8') as f:
    f.write("This is a test book content. Character named Alice was here. Bob was also here.")

try:
    print("Starting build_book_index test...")
    vs = build_book_index(test_file, progress_cb=progress_cb)
    print("Success!")
except Exception as e:
    import traceback
    print("FAILED with error:")
    traceback.print_exc()
finally:
    if os.path.exists(test_file):
        os.remove(test_file)

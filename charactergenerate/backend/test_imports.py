"""
Diagnostic script: tests each import in isolation and writes results to test_imports.log
Run with: python test_imports.py
"""
import sys
import traceback

log_path = "test_imports.log"

def test(label, fn):
    try:
        fn()
        msg = f"[OK]  {label}\n"
    except Exception as e:
        msg = f"[ERR] {label}: {type(e).__name__}: {e}\n{traceback.format_exc()}\n"
    print(msg, end="")
    with open(log_path, "a") as f:
        f.write(msg)

# Clear log
with open(log_path, "w") as f:
    f.write(f"Python: {sys.version}\n\n")

print(f"Python: {sys.version}\n")

test("dotenv",          lambda: __import__("dotenv"))
test("fastapi",         lambda: __import__("fastapi"))
test("uvicorn",         lambda: __import__("uvicorn"))
test("pydantic",        lambda: __import__("pydantic"))
test("ollama",          lambda: __import__("ollama"))
test("langchain_community.document_loaders.TextLoader",
     lambda: __import__("langchain_community.document_loaders", fromlist=["TextLoader"]))
test("langchain_text_splitters",
     lambda: __import__("langchain_text_splitters"))
test("langchain_chroma",
     lambda: __import__("langchain_chroma"))
test("langchain_huggingface",
     lambda: __import__("langchain_huggingface"))
test("sentence_transformers",
     lambda: __import__("sentence_transformers"))

print("\nDone. See test_imports.log for full output.")

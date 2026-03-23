import sys
import os

# Add service root to path
sys.path.append(os.getcwd())

print("Testing imports for LanceVectorStore...")
try:
    import numpy as np
    print(f"NumPy version: {np.__version__}")
    
    import lancedb
    print(f"LanceDB successfully imported.")
    
    from services.memory.core.lance_store import LanceVectorStore
    print("LanceVectorStore class successfully imported.")
    
    # Try initialization (without Ollama if possible, or just mock it)
    print("Attempting initialization...")
    store = LanceVectorStore(uri="./tmp/lance_test")
    print("✅ Success! Initialization worked.")
    
except Exception as e:
    print(f"❌ Failure: {e}")
    import traceback
    traceback.print_exc()

if __name__ == "__main__":
    pass

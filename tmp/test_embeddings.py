import asyncio
from langchain_community.embeddings import OllamaEmbeddings

async def test_embedding():
    model = "nomic-embed-text"
    print(f"Testing embeddings with model: {model}...")
    embeddings = OllamaEmbeddings(model=model, base_url="http://localhost:11434")
    try:
        vector = await embeddings.aembed_query("Hello world, this is a test of the AI memory layer.")
        print(f"Success! Vector length: {len(vector)}")
        print(f"First 5 values: {vector[:5]}")
    except Exception as e:
        print(f"Failed to generate embeddings with {model}: {e}")

if __name__ == "__main__":
    asyncio.run(test_embedding())

import requests
import json
import time

def test_full_pipeline():
    url = "http://localhost:8080/memories"
    payload = {
        "owner_id": "manager-1",
        "content": "The quarterly project rating is currently at 8/10 for Backend completion.",
        "metadata": {"type": "report", "priority": "high"}
    }
    
    print(f"Ingesting memory to {url}...")
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        print("Success! Response received.")
        print(f"Memory ID: {data.get('id')}")
        print(f"Vector Length: {len(data.get('vector', []))}")
        
        if len(data.get('vector', [])) > 0:
            print("✅ Brain Test: Vector generated successfully!")
        else:
            print("❌ Brain Test: Vector is still empty!")
            
        # Verify persistence
        print("\nChecking persistence...")
        get_url = f"http://localhost:8080/memories/manager-1"
        get_resp = requests.get(get_url)
        memories = get_resp.json()
        if any(m['id'] == data.get('id') for m in memories):
            print("✅ Storage Test: Memory persistent and retrieved!")
        else:
            print("❌ Storage Test: Memory NOT found in retrieval!")
            
    except Exception as e:
        print(f"Error during API test: {e}")

if __name__ == "__main__":
    test_full_pipeline()

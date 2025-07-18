# app/debug_check_collection.py

from app.vector_store import get_chroma_client

def debug_collection():
    db = get_chroma_client()
    collection = db.get_or_create_collection(name="pdf_documents")

    total_docs = collection.count()
    print(f"📦 Total embedded chunks: {total_docs}")

    if total_docs == 0:
        print("⚠️ No documents found in the collection.")
        return

    print("\n🔍 Sample Documents:\n")
    sample = collection.peek(5)
    for i, doc in enumerate(sample['documents'], 1):
        print(f"{i}. {doc[:200]}...\n")  # Preview first 200 characters

if __name__ == "__main__":
    debug_collection()

import chromadb
from chromadb.config import Settings

def store_embeddings(chunks, embeddings):
    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection(name="medical_rag")

    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        collection.add(
            documents=[chunk],
            embeddings=[emb.tolist()],
            ids=[f"chunk_{i}"]
        )

def get_chroma_client():
    client = chromadb.PersistentClient(path="chroma_db")
    return client


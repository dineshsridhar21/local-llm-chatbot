# app/query_pdf.py

from app.vector_store import get_chroma_client
from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model (same as used in embedder.py)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
db = get_chroma_client()
collection = db.get_or_create_collection(name="medical_rag")


def retrieve_similar_chunks(query, top_k=3):
    # Embed the user query
    query_embedding = model.encode(query).tolist()

    # Perform similarity search
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    # Extract texts
    return results["documents"][0]

# Example usage
if __name__ == "__main__":
    user_query = input("Enter your query: ")
    similar_chunks = retrieve_similar_chunks(user_query)

    print("\nTop Matching Chunks:\n")
    for i, chunk in enumerate(similar_chunks, 1):
        print(f"{i}. {chunk}\n")

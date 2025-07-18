# app/query_pdf.py

from app.vector_store import get_chroma_client
from sentence_transformers import SentenceTransformer
import subprocess

# Load embedding model (same as in embed_pdf.py)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
db = get_chroma_client()
collection = db.get_or_create_collection(name="pdf_documents")

def retrieve_similar_chunks(query, top_k=3):
    # Embed the user query
    query_embedding = model.encode(query).tolist()

    # Perform similarity search
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]  # top-k chunks

def generate_with_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode()

def format_prompt(context_chunks, query):
    context = "\n\n".join(context_chunks)
    prompt = f"""Answer the question using the context below.

Context:
{context}

Question: {query}

Answer:"""
    return prompt

# This is what Streamlit will call
def ask_question(query):
    chunks = retrieve_similar_chunks(query)
    prompt = format_prompt(chunks, query)
    response = generate_with_ollama(prompt)
    return response.strip()

# Keep CLI functionality if run directly
if __name__ == "__main__":
    user_query = input("Enter your query: ")
    print("\n LLM Answer:\n")
    print(ask_question(user_query))


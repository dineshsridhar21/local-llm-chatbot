from app.pdf_loader import load_and_split_pdf
from app.embedder import embed_text_chunks
from app.vector_store import store_embeddings

print("Loading and splitting PDF...")
chunks = load_and_split_pdf("data/sample.pdf")

print(f"Split into {len(chunks)} chunks. Creating embeddings...")
embeddings = embed_text_chunks(chunks)

print("Storing into Chroma DB...")
store_embeddings(chunks, embeddings)
print(f"Done! Stored {len(chunks)} chunks in Chroma vector DB.")


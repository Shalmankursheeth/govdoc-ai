from sentence_transformers import SentenceTransformer

# Load embeddings model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(text: str):
    """Convert text to embedding vector."""
    return embedding_model.encode(text)

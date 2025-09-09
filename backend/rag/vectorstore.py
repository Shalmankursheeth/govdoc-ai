import chromadb
from chromadb.config import Settings
from rag.embeddings import embedding_model


client = chromadb.PersistentClient(
    path="./chroma",
    settings=Settings()
)

collection = client.get_or_create_collection("gov_docs")

def add_doc(doc_id: str, text: str):
    vector = embedding_model.encode(text)
    collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[vector]
    )

def query_docs(query_text: str, n_results: int = 3):
    vector = embedding_model.encode(query_text)
    results = collection.query(query_embeddings=[vector], n_results=n_results)
    return results["documents"][0] if results else []

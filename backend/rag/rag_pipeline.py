from transformers import pipeline
from rag.vectorstore import query_docs
from utils.logger import logger

# Generator model for RAG (free)
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def query(question: str):
    """Run RAG pipeline: retrieve relevant docs + generate answer"""
    try:
        docs = query_docs(question)
        if not docs:
            return "No relevant documents found."
        context = "\n".join(docs)
        input_text = f"Context: {context}\nQuestion: {question}\nAnswer:"
        answer = generator(input_text, max_length=200, do_sample=False)[0]["generated_text"]
        return answer
    except Exception as e:
        logger.error(f"RAG query failed: {str(e)}")
        return "Error generating answer."

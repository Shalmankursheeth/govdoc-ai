from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils import pdf_reader, schema
from models import summarizer, decision_extractor, entity_extractor
from rag import rag_pipeline
from database import mongo_db
from utils.logger import logger

app = FastAPI(title="GovDoc-AI", version="1.0.0")

# Enable CORS (for frontend React app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "GovDoc-AI backend is running 🚀"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """Upload and process a government document (PDF/TXT)."""
    try:
        text = await pdf_reader.extract_text(file)
        if not text.strip():
            raise HTTPException(status_code=400, detail="Empty document")

        # Run AI pipelines
        summary = summarizer.generate_summary(text)
        decisions = decision_extractor.extract_decisions(text)
        entities = entity_extractor.extract_entities(text)

        # Store in MongoDB
        doc_id = mongo_db["documents"].insert_one({
            "filename": file.filename,
            "summary": summary,
            "decisions": decisions,
            "entities": entities
        }).inserted_id

        return {
            "doc_id": str(doc_id),
            "summary": summary,
            "decisions": decisions,
            "entities": entities
        }

    except Exception as e:
        logger.error(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Document processing failed")

@app.post("/query")
async def query_rag(request: schema.QueryRequest):
    """Query the RAG pipeline with natural language."""
    try:
        answer = rag_pipeline.query(request.question)
        return {"answer": answer}
    except Exception as e:
        logger.error(f"RAG query failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Query failed")

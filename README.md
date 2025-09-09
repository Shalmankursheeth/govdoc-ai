# GovDoc-AI

**AI-powered platform to analyze, summarize, and extract key decisions and entities from government documents** using open-source LLMs, LangChain, and vector databases.  

This project makes **policy documents, legal texts, and public records** accessible and actionable via an easy-to-use web dashboard.

---

## 🚀 Features

- Upload PDF or TXT documents
- Automatic **summarization** (BART)
- **Decision extraction** (regex / ML-ready)
- **Named entity recognition** (BERT-based NER)
- **Query documents** with **RAG pipeline** (LangChain + ChromaDB)
- Analytics dashboard for summaries and entities
- Fully deployable using **Render / Docker / Netlify / Vercel**
- 100% free, no OpenAI API key required

---

## 🏗️ Tech Stack

### Backend
- **FastAPI** → REST API
- **MongoDB Atlas (Free Tier)** → Document storage
- **ChromaDB** → Vector database for semantic search
- **Hugging Face Transformers** → Open-source LLMs
  - Summarizer: `facebook/bart-large-cnn`
  - Entity Extraction: `dbmdz/bert-large-cased-finetuned-conll03-english`
  - Embeddings: `sentence-transformers/all-MiniLM-L6-v2`
- **LangChain** → RAG orchestration pipeline

### Frontend
- **React (Vite + TailwindCSS)**
- **ShadCN + Recharts** → UI components + analytics
- **Axios** → API communication

### Deployment
- **Render Free Tier** → Backend & Frontend hosting
- **Docker** → Local development & production parity

---

## 📂 Project Structure

govdoc-ai/
│── backend/
│ ├── app.py
│ ├── models/
│ │ ├── summarizer.py
│ │ ├── decision_extractor.py
│ │ └── entity_extractor.py
│ ├── utils/
│ │ ├── pdf_reader.py
│ │ ├── schema.py
│ │ └── logger.py
│ ├── rag/
│ │ ├── embeddings.py
│ │ ├── vectorstore.py
│ │ ├── rag_pipeline.py
│ │ └── query_router.py
│ └── requirements.txt
│
│── frontend/
│ ├── src/
│ │ ├── App.jsx
│ │ ├── components/
│ │ │ ├── UploadForm.jsx
│ │ │ ├── SummaryCard.jsx
│ │ │ ├── DecisionCard.jsx
│ │ │ └── EntityList.jsx
│ │ └── main.jsx
│ └── package.json
│
│── docker-compose.yml
│── Dockerfile.backend
│── Dockerfile.frontend
│── render.yaml
│── README.md






---

---

## 💻 Local Setup

### Backend

- cd backend
- python -m venv venv
- venv\Scripts\activate     # Windows
- source venv/bin/activate # Linux/Mac
- pip install -r requirements.txt
- uvicorn app:app --reload --host 0.0.0.0 --port 8000




### Frontend

- cd frontend
- npm install
- npm run dev


### Docker

- docker-compose up --build


import pdfplumber
from fastapi import UploadFile
from io import BytesIO

async def extract_text(file: UploadFile) -> str:
    """Extract text from PDF or TXT files."""
    content = await file.read()
    filename = file.filename.lower()

    # TXT files
    if filename.endswith(".txt"):
        return content.decode("utf-8")

    # PDF files
    elif filename.endswith(".pdf"):
        text = ""
        with pdfplumber.open(BytesIO(content)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text.strip()

    else:
        raise ValueError("Unsupported file type. Only PDF and TXT are allowed.")

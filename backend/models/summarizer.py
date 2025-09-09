from transformers import pipeline
from utils.logger import logger

# Load once (avoid reloading on every request)
try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    logger.info("Summarizer model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load summarizer: {str(e)}")
    summarizer = None

def generate_summary(text: str, max_len: int = 200, min_len: int = 50) -> str:
    """Generate summary from text using BART model."""
    if not summarizer:
        return "Summarizer not available."
    try:
        summary = summarizer(
            text,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )[0]["summary_text"]
        return summary
    except Exception as e:
        logger.error(f"Summarization failed: {str(e)}")
        return "Error generating summary."

import re
from utils.logger import logger

def extract_decisions(text: str):
    """
    Extract decisions from government/legal docs.
    Very simple keyword + regex based (could be extended with ML).
    """
    try:
        # Look for common decision markers
        decisions = re.findall(r"(decides?|resolved|ordered|approved|denied).+", text, flags=re.IGNORECASE)
        return decisions if decisions else ["No explicit decisions found."]
    except Exception as e:
        logger.error(f"Decision extraction failed: {str(e)}")
        return ["Error extracting decisions."]

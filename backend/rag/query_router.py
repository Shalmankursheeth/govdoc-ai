from models import summarizer, decision_extractor, entity_extractor

def route_query(question: str):
    """Optional: route question to specific pipeline."""
    q_lower = question.lower()
    if "summarize" in q_lower:
        return summarizer.generate_summary(question)
    elif "decision" in q_lower or "who" in q_lower:
        return decision_extractor.extract_decisions(question)
    elif "entity" in q_lower or "organization" in q_lower:
        return entity_extractor.extract_entities(question)
    else:
        return None  # Default → RAG pipeline

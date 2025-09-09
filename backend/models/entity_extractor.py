from transformers import pipeline
from utils.logger import logger

# models/entity_extractor.py
from transformers import pipeline

# Smaller NER model
ner_model = pipeline(
    "ner",
    model="dslim/bert-base-NER",  # ~110MB instead of 1.3GB
    aggregation_strategy="simple"
)

from loguru import logger

# Configure loguru
logger.add("logs/backend.log", rotation="5 MB", retention="10 days", level="INFO")
logger.add(lambda msg: print(msg, end=""), level="INFO")

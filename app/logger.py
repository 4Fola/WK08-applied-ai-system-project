"""
Logging utilities for AI system behavior.
"""

import logging

# WK08 §4 Reliability and Evaluation: Structured logging
logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_event(message: str):
    logging.info(message)
    


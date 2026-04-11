"""
Logging utilities for AI system behavior.
"""

import logging
from pathlib import Path

# WK08 §4 Reliability and Evaluation: Structured logging
log_path = Path(__file__).parent.parent / "system.log"

logging.basicConfig(
    filename=str(log_path),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_event(message: str) -> None:
    logging.info(message)

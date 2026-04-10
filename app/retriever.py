"""
Retrieval module for known game glitches.
"""

import json
from pathlib import Path

# WK08 §1 Functionality: Retrieval-Augmented Generation (RAG)
def retrieve_known_glitch(glitch_report: str) -> dict | None:
    """
    Retrieve known glitch data based on keyword matching.
    """

    data_path = Path("data/known_glitches.json")
    
    with open(data_path, "r") as file:
        known_glitches = json.load(file)
        
    report_lower = glitch_report.lower()
    
    for glitch in known_glitches.values():
        if any(keyword in report_lower for keyword in glitch["keywords"]):
            return glitch
        
    return None




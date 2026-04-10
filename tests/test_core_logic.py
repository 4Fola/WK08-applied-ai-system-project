"""
Automated tests for AI core logic.
"""

from app.agent import analyze_glitch

# WK08 §4 Reliability: Automated evaluation
def test_known_glitch():
    result = analyze_glitch("Th game crashes on startup")
    assert result["confidence"] > 0.5

def test_unknown_glitch():
    result = analyze_glitch("Something weird happens")
    assert result["confidence"] < 0.5

def test_invalid_input():
    result = analyze_glitch("")
    assert result["diagnosis"] == "Invalid input"

# WK08 Requirement | Evidence
# End‑to‑end run   | CLI + Web UI
# Reliability      | Automated tests
# Explainability   | Reasoning + confidence
# Presentation     | Demo‑ready UI

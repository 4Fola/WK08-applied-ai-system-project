"""
Core reasoning logic for Game Glitch Investigator.
"""

from app.retriever import retrieve_known_glitch
from app.evaluator import score_confidence
from app.validator import validate_input
from app.logger import log_event

# WK08 §1 Functionality: Core reasoning module | Agentic reasoning using retrieved evidence
def analyze_glitch(glitch_report: str) -> dict:
    """
    Analyze a game glitch report and return a diagnosis using retrieved knowledge.
    """

    # WK08 §5 Ethics: Input validation
    if not validate_input(glitch_report):
        log_event("Rejected invalid input")
        return {
            "diagnosis": "Invalid input",
            "explanation": "Please provide a clearer description of the glitch.",
            "confidence": 0.0,
            "reasoning_summary": "Input validation failed"
        }
    
    log_event("input accepted for analysis")

    # Step I: Interpret input
    interpreted_issue = glitch_report.lower()

    # Step II: Retieve evidence
    retrieved = retrieve_known_glitch(interpreted_issue)

    # Step III: Hypothesis + verification
    if retrieved:
        diagnosis = retrieved["cause"]
        explanation = retrieved["fix"]
        reasoning_path = "Matched known glitch pattern"
    else:
        diagnosis = "Unknown glitch"
        explanation = "No known matches / supporting evidence found. More information is required."
        reasoning_path = "No match/known patterns found in knowledge base"

    # Step IV: Reliability scoring
    confidence = score_confidence(retrieved is not None)

    return {
        "diagnosis": diagnosis,
        "explanation": explanation,
        "confidence": confidence,
        "reasoning_summary": reasoning_path
    }


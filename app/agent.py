"""
Core reasoning logic for Game Glitch Investigator.
"""

# WK08 §1 Functionality: Core reasoning module
def analyze_glitch(glitch_report: str) -> dict:
    """
    Analyze a game glitch report and return a diganosis.
    """
    # WK08 §1: Baseline reasoning (pre-AI extension)
    diagnosis = "Unknown glitch"
    explanation = "Insufficient information provided."

    if "crash" in glitch_report.lower():
        diagnosis = "Game Crash"
        explanation = "The report suggests the game is unexpectedly terminating."

    return {
        "diagnosis": diagnosis,
        "explanation": explanation
    }

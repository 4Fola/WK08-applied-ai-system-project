"""
Core reasoning logic for Game Glitch Investigator.
"""

from app.retriever import retrieve_known_glitch

# WK08 §1 Functionality: Core reasoning module | Agentic reasoning using retrieved evidence
def analyze_glitch(glitch_report: str) -> dict:
    """
    Analyze a game glitch report and return a diganosis using retrieved knowledge.
    """
    retrieved = retrieve_known_glitch(glitch_report)

    if retrieved:
        # WK08 §1: RAG-informed reasoning path
        diagnosis = retrieved["cause"]
        explanation = retrieved["fix"]
    else:
        # WK08 §4 Reliability: Safe fallback when knowledge is missing
        diagnosis = "Unkown glitch"
        explanation = "No known matches found. More information is required."

    return {
        "diagnosis": diagnosis,
        "explanation": explanation,
        "used_retrieval": retrieved is not None
    }




    # # WK08 §1: Baseline reasoning (pre-AI extension)
    # diagnosis = "Unknown glitch"
    # explanation = "Insufficient information provided."

    # if "crash" in glitch_report.lower():
    #     diagnosis = "Game Crash"
    #     explanation = "The report suggests the game is unexpectedly terminating."

    # return {
    #     "diagnosis": diagnosis,
    #     "explanation": explanation
    # }



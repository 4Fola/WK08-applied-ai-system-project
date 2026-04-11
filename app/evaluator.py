"""
Evaluation and confidence scoring for AI decisions.
"""

# WK08 §4 Reliability: Confidence scoring
def score_confidence(used_retrieval: bool) -> float:
    """
    Assign a confidence score based on evidence usage.
    If retrieval was used, the system reports higher confidence.
    """
    return 0.85 if used_retrieval else 0.40
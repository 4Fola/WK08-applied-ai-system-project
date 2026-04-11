"""
Input validation and guardrails.
"""

# WK08 §5 Ethics: Input validation guardrail
def validate_input(glitch_report: str) -> bool:
    """
    Ensure the input is non-empty and meaningful.
    """
    if not glitch_report:
        return False
    if len(glitch_report.strip()) < 5:
        return False
    return True

"""
✅ Prevents garbage input
✅ Explicit ethical safeguard
"""

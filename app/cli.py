"""
CLI interface for Game Glitch Investigator.
"""

from app.agent import analyze_glitch

# WK08 §1 Functionality: CLI entrypoint
def main():
    report = input("Describe the game glitch: ")
    result = analyze_glitch(report)

    print("\nDiagnosis:", result["diagnosis"])
    print("Explanation:", result["explanation"])
    print("Confidence:", result["confidence"])
    print("Reasoning:", result["reasoning_summary"])

if __name__ == "__main__":
    main()
    


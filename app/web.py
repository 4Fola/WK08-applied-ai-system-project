"""
Flask web interface for Game Glitch Investigator 2.0.
"""

from flask import Flask, render_template, request
from pathlib import Path
from app.agent import analyze_glitch

# Configure Flask to use templates from the project root
template_dir = Path(__file__).parent.parent / "templates"
app = Flask(__name__, template_folder=str(template_dir))

# WK08 §1 Functionality: Web-based system interaction
@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        glitch_report = request.form.get("glitch_report", "")
        result = analyze_glitch(glitch_report)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=False)

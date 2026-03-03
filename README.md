# 🎮 Game Glitch Investigator: The Impossible Guesser

# NB:
### App Web Dashboard
<img src="demos/GameGlitch.gif" alt="Game Glitch web UI">

### `What was broken?`  
### `What was broken?`
- Logically wrong functions in e.g., search_songs, compute_playlist_stats etc.
- Security / maintainability: unusual import deferment
- No unit test(s)

### `Recommendations`  
- Reverse search conditions
- Correct ratios computations
- Copy lists
- Consider adding unit tests

## Summary:

- Core Concept Needed: knowledge on input normalization, deterministic classification rules etc. maybe useful to understand predictable application behavior.
- Possible Learning Struggle: subtle logic bugs such as wrong denominators for averages, list alias during merge, empty inputs handling.
- AI Help: AI can be helpful in locating concrete issues, impact explanation and targeted improvement suggestions.
- AI Mislead: possible inference in design intentions in situations where behaviour might be legitimate choices.
- Scholar Guide: suggest going through a single example song and show its normal form, classification decision and where it ends up. Consider an intentional failing unit test to capture the unexpected behaviour.

# NB END:

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

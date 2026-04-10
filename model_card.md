# 👉 [Model Card](model_card.md) | [ReadMe](README.md) |

# 🎮 Model Card | Game Glitch Investigator 2.0: The Impossible Guesser

## 🧠 `model_card.md` (Responsible AI Reflection)

## Intended Use
This system is designed to assist users in diagnosing common video game glitches.
It is not intended to replace professional technical support.

## AI Components
- Retrieval-Augmented Generation (RAG)
- Agentic reasoning workflow
- Confidence scoring
- Input validation and logging

## Limitations and Biases
The system relies on a limited knowledge base and may fail on novel or complex glitches.
Keyword-based retrieval may miss relevant cases with unusual phrasing.

## Misuse Prevention
- The system explicitly reports uncertainty.
- Invalid or vague inputs are rejected.
- No autonomous actions are taken.

## Reliability Observations
The system performed consistently on known cases but struggled when insufficient context was provided.
Confidence scores helped surface uncertainty.

## Collaboration with AI
AI assistance was helpful in structuring modular logic and identifying guardrails.
In some cases, AI suggestions required simplification to maintain explainability.

User <br>
 ├─ CLI <br>
 └─ Web UI <br>
      ↓ <br>
Input Validator <br>
      ↓ <br>
Retriever (RAG) <br>
      ↓ <br>
Agentic Reasoning <br>
      ↓ <br>
Confidence Scorer <br>
      ↓ <br>
Output + Logs <br>


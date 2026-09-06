# GambitLens ♟️🔍
**Autonomous Agentic Telemetry Engine & Natural Language Tactical Coach**
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.14-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![MLOps](https://img.shields.io/badge/MLOps-Automated-orange)
---
## 📖 The Story Behind GambitLens
In competitive chess, high-level engines like Stockfish output raw numeric evaluations (+1.4, -3.2) and deep principal variations that remain cryptic to intermediate players. Existing commercial tools lock actionable coaching behind heavy paywalls.
Inspired by clinical triage systems like **AfyaTriage**, **GambitLens** was engineered as an open, autonomous agentic engine that transforms raw move-level telemetry into natural-language tactical coaching. It ingests move times, centipawn losses, and positional board states from Lichess, runs classification models to pinpoint blunders, and leverages LLM agents to deliver natural language feedback—democratizing elite grandmaster analysis at $0 operational cost.
---
## 🏗️ Production System Architecture
```
[ Lichess REST API ]
         │
         ▼
[ src/ingestion.py ] ────► Raw PGN & Telemetry Parsing
         │
         ▼
[ src/features.py ]  ────► Centipawn Loss (CPL) Delta Calculation
         │
         ▼
[ src/model.py ]     ────► Tactical Blunder Classifier
         │
  ┌──────┴───────────────────────┐
  ▼                              ▼
[ src/visuals.py ]      [ src/agent.py ]
  │                              │
  ▼                              ▼
(Pure SVG Asset Render)   (Groq LLM Coaching Insights)
```
---
## 📊 Live System Telemetry & Diagnostics
Below is an automatically generated SVG diagnostic chart rendering real-time evaluation drift across analyzed game plies:
![Centipawn Evaluation Drift](assets/centipawn_drift.svg)
---
## 🧪 Comprehensive Testing Suite
All engine components are covered by unit tests verified across Python environments:

| Module | Purpose | Test Status |
| :--- | :--- | :--- |
| `src/ingestion.py` | Lichess PGN stream parsing & eval regex extraction | ✅ Passed |
| `src/features.py` | Centipawn loss (CPL) & game phase tagging | ✅ Passed |
| `src/model.py` | Standalone blunder prediction model | ✅ Passed |
| `src/visuals.py` | Pure-Python SVG diagnostic chart generator | ✅ Passed |
| `src/agent.py` | LLM tactical coaching explanation fallback loop | ✅ Passed |

Full test logs are archived in [`docs/TEST_RESULTS.md`](docs/TEST_RESULTS.md).
---
## ⚡ Quick Start
```bash
# Clone repository
git clone [https://github.com/your-username/GambitLens.git](https://github.com/your-username/GambitLens.git)
cd GambitLens
# Install lightweight dependencies
pip install -r requirements.txt
# Execute test suite
pytest
# Run full pipeline
python -m src.main
```
---
## 🤖 Continuous Integration & Daily Streak Automation
GambitLens runs on an automated **GitHub Actions** schedule (`.github/workflows/daily_pipeline.yml`). Every 24 hours, the runner ingests fresh game telemetry, validates model accuracy, updates diagnostic SVG assets, and commits the output back to the repository—maintaining active contribution matrix activity.

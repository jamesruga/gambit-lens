# GambitLens ♟️🔍

[![Daily Pipeline](https://github.com/jamesruga/gambit-lens/actions/workflows/daily_pipeline.yml/badge.svg)](https://github.com/jamesruga/gambit-lens/actions/workflows/daily_pipeline.yml)
![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.14-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![MLOps](https://img.shields.io/badge/MLOps-Automated-orange)
![LLM Engine](https://img.shields.io/badge/LLM-Groq%20Llama3-7c3aed)

An open-source MLOps engine that ingests raw move-level chess telemetry from Lichess, trains automated blunder classifiers, and generates natural-language tactical coaching with pure-SVG diagnostic charts.

---

## 📖 The Story Behind GambitLens

In competitive chess, high-level engines like Stockfish output raw numeric evaluations (+1.4, -3.2) and deep principal variations that remain cryptic to intermediate players. Existing commercial tools lock actionable coaching behind heavy paywalls.

GambitLens was engineered as an open, autonomous agentic engine that transforms raw move-level telemetry into natural-language tactical coaching. It ingests move times, centipawn losses, and positional board states from Lichess, runs classification models to pinpoint blunders, and leverages LLM agents to deliver natural language feedback at zero operational cost.

---

## 🏗️ Production System Architecture

```
┌────────────────────┐      ┌────────────────────┐      ┌────────────────────┐
│  Lichess REST API  │ ───► │  src/ingestion.py  │ ───► │   src/features.py  │
└────────────────────┘      └────────────────────┘      └─────────┬──────────┘
                                                                  │
                                                                  ▼
┌────────────────────┐      ┌────────────────────┐      ┌────────────────────┐
│ (Pure SVG Visuals) │ ◄─── │   src/visuals.py   │ ◄─── │    src/model.py    │
└────────────────────┘      └────────────────────┘      └─────────┬──────────┘
                                                                  │
                                                                  ▼
┌────────────────────┐                                  ┌────────────────────┐
│ (Groq LLM Insights)│ ◄─────────────────────────────── │    src/agent.py    │
└────────────────────┘                                  └────────────────────┘
```

---

## 💡 Sample Tactical Coaching Output

```text
[Move 3 - White played 'g4' (Ply 3)]
  ⚠️ CRITICAL BLUNDER DETECTED (Centipawn Loss: -3.65)
  
  🤖 Tactical Agent Feedback:
  "White's move 3. g4 severely weakens the f2-g4 diagonal leading directly to the king.
   By pushing the g-pawn prematurely, White forfeits king safety before developing any
   minor pieces. Black can immediately exploit this positional flaw with 3... Qh4#,
   delivering a rapid Fool's Mate checkmate."
```

---

## 📊 Live System Telemetry & Diagnostics

Below are the automatically rendered SVG diagnostic charts presenting evaluation drift and clock duration correlation across analyzed game plies:

### Centipawn Evaluation Drift
![Centipawn Evaluation Drift](assets/centipawn_drift.svg)

### Move Clock Duration Telemetry
![Move Clock Duration Telemetry](assets/move_time_telemetry.svg)

---

## 🧪 Comprehensive Testing Suite

All engine components are covered by unit tests verified across Python environments:

| Module | Purpose | Test Status |
| :--- | :--- | :--- |
|  | Lichess PGN stream parsing & eval regex extraction | ✅ Passed |
|  | Centipawn loss (CPL) & game phase tagging | ✅ Passed |
|  | Standalone blunder prediction model | ✅ Passed |
|  | Pure-Python SVG diagnostic chart generator | ✅ Passed |
|  | LLM tactical coaching explanation fallback loop | ✅ Passed |

Full test logs are archived in [](docs/TEST_RESULTS.md).

---

## ⚡ Quick Start

```bash
# Clone repository
git clone https://github.com/jamesruga/gambit-lens.git
cd gambit-lens

# Install lightweight dependencies
pip install -r requirements.txt

# Execute test suite
pytest

# Run full pipeline
python -m src.main
```

---

## 🤖 Continuous Integration & Automated Workflows

GambitLens executes automatically on a daily schedule ([](.github/workflows/daily_pipeline.yml)). Every 24 hours, the runner ingests fresh game telemetry, validates model accuracy, updates diagnostic SVG assets, and synchronizes outputs back to the repository.

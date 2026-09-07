# GambitLens ♟️🔍

[![GambitLens Daily Automation](https://github.com/jamesruga/gambit-lens/actions/workflows/daily_pipeline.yml/badge.svg)](https://github.com/jamesruga/gambit-lens/actions/workflows/daily_pipeline.yml)
[![python](https://img.shields.io/badge/python-3.11%20%7C%203.14-blue)](https://www.python.org/)
[![license](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)
[![MLOps](https://img.shields.io/badge/MLOps-Automated-orange)](https://ml-ops.org/)
[![LLM](https://img.shields.io/badge/LLM-Groq%20Llama3-purple)](https://groq.com/)

An open-source MLOps engine that ingests raw move-level chess telemetry from [Lichess](https://lichess.org/), trains automated blunder classifiers, and generates natural-language tactical coaching with pure-SVG diagnostic charts.

---

## 📖 The Story Behind GambitLens

In competitive chess, high-level engines like Stockfish output raw numeric evaluations and deep principal variations that remain cryptic to intermediate players. Existing commercial tools lock actionable coaching behind heavy paywalls. GambitLens was engineered as an open, autonomous agentic engine that transforms raw move-level telemetry into natural-language tactical coaching at zero operational cost.

---

## 🏗️ Production System Architecture

```text
┌─────────────────────────────────────────┐
│ 1. Data Ingestion (src/ingestion.py)    │
└────────────────────┬────────────────────┘
                     │ Lichess PGN stream
                     v
┌─────────────────────────────────────────┐
│ 2. Feature Engineering (src/features.py)│
└────────────────────┬────────────────────┘
                     │ Centipawn loss / CPL
                     v
┌─────────────────────────────────────────┐
│ 3. Model Training (src/model.py)        │
└────────────────────┬────────────────────┘
                     │ Blunder classification
                     v
┌─────────────────────────────────────────┐
│ 4. Diagnostic Visuals (src/visuals.py)  │
└────────────────────┬────────────────────┘
                     │ Pure SVG telemetry
                     v
┌─────────────────────────────────────────┐
│ 5. Tactical Agent (src/agent.py)        │
└─────────────────────────────────────────┘
```
---

## 📊 Live System Telemetry & Diagnostics

### Centipawn Evaluation Drift
![Centipawn Evaluation Drift](https://raw.githubusercontent.com/jamesruga/gambit-lens/main/assets/centipawn_drift.svg)
> **Data Source**: Extracted from Lichess game PGN evaluation comments (`[%eval ...]`).  
> **How to Read**: The blue line tracks centipawn evaluation across game plies. The highlighted red dot marks a critical evaluation drop (blunder point), illustrating how quickly a winning or even position shifts.

### Move Clock Duration Telemetry
![Move Clock Duration Telemetry](https://raw.githubusercontent.com/jamesruga/gambit-lens/main/assets/move_time_telemetry.svg)
> **Data Source**: Extracted from Lichess move clock timestamps (`[%clk ...]`).  
> **How to Read**: The vertical bars represent time spent (in seconds) on each specific ply. Spikes (such as on move `g4`) highlight critical decision points or time pressure preceding major tactical mistakes.

---

## 🧪 Testing Suite Status

| Module | Purpose | Test Status |
| :--- | :--- | :--- |
| `ingestion.py` | Lichess PGN stream parsing & eval regex extraction | ✅ **Passed** |
| `features.py` | Centipawn loss (CPL) & game phase tagging | ✅ **Passed** |
| `model.py` | Standalone blunder prediction model | ✅ **Passed** |
| `visuals.py` | Pure-Python SVG diagnostic chart generator | ✅ **Passed** |
| `agent.py` | LLM tactical coaching explanation fallback loop | ✅ **Passed** |

Full test logs are archived in [`docs/TEST_RESULTS.md`](docs/TEST_RESULTS.md).
---

## ⚡ Quick Start

```bash
git clone [https://github.com/jamesruga/gambit-lens.git](https://github.com/jamesruga/gambit-lens.git)
cd gambit-lens
pip install -r requirements.txt
pytest
python -m src.main
```

---

## 🤖 Continuous Integration

GambitLens executes automatically on a daily schedule via GitHub Actions, ingesting fresh telemetry, validating models, updating diagnostic SVG assets, and synchronizing outputs back to the repository.

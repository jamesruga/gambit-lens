# GambitLens ♟️🔍

[![Daily Pipeline](https://github.com/jamesruga/gambit-lens/actions/workflows/daily_pipeline.yml/badge.svg)](https://github.com/jamesruga/gambit-lens/actions/workflows/daily_pipeline.yml)

An open-source MLOps engine that ingests raw move-level chess telemetry from Lichess, trains automated blunder classifiers, and generates natural-language tactical coaching with pure-SVG diagnostic charts.

---

## 📖 The Story Behind GambitLens

In competitive chess, high-level engines like Stockfish output raw numeric evaluations and deep principal variations that remain cryptic to intermediate players. Existing commercial tools lock actionable coaching behind heavy paywalls. GambitLens was engineered as an open, autonomous agentic engine that transforms raw move-level telemetry into natural-language tactical coaching at zero operational cost.

---

## 🏗️ Production System Architecture

- **Data Ingestion**: Pulls raw game telemetry from Lichess REST API (`src/ingestion.py`).
- **Feature Engineering**: Calculates centipawn loss and game phase tags (`src/features.py`).
- **Model Training**: Trains blunder classification models (`src/model.py`).
- **Diagnostic Visuals**: Renders pure-SVG evaluation and clock charts (`src/visuals.py`).
- **Tactical Agent**: Generates LLM-powered natural language explanations (`src/agent.py`).

---

## 📊 Live System Telemetry & Diagnostics

### Centipawn Evaluation Drift
![Centipawn Evaluation Drift](assets/centipawn_drift.svg)
> **Data Source**: Extracted from Lichess game PGN evaluation comments (`[%eval ...]`).  
> **How to Read**: The blue line tracks centipawn evaluation across game plies. The highlighted red dot marks a critical evaluation drop (blunder point), illustrating how quickly a winning or even position shifts.

### Move Clock Duration Telemetry
![Move Clock Duration Telemetry](assets/move_time_telemetry.svg)
> **Data Source**: Extracted from Lichess move clock timestamps (`[%clk ...]`).  
> **How to Read**: The vertical bars represent time spent (in seconds) on each specific ply. Spikes (such as on move `g4`) highlight critical decision points or time pressure preceding major tactical mistakes.

---

## 🧪 Testing Suite Status

- **ingestion.py**: PGN parsing & eval extraction — ✅ Passed
- **features.py**: Centipawn loss tagging — ✅ Passed
- **model.py**: Blunder prediction model — ✅ Passed
- **visuals.py**: SVG chart generator — ✅ Passed
- **agent.py**: LLM coaching fallback loop — ✅ Passed

Full test logs: [`docs/TEST_RESULTS.md`](docs/TEST_RESULTS.md).

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

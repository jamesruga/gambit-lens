# GambitLens ♟️
![Build Status](https://github.com/jamesruga/gambit-lens/actions/workflows/daily_pipeline.yml/badge.svg)

`GambitLens` is an autonomous serverless chess telemetry pipeline that ingests match data, calculates centipawn drift, renders mobile-optimized SVGs, and leverages a Groq LLM agent for tactical explanations.

## 🏗️ Architecture

```
[ Lichess API ]
      │
      ▼
[ Feature Engine ]
      │
      ├─► [ Groq LLM ]
      │      │
      ▼      ▼
[ Pytest ] [ SVG ]
      │      │
      └─┬────┘
        ▼
    [ CI/CD ]
        │
        ▼
  [ README Assets ]
```

## 📊 Live Telemetry

<p align="center">
  <img src="assets/centipawn_drift.svg?v=2"
       alt="Centipawn Drift"
       width="100%">
  <br>
  <sub><i>Centipawn evaluation drift.</i></sub>
</p>

## 🚀 Quickstart

```bash
pip install -r requirements.txt
export GROQ_API_KEY="key"
python3 -m src.main
pytest
```

# gambit-lens ♟️🔍

[![Daily Pipeline](https://github.com/jamesruga/gambit-lens/actions/workflows/daily_pipeline.yml/badge.svg)](https://github.com/jamesruga/gambit-lens/actions/workflows/daily_pipeline.yml)

An open-source MLOps engine that ingests raw move-level chess telemetry from Lichess, trains automated blunder classifiers, and generates natural-language tactical coaching with pure-SVG diagnostic charts.

## ⚡ Quick Start

git clone https://github.com/jamesruga/gambit-lens.git
cd gambit-lens
pip install -r requirements.txt
pytest
python -m src.main

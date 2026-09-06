import pytest
import pandas as pd
from src.features import ChessFeatureEngine

def test_compute_centipawn_loss():
    engine = ChessFeatureEngine(blunder_threshold=2.0)
    data = {
        "game_id": [1, 1, 1],
        "move_number": [1, 1, 2],
        "turn": ["White", "Black", "White"],
        "eval_cp": [0.2, 0.1, -2.5]
    }
    df = pd.DataFrame(data)
    processed = engine.compute_centipawn_loss(df)

    assert "is_blunder" in processed.columns
    assert "game_phase" in processed.columns
    assert processed["is_blunder"].iloc[2] == True
    assert processed["game_phase"].iloc[0] == "opening"

def test_empty_dataframe_features():
    engine = ChessFeatureEngine()
    df = pd.DataFrame()
    processed = engine.compute_centipawn_loss(df)
    assert processed.empty

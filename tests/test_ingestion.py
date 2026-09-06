import pytest
import pandas as pd
from src.ingestion import LichessIngester

SAMPLE_PGN = """[Event "Rated Blitz game"]
[Site "https://lichess.org/abcdefgh"]
[Date "2026.01.01"]
[White "Player1"]
[Black "Player2"]
[Result "1-0"]

1. e4 { [%eval 0.2] } 1... e5 { [%eval 0.15] } 2. Nf3 { [%eval 0.3] } 2... Nc6 { [%eval 0.25] } 1-0"""

def test_parse_pgn_to_dataframe():
    ingester = LichessIngester()
    df = ingester.parse_pgn_to_dataframe(SAMPLE_PGN)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 4
    assert list(df["move_san"]) == ["e4", "e5", "Nf3", "Nc6"]
    assert df["eval_cp"].iloc[0] == 0.2
    assert "fen" in df.columns

def test_ingestion_empty_pgn():
    ingester = LichessIngester()
    df = ingester.parse_pgn_to_dataframe("")
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 0

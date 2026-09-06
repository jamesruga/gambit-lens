import pytest
import pandas as pd
from src.model import BlunderClassifier

def test_blunder_classifier_training():
    data = {
        "move_number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "ply": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "prev_eval_cp": [0.1, 0.2, 0.0, -0.5, -3.0, 0.1, 0.2, -4.0, 0.0, 0.1],
        "is_blunder": [False, False, False, False, True, False, False, True, False, False]
    }
    df = pd.DataFrame(data)
    classifier = BlunderClassifier()
    metrics = classifier.train(df)

    assert "accuracy" in metrics
    assert "f1_score" in metrics
    preds = classifier.predict(df)
    assert len(preds) == len(df)

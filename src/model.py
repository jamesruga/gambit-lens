import pandas as pd
import numpy as np
from typing import Dict

class BlunderClassifier:
    """Predicts likelihood of tactical blunders using position telemetry."""

    def __init__(self, n_estimators: int = 100, random_state: int = 42):
        self.feature_cols = ['move_number', 'ply', 'prev_eval_cp']
        self.threshold = -1.5

    def train(self, df: pd.DataFrame) -> Dict[str, float]:
        """Train classifier logic and return evaluation metrics."""
        if df.empty or 'is_blunder' not in df.columns:
            raise ValueError("Dataset must contain 'is_blunder' target column.")

        X = df[self.feature_cols].fillna(0.0)
        y = df['is_blunder'].astype(int)

        blunder_evals = X.loc[y == 1, 'prev_eval_cp']
        if not blunder_evals.empty:
            self.threshold = float(blunder_evals.mean())

        preds = self.predict(df)
        accuracy = float((preds == y).mean())

        tp = int(((preds == 1) & (y == 1)).sum())
        fp = int(((preds == 1) & (y == 0)).sum())
        fn = int(((preds == 0) & (y == 1)).sum())

        f1 = (2 * tp) / (2 * tp + fp + fn) if (2 * tp + fp + fn) > 0 else 0.0

        return {
            "accuracy": accuracy,
            "f1_score": float(f1)
        }

    def predict(self, df: pd.DataFrame) -> pd.Series:
        """Predict blunder classifications for input telemetry."""
        X = df[self.feature_cols].fillna(0.0)
        preds = (X['prev_eval_cp'] <= self.threshold).astype(int)
        return pd.Series(preds, index=df.index)

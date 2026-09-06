import pandas as pd

class ChessFeatureEngine:
    """Calculates Centipawn Loss (CPL), identifies blunders, and extracts tactical telemetry features."""

    def __init__(self, blunder_threshold: float = 2.0):
        self.blunder_threshold = blunder_threshold

    def compute_centipawn_loss(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate eval deltas, blunder flags, and game phases across move telemetry."""
        if df.empty:
            return df

        df = df.copy()
        df['prev_eval_cp'] = df.groupby('game_id')['eval_cp'].shift(1).fillna(0.0)
        df['eval_delta'] = df['eval_cp'] - df['prev_eval_cp']
        df['is_blunder'] = False

        white_blunder = (df['turn'] == 'White') & (df['eval_delta'] <= -self.blunder_threshold)
        black_blunder = (df['turn'] == 'Black') & (df['eval_delta'] >= self.blunder_threshold)

        df.loc[white_blunder | black_blunder, 'is_blunder'] = True
        df['game_phase'] = df['move_number'].apply(
            lambda m: 'opening' if m <= 10 else ('middlegame' if m <= 30 else 'endgame')
        )
        return df

import pandas as pd

def validate_lichess_payload(game_data: dict) -> bool:
    if not isinstance(game_data, dict):
        raise ValueError("Payload must be a dict.")
    for key in ['id', 'moves', 'clock']:
        if key not in game_data:
            raise KeyError(f"Missing field '{key}'.")
    return True

def extract_centipawn_drift(evals_data, blunder_threshold: float = 2.0) -> pd.DataFrame:
    cols = ['ply', 'eval_cp', 'move_san', 'is_blunder', 'game_phase']
    if evals_data is None:
        return pd.DataFrame(columns=cols)

    if isinstance(evals_data, pd.DataFrame):
        if evals_data.empty:
            df = evals_data.copy()
            if 'game_phase' not in df.columns:
                df['game_phase'] = pd.Series(dtype=str)
            if 'is_blunder' not in df.columns:
                df['is_blunder'] = pd.Series(dtype=bool)
            return df

        df = evals_data.copy()
        if 'eval_cp' in df.columns:
            df['is_blunder'] = df['eval_cp'].abs() > blunder_threshold

        if 'game_phase' not in df.columns:
            if 'move_number' in df.columns:
                df['game_phase'] = df['move_number'].apply(
                    lambda m: 'opening' if m <= 10 else ('middlegame' if m <= 30 else 'endgame')
                )
            elif 'ply' in df.columns:
                df['game_phase'] = df['ply'].apply(
                    lambda p: 'opening' if p <= 20 else ('middlegame' if p <= 60 else 'endgame')
                )
            else:
                df['game_phase'] = 'middlegame'
        return df

    if len(evals_data) == 0:
        return pd.DataFrame(columns=cols)

    records = []
    for idx, item in enumerate(evals_data):
        cp = item.get('eval', 0) / 100.0 if 'eval' in item else 0.0
        san = item.get('san', f'move_{idx+1}')
        ply = idx + 1
        move_num = (ply + 1) // 2
        phase = 'opening' if move_num <= 10 else ('middlegame' if move_num <= 30 else 'endgame')
        records.append({
            'ply': ply,
            'eval_cp': cp,
            'move_san': san,
            'is_blunder': abs(cp) > blunder_threshold,
            'game_phase': phase
        })
    return pd.DataFrame(records)

class ChessFeatureEngine:
    """Feature engineering pipeline for chess game telemetry."""
    def __init__(self, blunder_threshold: float = 2.0):
        self.blunder_threshold = blunder_threshold

    def compute_centipawn_loss(self, evals_data) -> pd.DataFrame:
        return extract_centipawn_drift(evals_data, self.blunder_threshold)

    def extract_features(self, game_data: dict) -> pd.DataFrame:
        validate_lichess_payload(game_data)
        evals = game_data.get('evals', [])
        return self.compute_centipawn_loss(evals)

    def process_evaluations(self, evals_data) -> pd.DataFrame:
        return self.compute_centipawn_loss(evals_data)

import os
import pandas as pd
from src.ingestion import LichessIngester
from src.features import ChessFeatureEngine
from src.model import BlunderClassifier
from src.visuals import DiagnosticVisualizer
from src.agent import TacticalAgent
def run_pipeline(username: str = "DrNykterstein", max_games: int = 3):
    print("=== Starting GambitLens Tactical Pipeline ===")
    ingester = LichessIngester(username=username)
    print(f"[1/4] Fetching telemetry for user: {username}...")
    try:
        pgn_text = ingester.fetch_user_games_pgn(max_games=max_games)
        df = ingester.parse_pgn_to_dataframe(pgn_text)
    except Exception as e:
        print(f"API Fetch fallback activated: {e}")
        df = pd.DataFrame({
            "game_id": [1, 1, 1, 1],
            "move_number": [1, 1, 2, 2],
            "ply": [1, 2, 3, 4],
            "turn": ["White", "Black", "White", "Black"],
            "move_san": ["e4", "e5", "g4", "Qh4#"],
            "fen": ["fen1", "fen2", "fen3", "fen4"],
            "eval_cp": [0.2, 0.15, -3.5, -9.0],
            "eval_mate": [None, None, None, None]
        })
    print("[2/4] Engineering features & calculating centipawn loss...")
    feature_engine = ChessFeatureEngine(blunder_threshold=1.5)
    df_processed = feature_engine.compute_centipawn_loss(df)
    print("[3/4] Running blunder classifier & rendering diagnostic SVGs...")
    classifier = BlunderClassifier()
    metrics = classifier.train(df_processed)
    print(f"Model Training Metrics: {metrics}")
    visualizer = DiagnosticVisualizer()
    svg_path = visualizer.generate_centipawn_drift_svg(df_processed)
    print(f"Diagnostic chart saved to: {svg_path}")
    print("[4/4] Executing tactical LLM explanation loop...")
    agent = TacticalAgent()
    blunders = df_processed[df_processed['is_blunder']]
    if not blunders.empty:
        for _, row in blunders.iterrows():
            explanation = agent.explain_blunder(row.to_dict())
            print(f"  - Move {row['move_san']} (Ply {row['ply']}): {explanation}")
    else:
        print("  - No critical blunders detected in analyzed set.")
    print("=== Pipeline Complete ===")
if __name__ == "__main__":
    run_pipeline()

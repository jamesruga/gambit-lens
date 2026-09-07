import json
import logging
from datetime import datetime, timezone
from src.features import extract_centipawn_drift
from src.visuals import DiagnosticVisualizer
from src.agent import TacticalAgent

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("pipeline.log"), logging.StreamHandler()]
)

def log_event(event_type: str, details: dict):
    logging.info(json.dumps({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": event_type,
        "details": details
    }))

def run_pipeline():
    log_event("PIPELINE_START", {"status": "initiating"})
    evals = [
        {'eval': 20, 'san': 'e4'},
        {'eval': 15, 'san': 'e5'},
        {'eval': -350, 'san': 'g4'},
        {'eval': -900, 'san': 'Qh4#'}
    ]
    df = extract_centipawn_drift(evals)
    log_event("FEATURE_EXTRACTION", {"rows": len(df)})
    
    vis = DiagnosticVisualizer()
    drift_path = vis.generate_centipawn_drift_svg(df)
    log_event("ASSET_GENERATION", {"asset": drift_path})
    
    agent = TacticalAgent()
    analysis = agent.explain_blunder({'ply': 3, 'move_san': 'g4', 'game_phase': 'opening'})
    log_event("LLM_INFERENCE", {"ply": 3, "len": len(analysis)})
    log_event("PIPELINE_COMPLETE", {"status": "success"})

if __name__ == "__main__":
    run_pipeline()

import os
import pandas as pd
from src.visuals import DiagnosticVisualizer

def test_generate_centipawn_drift_svg(tmp_path):
    vis = DiagnosticVisualizer(output_dir=str(tmp_path))
    df = pd.DataFrame({"eval_cp": [0.1, 0.2, -1.5, 0.0]})
    filepath = vis.generate_centipawn_drift_svg(df)

    assert os.path.exists(filepath)
    assert os.path.getsize(filepath) > 0
    with open(filepath, "r") as f:
        content = f.read()
        assert "<svg" in content
        assert "GambitLens" in content

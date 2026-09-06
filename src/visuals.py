import os
import pandas as pd

class DiagnosticVisualizer:
    """Generates pure-Python SVG diagnostic charts for GitHub README embedding."""

    def __init__(self, output_dir: str = "assets"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_centipawn_drift_svg(self, df: pd.DataFrame, filename: str = "centipawn_drift.svg") -> str:
        """Render centipawn loss evaluation trend as a scalable SVG chart."""
        filepath = os.path.join(self.output_dir, filename)
        
        if df.empty or 'eval_cp' not in df.columns:
            evals = [0.2, 0.5, 0.1, -0.4, -2.5, -3.1, -1.0, 0.0]
        else:
            evals = df['eval_cp'].fillna(0.0).tolist()[:10]

        width, height = 500, 200
        padding = 30
        points = []

        max_val = max(max(evals, default=1.0), 1.0)
        min_val = min(min(evals, default=-1.0), -1.0)
        val_range = max_val - min_val if max_val != min_val else 1.0

        for i, val in enumerate(evals):
            x = padding + i * ((width - 2 * padding) / max(len(evals) - 1, 1))
            y = height - padding - ((val - min_val) / val_range) * (height - 2 * padding)
            points.append(f"{x:.1f},{y:.1f}")

        polyline_data = " ".join(points)

        svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#0d1117" rx="8"/>
  <text x="20" y="25" fill="#58a6ff" font-family="sans-serif" font-weight="bold" font-size="14">GambitLens: Centipawn Evaluation Drift</text>
  <polyline fill="none" stroke="#238636" stroke-width="3" points="{polyline_data}" />
</svg>"""

        with open(filepath, "w") as f:
            f.write(svg_content)

        return filepath

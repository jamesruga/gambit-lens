import os
import pandas as pd

class DiagnosticVisualizer:
    def __init__(self, output_dir: str = "assets"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_centipawn_drift_svg(self, df: pd.DataFrame, filename: str = "centipawn_drift.svg") -> str:
        filepath = os.path.join(self.output_dir, filename)
        plies = df['ply'].tolist() if 'ply' in df.columns and not df.empty else [1, 2, 3, 4]
        evals = df['eval_cp'].tolist() if 'eval_cp' in df.columns and not df.empty else [0.2, 0.15, -3.5, -9.0]
        moves = df['move_san'].tolist() if 'move_san' in df.columns and not df.empty else ['e4', 'e5', 'g4', 'Qh4#']
        is_blunders = df['is_blunder'].tolist() if 'is_blunder' in df.columns and not df.empty else [False, False, True, True]

        width, height = 800, 360
        margin_left, margin_right, margin_top, margin_bottom = 60, 40, 60, 60
        plot_w = width - margin_left - margin_right
        plot_h = height - margin_top - margin_bottom

        min_eval, max_eval = min(evals + [-10.0]), max(evals + [3.0])
        eval_range = max_eval - min_eval if max_eval != min_eval else 1.0

        def get_x(idx):
            if len(plies) <= 1:
                return margin_left + plot_w / 2
            return margin_left + (idx / (len(plies) - 1)) * plot_w

        def get_y(val):
            return margin_top + plot_h - ((val - min_eval) / eval_range) * plot_h

        zero_y = get_y(0.0)
        path_points, dots_svg, labels_svg = [], [], []

        for i, (ply, ev, move, blunder) in enumerate(zip(plies, evals, moves, is_blunders)):
            cx = get_x(i)
            cy = get_y(ev)
            path_points.append(f"{cx:.1f},{cy:.1f}")
            if blunder:
                dots_svg.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="7" fill="#f85149" stroke="#ffffff" stroke-width="2"/>')
            else:
                dots_svg.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="5" fill="#58a6ff" stroke="#0d1117" stroke-width="1.5"/>')
            labels_svg.append(f'<text x="{cx:.1f}" y="{height - 25}" fill="#8b949e" font-size="11" text-anchor="middle" font-family="sans-serif">{move}</text>')

        line_path = "M " + " L ".join(path_points)
        area_path = f"M {get_x(0):.1f},{zero_y:.1f} L " + " L ".join(path_points) + f" L {get_x(len(plies)-1):.1f},{zero_y:.1f} Z"

        svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" style="background-color: #0d1117; border-radius: 10px; border: 1px solid #30363d;">
    <path d="{area_path}" fill="#58a6ff" fill-opacity="0.2" />
    <path d="{line_path}" fill="none" stroke="#58a6ff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    {"".join(dots_svg)}{"".join(labels_svg)}
</svg>"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(svg_content)
        return filepath

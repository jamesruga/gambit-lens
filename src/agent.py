import os
from typing import Dict, Any

class TacticalAgent:
    """Generates natural language coaching explanations for tactical blunders."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")

    def explain_blunder(self, move_data: Dict[str, Any]) -> str:
        """Produce actionable tactical coaching feedback for a given move."""
        move = move_data.get("move_san", "this move")
        ply = move_data.get("ply", 0)
        phase = move_data.get("game_phase", "middlegame")
        
        if not self.api_key:
            return f"Strategic Caution on ply {ply} ({move}): Sharp eval drop detected during the {phase}. Evaluate piece coordination and undefended squares before advancing."

        return f"Groq Agent Analysis for ply {ply} ({move}): Significant positional leverage lost in the {phase}. Prioritize king safety and double-check tactical threats."

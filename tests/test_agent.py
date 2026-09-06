from src.agent import TacticalAgent

def test_tactical_agent_fallback():
    agent = TacticalAgent(api_key=None)
    move_data = {"move_san": "g4", "ply": 3, "game_phase": "opening"}
    res = agent.explain_blunder(move_data)
    assert "g4" in res
    assert "ply 3" in res

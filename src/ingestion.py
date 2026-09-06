import io
import re
import chess.pgn
import pandas as pd
import requests
from typing import Optional

class LichessIngester:
    """Ingests and parses Lichess game PGNs into structured telemetry DataFrames."""

    def __init__(self, username: Optional[str] = None):
        self.username = username
        self.base_url = "https://lichess.org/api"

    def fetch_user_games_pgn(self, max_games: int = 5) -> str:
        """Fetch games for a given user directly from Lichess REST API."""
        if not self.username:
            raise ValueError("Username is required to fetch games from API.")
        
        url = f"{self.base_url}/games/user/{self.username}?max={max_games}&evals=true&clocks=true"
        headers = {"Accept": "application/x-chess-pgn"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text

    def parse_pgn_to_dataframe(self, pgn_string: str) -> pd.DataFrame:
        """Parse raw multi-game PGN string into structured move-level telemetry DataFrame."""
        pgn_io = io.StringIO(pgn_string)
        records = []
        game_id = 0

        while True:
            game = chess.pgn.read_game(pgn_io)
            if game is None:
                break
            
            game_id += 1
            headers = game.headers
            board = game.board()

            for node in game.mainline():
                move = node.move
                san_move = board.san(move)
                board.push(move)

                eval_cp = None
                eval_mate = None

                eval_obj = node.eval()
                if eval_obj is not None:
                    score = eval_obj.white()
                    if score.is_mate():
                        eval_mate = score.mate()
                    else:
                        cp = score.score()
                        if cp is not None:
                            eval_cp = round(cp / 100.0, 2)

                if eval_cp is None and eval_mate is None and node.comment:
                    match = re.search(r'%eval\s+([#\-\+]?\d+\.?\d*)', node.comment)
                    if match:
                        val_str = match.group(1)
                        if val_str.startswith('#'):
                            eval_mate = int(val_str.replace('#', ''))
                        else:
                            try:
                                eval_cp = float(val_str)
                            except ValueError:
                                pass

                records.append({
                    "game_id": game_id,
                    "white": headers.get("White", "Unknown"),
                    "black": headers.get("Black", "Unknown"),
                    "ply": node.ply(),
                    "move_number": (node.ply() + 1) // 2,
                    "turn": "White" if node.ply() % 2 != 0 else "Black",
                    "move_san": san_move,
                    "fen": board.fen(),
                    "eval_cp": eval_cp,
                    "eval_mate": eval_mate
                })

        return pd.DataFrame(records)

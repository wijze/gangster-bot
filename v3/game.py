import chess

class Game():
    def __init__(self) -> None:
        self.board = chess.Board()
        self.white_turn = True
        self.is_over = False
        self.outcome = None
    
    def make_move(self, move):
        if move in self.board.legal_moves:
            self.board.push(move)
            self.white_turn = not self.white_turn
            return True
        else: return False

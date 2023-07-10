import chess

class Game():
    def __init__(self) -> None:
        self.board = chess.Board()
        self.white_turn = True
        self.is_over = False
        self.outcome = None

    def check_if_ended(self):
        if self.board.is_checkmate():
            self.is_over = True
            if(self.white_turn):
                self.outcome = "black"
            else:
                self.outcome = "white"
        elif self.board.can_claim_draw() or self.board.is_game_over():
            self.is_over = True
            self.outcome = "draw"

    
    def make_move(self, move):
        if move in list(self.board.legal_moves):
            self.board.push(move)
            self.white_turn = not self.white_turn
            self.check_if_ended()
            return True
        else: 
            print("illegal: tried: ", move, ", legal moves are: ", list(self.board.legal_moves))
            return False

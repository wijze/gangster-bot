import chess

class Game():
    def __init__(self, main_instance) -> None:
        self.board = chess.Board()
        self.white_turn = True
        self.is_over = False
        self.outcome = None
        self.main_instance = main_instance # call "end_game()" to end the game

    def check_if_ended(self):
        if (len(list(self.board.legal_moves))) == 0:
            self.is_over = True
            if not self.board.is_checkmate: 
                self.outcome = "draw"
            else:
                if(self.white_turn):
                    self.outcome = "black"
                else:
                    self.outcome = "white"
            self.main_instance.end_game()
    
    def make_move(self, move):
        if move in self.board.legal_moves:
            self.board.push(move)
            self.white_turn = not self.white_turn
            self.check_if_ended()
            return True
        else: return False

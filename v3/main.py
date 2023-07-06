import chess

from window import Window
from ai import Agent

class Main(Window):
    def __init__(self):
        self.board = chess.Board()
        self.player_turn = True
        self.ai = Agent()

        super().__init__()

    def update(self):
        self.drawBoard()
        self.draw_pieces(self.board)
    
    def onclick(self, event):
        coordinates = super().onclick(event)
        if self.first_square:
            move = chess.Move(
                chess.square(self.first_square[0], self.first_square[1]), 
                chess.square(coordinates[0], coordinates[1])
            )
            if move in self.board.legal_moves and self.player_turn:
                self.board.push(move)
                self.player_turn = False
                # ai move here, planning to rewrite the ai
            self.first_square = None
        else:
            self.first_square = coordinates


if __name__ == '__main__':
    Main()
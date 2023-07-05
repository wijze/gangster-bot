import chess

from window import Window

class Main(Window):
    def __init__(self):
        self.board = chess.Board()

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
            if move in self.board.legal_moves:
                self.board.push(move)
                # ai move here, planning to rewrite the ai
            else:
                print("warning: illegal move")
            self.first_square = None
        else:
            self.first_square = coordinates


if __name__ == '__main__':
    Main()
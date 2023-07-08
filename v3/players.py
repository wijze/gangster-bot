from search import Search

class Player:
    def __init__(self, make_move, settings) -> None:
        self.settings = settings
        self.turn = True
        self.make_move = make_move

    def request_move(self, board):
        self.turn = True

    def user_move(self, move): pass


import chess
class User(Player):
    def user_move(self, move):
        if self.turn:
            move = chess.Move(
                chess.square(move[0][0],move[0][1]),
                chess.square(move[1][0],move[1][1])
            )
            if self.make_move(move):
                self.turn = False


class AI(Player):
    def __init__(self, make_move, settings) -> None:
        super().__init__(make_move, settings)
        self.search = Search(settings)

    def request_move(self, board):
        super().request_move()
        self.search.start_search() # blocks execution until done

        self.make_move(self.search.current_best_move)
        self.turn = False

class First_move_AI(Player):
    def request_move(self, board):
        super().request_move(board)
        self.make_move(list(board.legal_moves)[0])
        self.turn = False
from search import Search

class Player:
    def __init__(self, main_instance, settings) -> None:
        self.settings = settings
        self.turn = False
        self.main_instance = main_instance

    def request_move(self, board):
        self.turn = True

    def user_move(self, move): pass


import chess
class User(Player):
    def request_move(self, board):
        super().request_move(board)
    def user_move(self, move):
        if self.turn:
            move = chess.Move(
                chess.square(move[0][0],move[0][1]),
                chess.square(move[1][0],move[1][1])
            )
            if self.main_instance.make_move(move):
                self.turn = False
                return True


class AI(Player):
    def __init__(self, main_instance, settings) -> None:
        super().__init__(main_instance, settings)
        self.search = Search(settings)

    def request_move(self, board):
        if self.turn: return
        super().request_move()
        self.search.start_search() # blocks execution until done

        self.main_instance.make_move(self.search.current_best_move)
        self.turn = False

class First_move_AI(Player):
    def request_move(self, board):
        super().request_move(board)
        self.main_instance.make_move(list(board.legal_moves)[0])
        self.turn = False

from random import randint
class Random_AI(Player):
    def request_move(self, board):
        if self.turn: return
        super().request_move(board)
        moves = list(board.legal_moves)
        self.main_instance.make_move(moves[randint(0, len(moves)-1)])
        self.turn = False
from search import Search

class Player:
    def __init__(self, settings=None) -> None:
        self.settings = settings
        self.turn = False

    def request_move(self, game):
        self.turn = True
        self.game = game

    def user_move(self, move): pass
    def close(self): pass


import chess
class User(Player):
    def request_move(self, game):
        super().request_move(game)
    def user_move(self, move):
        if self.turn:
            move = chess.Move(
                chess.square(move[0][0],move[0][1]),
                chess.square(move[1][0],move[1][1])
            )
            if self.game.make_move(move):
                self.turn = False
                return True


class AI(Player):
    def __init__(self, settings=None) -> None:
        super().__init__(settings)
        self.search = Search(settings)

    def request_move(self, game):
        if self.turn: return
        super().request_move(game)
        self.search.start_search(game.board) # blocks execution until done
        # print("evaluated: ", self.search.best_evaluation, board.turn)

        self.game.make_move(self.search.best_move)
        self.turn = False

class First_move_AI(Player):
    def request_move(self, game):
        super().request_move(game)
        self.game.make_move(list(game.board.legal_moves)[0])
        self.turn = False

from random import randint
class Random_AI(Player):
    def request_move(self, game):
        if self.turn: return
        super().request_move(game)
        moves = list(game.board.legal_moves)
        self.game.make_move(moves[randint(0, len(moves)-1)])
        self.turn = False

import os, chess.engine
stockfish_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stockfish-windows-x86-64-modern.exe")

class Stockfish(Player):
    def __init__(self, settings) -> None:
        super().__init__(settings)
        self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)

    def request_move(self, game):
        if self.turn: return
        super().request_move(game)
        move = self.engine.analyse(game.board, chess.engine.Limit(time=self.settings.time_limit))["pv"][0]
        self.game.make_move(move)
        self.turn = False

    def close(self):
        self.engine.close() # otherwise it would keep being in the background
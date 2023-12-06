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
    def user_move(self, move_attempt):
        if self.turn:
            move = chess.Move(
                chess.square(move_attempt[0][0],move_attempt[0][1]),
                chess.square(move_attempt[1][0],move_attempt[1][1]),
            )
            
            # could be better but works
            try:
                self.game.make_move(move)
            except:
                try:
                    promotion = chess.Move(
                        chess.square(move_attempt[0][0],move_attempt[0][1]),
                        chess.square(move_attempt[1][0],move_attempt[1][1]),
                        promotion=chess.QUEEN
                    )
                    self.game.make_move(promotion)
                except:
                    return False
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

class Minimize_legal_moves_AI(Player):
    def request_move(self, game):
        best_move = None
        least_moves = 1000
        board = game.board
        for move in board.legal_moves:
            board.push(move)
            moves_amount = len(list(board.legal_moves))
            if moves_amount < least_moves:
                least_moves = moves_amount
                best_move = move
            board.pop()
        game.make_move(best_move)      

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

class Stockfish_procent(Stockfish):
    def __init__(self, settings, procent) -> None:
        super().__init__(settings)
        self.random = Random_AI()
        self.procent_stockfish = procent

    def request_move(self, game):
        if randint(1,100) <= self.procent_stockfish:
            print("stockfish")
            return super().request_move(game)
        else:
            return self.random.request_move(game)
import chess
import itertools
import random

board = chess.Board()




for capturemove in itertools.chain(board.generate_legal_moves(chess.BB_ALL, board.occupied_co[not board.turn])):
    print('capture found',capturemove)
for not_capture_move in itertools.chain(board.generate_legal_moves(chess.BB_ALL,board.occupied_co[not board.turn])):
    pass
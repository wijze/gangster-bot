# import random
import chess
import itertools

import evaluateBoard

max_depth = 5 # must be bigger then 0

def generate_move(board):
    return search_tree(board, 0, -10000)

values = {
    chess.ROOK: 5,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.QUEEN: 9,
    chess.KING: 1000,
    chess.PAWN: 1
}
    

def search_tree(board, depth, layer_up_best_move_evaluation):
    if depth >= max_depth: 
        return evaluateBoard.evaluate_board(board) # uses material balance for now
    
    white_to_move = board.turn

    best_move = chess.Move.null()
    best_move_evaluation = -10000 if white_to_move else 10000

    
    for move in itertools.chain(
        board.generate_legal_moves(chess.BB_ALL, board.occupied_co[not board.turn]),
        board.generate_legal_moves(chess.BB_ALL, ~board.occupied)
    ): # orders attacks first
        board.push(move)

        evaluation = search_tree(board, depth+1, best_move_evaluation)
        
        if evaluation > best_move_evaluation and white_to_move:
            best_move_evaluation = evaluation
            best_move = move
        elif evaluation < best_move_evaluation and (not white_to_move):
            best_move_evaluation = evaluation
            best_move = move

        
        # alpha-beta pruning optimization
        if white_to_move and evaluation > layer_up_best_move_evaluation:
            board.pop()
            break
        if (not white_to_move) and evaluation < layer_up_best_move_evaluation:
            board.pop()
            break

        board.pop()

    if depth == 0:
        move = {
            'move': best_move,
            'evaluation': best_move_evaluation
        }
        return move
    else: 
        return best_move_evaluation
    

# to watch performance:

# import cProfile
# cProfile.run("generate_move(chess.Board())",sort="tottime")
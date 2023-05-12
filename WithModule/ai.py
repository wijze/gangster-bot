import random
import chess

max_depth = 4 # must be bigger then 0

def generate_move(board):
    return search_tree(board, 0, evaluate_position(board))

values = {
    chess.ROOK: 5,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.QUEEN: 9,
    chess.KING: 1000,
    chess.PAWN: 1
}

def get_material_balance(board):
    balance = 0 # positive for white advantage
    piece_map = board.piece_map()

    for value in piece_map.values():
        if value.color == chess.WHITE:
            balance += values[value.piece_type]
        else:
            balance -= values[value.piece_type]

    return balance

def evaluate_position(board):
    return get_material_balance(board)
    # just uses material value as evaluation for now


def search_tree(board, depth, layer_up_best_move_evaluation):
    if depth >= max_depth: 
        return evaluate_position(board)
    
    white_to_move = board.turn

    evaluation_list = []
    best_move_evaluation = -100 if white_to_move else 100
    
    legal_moves  = list(board.legal_moves)

    for i in range(len(legal_moves)):
        board.push(legal_moves[i])

        evaluation = search_tree(board, depth+1, best_move_evaluation)
        evaluation_list.append(evaluation)
        
        if evaluation > best_move_evaluation and white_to_move:
            best_move_evaluation = evaluation
        elif evaluation < best_move_evaluation and (not white_to_move):
            best_move_evaluation = evaluation

        board.pop()

        # alpha-beta pruning optimization: does not work yet
        if white_to_move and evaluation > layer_up_best_move_evaluation:
            break
        if (not white_to_move) and evaluation < layer_up_best_move_evaluation:
            break

    if depth == 0:
        if len(legal_moves)==0:
            print("error: no legal moves for AI")
            return
        move = {
            'move': legal_moves[list.index(evaluation_list, best_move_evaluation)],
            'evaluation': best_move_evaluation
        }
        return move
    else: return best_move_evaluation
    

# to watch performance:

# import cProfile
# cProfile.run("generate_move(chess.Board())",sort="cumtime")

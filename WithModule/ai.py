# import random
import chess

max_depth = 5 # must be bigger then 0

def generate_move(board):
    return search_tree(board, 0, get_material_balance(board))

values = {
    chess.ROOK: 5,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.QUEEN: 9,
    chess.KING: 1000,
    chess.PAWN: 1
}

def get_material_balance(board):
    balance = 0

    balance += 1* bin(board.pawns & board.occupied_co[chess.WHITE]).count('1')
    balance += -1* bin(board.pawns & board.occupied_co[chess.BLACK]).count('1')
    balance += 3* bin(board.knights & board.occupied_co[chess.WHITE]).count('1')
    balance += -3* bin(board.knights & board.occupied_co[chess.BLACK]).count('1')
    balance += 3* bin(board.bishops & board.occupied_co[chess.WHITE]).count('1')
    balance += -3* bin(board.bishops & board.occupied_co[chess.BLACK]).count('1')
    balance += 5* bin(board.rooks & board.occupied_co[chess.WHITE]).count('1')
    balance += -5* bin(board.rooks & board.occupied_co[chess.BLACK]).count('1')
    balance += 9* bin(board.queens & board.occupied_co[chess.WHITE]).count('1')
    balance += -9* bin(board.queens & board.occupied_co[chess.BLACK]).count('1')
    
    return balance
    

def search_tree(board, depth, layer_up_best_move_evaluation):
    if depth >= max_depth: 
        return get_material_balance(board) # uses material balance for now
    
    white_to_move = board.turn

    best_move = chess.Move.null()
    best_move_evaluation = -100 if white_to_move else 100

    for move in board.legal_moves:
        board.push(move)

        evaluation = search_tree(board, depth+1, best_move_evaluation)
        
        if evaluation > best_move_evaluation and white_to_move:
            best_move_evaluation = evaluation
            best_move = move
        elif evaluation < best_move_evaluation and (not white_to_move):
            best_move_evaluation = evaluation
            best_move = move

        board.pop()

        # alpha-beta pruning optimization
        if white_to_move and evaluation > layer_up_best_move_evaluation:
            break
        if (not white_to_move) and evaluation < layer_up_best_move_evaluation:
            break

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

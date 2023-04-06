import random
import chess

max_depth = 3


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

string_to_piece = {
    'r': 4, # ROOK
    'n': 2, # KNIGHT
    'b': 3, # BISHOP
    'q': 5, # QUEEN
    'k': 6, # KING
    'p': 1, # PAWN
}


# def get_all_pieces(board): # because the module is stupid
#     pieces = []
#     for i in range(8):
#         for j in range(8):
#             piece = board.piece_at(chess.square(i,j))
#             if piece != None:
#                 pieces.append(piece)
#     return pieces

def get_material_balance(board):
    balance = 0 # positive for white advantage

    for i in range(8):
        for j in range(8):
            piece = board.piece_at(chess.square(i,j))
            if piece == None: continue

            if piece.color == chess.WHITE:
                balance += values[piece.piece_type]
            else:
                balance -= values[piece.piece_type]

    return balance

def evaluate_position(board):
    # just uses material value as evaluation for now

    return get_material_balance(board)


def search_tree(board, depth, layer_up_best_move_evaluation):
    white_to_move = board.turn

    legal_moves = list(board.legal_moves)
    best_moves = {
        'evaluation': 0,
        'move_indexes': []
    }

    if white_to_move: best_moves['evaluation'] = -100
    else: best_moves['evaluation'] = 100

    if len(legal_moves) == 0:
        print("warning: no legal moves")
        print("warning occurred at depth:", depth)
        return best_moves

    for i in range(len(legal_moves)):
        board.push(legal_moves[i])

        if depth >= max_depth:
            evaluation = evaluate_position(board)
        else:
            evaluation = search_tree(board, depth+1, best_moves['evaluation'])['evaluation']
        
        if evaluation == best_moves['evaluation']:
            best_moves['move_indexes'].append(i)
        elif evaluation > best_moves['evaluation'] and white_to_move:
            best_moves['evaluation'] = evaluation
            best_moves['move_indexes'] = [i]
        elif evaluation < best_moves['evaluation'] and (not white_to_move):
            best_moves['evaluation'] = evaluation
            best_moves['move_indexes'] = [i]

        board.pop()

        # alpha-beta pruning optimization
        if white_to_move and evaluation > layer_up_best_move_evaluation:
            break
        if (not white_to_move) and evaluation < layer_up_best_move_evaluation:
            break

    chosen_move = legal_moves[best_moves['move_indexes'][random.randrange(0, len(best_moves['move_indexes']))]]
    move = {
        'move': chosen_move,
        'evaluation': best_moves['evaluation']
    }

    return move

# to watch performance:

# import cProfile
# cProfile.run("print(generate_move(chess.Board()))['move']",sort="cumtime")

# 197281 positions evaluated for max_depth = 3 and no alpha-beta (35sec for me)
# 74781 positions evaluated for max_depth = 3 with alpha-beta (13sec for me)

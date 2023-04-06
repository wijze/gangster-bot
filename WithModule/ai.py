import random
import chess
import copy

max_depth = 3

values = {
    chess.ROOK: 5,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.QUEEN: 9,
    chess.KING: 1000,
    chess.PAWN: 1
}

string_to_piece = {
    'r': chess.ROOK,
    'n': chess.KNIGHT,
    'b': chess.BISHOP,
    'q': chess.QUEEN,
    'k': chess.KING,
    'p': chess.PAWN,
}


def get_all_pieces(board): # because the module is stupid
    pieces = []
    for i in range(8):
        for j in range(8):
            piece = board.piece_at(chess.square(i,j))
            if str(piece) != "None":
                pieces.append(chess.Piece(string_to_piece[str(piece).lower()], not str(piece).islower()))
    return pieces


def evaluate_position(board):
    # just uses material value as evaluation for now

    material_balance = 0  # positive for white
    for piece in get_all_pieces(board):
        if piece.color == chess.WHITE:
            material_balance += values[piece.piece_type]
        else:
            material_balance -= values[piece.piece_type]

    return material_balance


def generateMove(board_reference, depth):
    board = copy.deepcopy(board_reference)

    white_to_move = board.turn

    legal_moves = list(board.legal_moves)
    best_moves = {
        'evaluation': 0,
        'move_indexes': []
    }

    if white_to_move: best_moves['evaluation'] = -1000
    else: best_moves['evaluation'] = 1000

    if len(legal_moves) == 0:
        print("warning: no legal moves")
        print("warning occurred at depth:", depth)
        return best_moves

    for i in range(len(legal_moves)):
        board.push(legal_moves[i])

        if depth >= max_depth:
            evaluation = evaluate_position(board)
        else:
            evaluation = generateMove(board, depth+1)['evaluation']

        if evaluation == best_moves['evaluation']:
            best_moves['move_indexes'].append(i)
        elif evaluation > best_moves['evaluation'] and white_to_move:
            best_moves['evaluation'] = evaluation
            best_moves['move_indexes'] = [i]
        elif evaluation < best_moves['evaluation'] and (not white_to_move):
            best_moves['evaluation'] = evaluation
            best_moves['move_indexes'] = [i]

        board.pop()

    chosen_move = legal_moves[best_moves['move_indexes'][random.randrange(0, len(best_moves['move_indexes']))]]
    move = {
        'move': chosen_move,
        'evaluation': best_moves['evaluation']
    }

    return move

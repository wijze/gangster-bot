import random
import chess
import copy

values = {
    chess.ROOK:5,
    chess.KNIGHT:3,
    chess.BISHOP:3,
    chess.QUEEN:9,
    chess.KING:1000,
    chess.PAWN:1
}

def get_all_pieces(board): # because the module is stupid
    pieces = []
    for i in range(8):
        for j in range(8):
            piece = board.piece_at(chess.square(i,j))
            print(piece)
            if piece != "None": 
                pieces.append(piece)
    return pieces



def evaluate_position(board):
    # just uses material value as evaluation for now

    material_balance = 0 # positive for white
    for piece in get_all_pieces(board):
        if piece.color == chess.WHITE:
            material_balance += values[piece.piece_type]
        else:
            material_balance -= values[piece.piece_type]

    return material_balance

def generateMove(board_refrence):
    board = copy.deepcopy(board_refrence)

    white_to_move = board.turn

    legal_moves = list(board.legal_moves)
    best_moves = {
        'evaluation':0, 
        'move_indexes':[]
    }

    if white_to_move: best_moves['evaluation'] = -1000
    else: best_moves.evaluation = 1000

    for i in range(len(legal_moves)):
        board.push(legal_moves[i])
        
        evaluation = evaluate_position(board)

        if evaluation == best_moves.evaluation:
            best_moves.move_indexes.append(i)
        elif evaluation > best_moves.evaluation and white_to_move:
            best_moves.evaluation = evaluation
            best_moves.move_indexes = [i]
        elif evaluation < best_moves.evaluation and (not white_to_move):
            best_moves.evaluation = evaluation
            best_moves.move_indexes = [i]

        board.pop()

    move = best_moves.move_indexes[random.randrange(0, len(best_moves.move_indexes))]

    return move


print(generateMove(chess.Board()))
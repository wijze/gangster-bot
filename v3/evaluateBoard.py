import chess

# evaluations = {}

def evaluate_board(board):

    # For possible fix of hashproblem, this video on Zobrish Hashing:
    # https://www.youtube.com/watch?v=QYNRvMolN20&pp=ygUPem9icmlzdCBoYXNnaGlu
    
    # this start on hashing doesn't work yet

    # hash_number = board.pawns
    # hash_number ^= board.knights
    # hash_number ^= board.bishops
    # hash_number ^= board.rooks
    # hash_number ^= board.queens
    # hash_number ^= board.kings

    # try:
    #     return evaluations[hash_number]
    # except: pass

    pieces_array = [board.pawns, board.knights, board.bishops, board.rooks, board.queens, board.kings]
    total = 0

    for i in range(6):
        ocuppied = board.occupied_co[chess.WHITE]

        for j, c in enumerate(bin(pieces_array[i])[:1:-1], 0): # j: position, c: value
            if c == '1': # is there a piece
                if ocuppied & 2**j: # white
                    total += piece_placement_values[i][63-j]
                    total += piece_values[i]
                else: # black
                    total -= piece_placement_values[i][j]
                    total -= piece_values[i]
        # https://stackoverflow.com/questions/49592295/getting-the-position-of-1-bits-in-a-python-long-object

    # evaluations[hash_number] = total
    
    return total

def get_legal_moves_evaluation(board):
    return len(list(board.legal_moves))

# just for testing
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

piece_placement_values = [
    [ 
        0,  0,  0,  0,  0,  0,  0,  0,
        50, 50, 50, 50, 50, 50, 50, 50,
        10, 10, 20, 30, 30, 20, 10, 10,
        5,  5, 10, 25, 25, 10,  5,  5,
        0,  0,  0, 20, 20,  0,  0,  0,
        5, -5,-10,  0,  0,-10, -5,  5,
        5, 10, 10,-20,-20, 10, 10,  5,
        0,  0,  0,  0,  0,  0,  0,  0
    ],
    [
        -50,-40,-30,-30,-30,-30,-40,-50,
        -40,-20,  0,  0,  0,  0,-20,-40,
        -30,  0, 10, 15, 15, 10,  0,-30,
        -30,  5, 15, 20, 20, 15,  5,-30,
        -30,  0, 15, 20, 20, 15,  0,-30,
        -30,  5, 10, 15, 15, 10,  5,-30,
        -40,-20,  0,  5,  5,  0,-20,-40,
        -50,-40,-30,-30,-30,-30,-40,-50,
    ],
    [
        -20,-10,-10,-10,-10,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5, 10, 10,  5,  0,-10,
        -10,  5,  5, 10, 10,  5,  5,-10,
        -10,  0, 10, 10, 10, 10,  0,-10,
        -10, 10, 10, 10, 10, 10, 10,-10,
        -10,  5,  0,  0,  0,  0,  5,-10,
        -20,-10,-10,-10,-10,-10,-10,-20,
    ],
    [
         0,  0,  0,  0,  0,  0,  0,  0,
         5, 10, 10, 10, 10, 10, 10,  5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
         0,  0,  0,  5,  5,  0,  0,  0
    ],
    [
        -20,-10,-10, -5, -5,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5,  5,  5,  5,  0,-10,
         -5,  0,  5,  5,  5,  5,  0, -5,
          0,  0,  5,  5,  5,  5,  0, -5,
        -10,  5,  5,  5,  5,  5,  0,-10,
        -10,  0,  5,  0,  0,  0,  0,-10,
        -20,-10,-10, -5, -5,-10,-10,-20
    ],
    [
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -20,-30,-30,-40,-40,-30,-30,-20,
        -10,-20,-20,-20,-20,-20,-20,-10,
         20, 20,  0,  0,  0,  0, 20, 20,
         20, 30, 10,  0,  0, 10, 30, 20
    ],
]
# https://www.chessprogramming.org/Simplified_Evaluation_Function

piece_values = {
    0:100, # pawn
    1:300, # knight
    2:300, # bishop
    3:500, # rook
    4:900, # queen
    5:10000 # king
}


# board = chess.Board()
# def perf(n=10000):
#     for i in range(n):
#         evaluate_board(board)

# import cProfile
# cProfile.run('perf()')

# print(evaluate_board(board))

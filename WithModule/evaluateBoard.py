import chess

matches = 0
evaluations = {}

def evaluate_board(board):
    # global matches

    # hash_number = board.pawns
    # hash_number ^= board.knights
    # hash_number ^= board.bishops
    # hash_number ^= board.rooks
    # hash_number ^= board.queens
    # hash_number ^= board.kings

    # try:
    #     matches+=1
    #     return evaluations[hash_number]
    # except: pass
    # matches-=1

    balance = 0

    balance += get_piece_type_total_value(board, 0)
    balance += get_piece_type_total_value(board, 1)
    balance += get_piece_type_total_value(board, 2)
    balance += get_piece_type_total_value(board, 3)
    balance += get_piece_type_total_value(board, 4)
    balance += get_piece_type_total_value(board, 5)
    
    # evaluations[hash_number] = balance
    return balance

def get_piece_type_total_value(board, piece_type):
    total = 0

    placement_values = piece_placement_values[piece_type]
    piece_value = piece_values[piece_type]
    if piece_type==0: placements=board.pawns
    elif piece_type==1: placements=board.knights
    elif piece_type==2: placements=board.bishops
    elif piece_type==3: placements=board.rooks
    elif piece_type==4: placements=board.queens
    elif piece_type==5: placements=board.kings

    white_placements = placements & board.occupied_co[chess.WHITE]
    black_placements = placements & board.occupied_co[chess.BLACK]

    n = 63
    while white_placements:
        last_bit = white_placements & 1
        if(last_bit):
            total += placement_values[n]
            total += piece_value
        n-=1
        white_placements = white_placements >> 1

    n = 0
    while black_placements:
        last_bit = black_placements & 1
        if(last_bit):
            total -= placement_values[n]
            total -= piece_value
        n+=1
        black_placements = black_placements >> 1

    return total


piece_placement_values = {
    0:[ 
        0,  0,  0,  0,  0,  0,  0,  0,
        50, 50, 50, 50, 50, 50, 50, 50,
        10, 10, 20, 30, 30, 20, 10, 10,
        5,  5, 10, 25, 25, 10,  5,  5,
        0,  0,  0, 20, 20,  0,  0,  0,
        5, -5,-10,  0,  0,-10, -5,  5,
        5, 10, 10,-20,-20, 10, 10,  5,
        0,  0,  0,  0,  0,  0,  0,  0
    ],
    1:[
        -50,-40,-30,-30,-30,-30,-40,-50,
        -40,-20,  0,  0,  0,  0,-20,-40,
        -30,  0, 10, 15, 15, 10,  0,-30,
        -30,  5, 15, 20, 20, 15,  5,-30,
        -30,  0, 15, 20, 20, 15,  0,-30,
        -30,  5, 10, 15, 15, 10,  5,-30,
        -40,-20,  0,  5,  5,  0,-20,-40,
        -50,-40,-30,-30,-30,-30,-40,-50,
    ],
    2:[
        -20,-10,-10,-10,-10,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5, 10, 10,  5,  0,-10,
        -10,  5,  5, 10, 10,  5,  5,-10,
        -10,  0, 10, 10, 10, 10,  0,-10,
        -10, 10, 10, 10, 10, 10, 10,-10,
        -10,  5,  0,  0,  0,  0,  5,-10,
        -20,-10,-10,-10,-10,-10,-10,-20,
    ],
    3:[
         0,  0,  0,  0,  0,  0,  0,  0,
         5, 10, 10, 10, 10, 10, 10,  5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
        -5,  0,  0,  0,  0,  0,  0, -5,
         0,  0,  0,  5,  5,  0,  0,  0
    ],
    4:[
        -20,-10,-10, -5, -5,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5,  5,  5,  5,  0,-10,
         -5,  0,  5,  5,  5,  5,  0, -5,
          0,  0,  5,  5,  5,  5,  0, -5,
        -10,  5,  5,  5,  5,  5,  0,-10,
        -10,  0,  5,  0,  0,  0,  0,-10,
        -20,-10,-10, -5, -5,-10,-10,-20
    ],
    5:[
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -30,-40,-40,-50,-50,-40,-40,-30,
        -20,-30,-30,-40,-40,-30,-30,-20,
        -10,-20,-20,-20,-20,-20,-20,-10,
         20, 20,  0,  0,  0,  0, 20, 20,
         20, 30, 10,  0,  0, 10, 30, 20
    ],
}
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

# print(evaluate_board(board), matches)
import chess

board = chess.Board()
pawn_placement_values = [ 
    0,  0,  0,  0,  0,  0,  0,  0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    5,  5, 10, 25, 25, 10,  5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5, -5,-10,  0,  0,-10, -5,  5,
    5, 10, 10,-20,-20, 10, 10,  5,
    0,  0,  0,  0,  0,  0,  0,  0
 ]

def get_pawn_values_total():
    positions = board.pawns & board.occupied_co[chess.BLACK]
    return calculate_total_values(positions, pawn_placement_values)

def calculate_total_values(bitboard, values):
    total = 0
    n = 0
    while bitboard:
        last_bit = bitboard & 1
        if(last_bit):
            total+=values[n]
            print('true')
        n+=1
        bitboard = bitboard >> 1

    return total


print(get_pawn_values_total())
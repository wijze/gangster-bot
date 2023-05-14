import chess

board = chess.Board()

def get_material_balance_raw():
  balance = 0
  # balance += len(board.pawns)

  balance += len(chess.SquareSet(board.pawns & board.occupied_co[chess.WHITE]))
  balance += -len(chess.SquareSet(board.pawns & board.occupied_co[chess.BLACK]))
  balance += 3* len(chess.SquareSet(board.knights & board.occupied_co[chess.WHITE]))
  balance += -3* len(chess.SquareSet(board.knights & board.occupied_co[chess.BLACK]))
  balance += 3* len(chess.SquareSet(board.bishops & board.occupied_co[chess.WHITE]))
  balance += -3* len(chess.SquareSet(board.bishops & board.occupied_co[chess.BLACK]))
  balance += 5* len(chess.SquareSet(board.rooks & board.occupied_co[chess.WHITE]))
  balance += -5* len(chess.SquareSet(board.rooks & board.occupied_co[chess.BLACK]))
  balance += 9* len(chess.SquareSet(board.queens & board.occupied_co[chess.WHITE]))
  balance += -9* len(chess.SquareSet(board.queens & board.occupied_co[chess.BLACK]))
  
  return balance

def get_material_balance_very_raw():
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

values = {
    chess.ROOK: 5,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.QUEEN: 9,
    chess.KING: 1000,
    chess.PAWN: 1
}
symbol_values = {
    'r':5,
    'n':3,
    'b':3,
    'q':9,
    'k':100,
    'p':1,
    'R':-5,
    'N':-3,
    'B':-3,
    'Q':-9,
    'K':-100,
    'P':-1,
}



def get_material_balance_piece_map():
  balance = 0 # positive for white advantage
  piece_map = board.piece_map()

  for value in piece_map.values():
    if value.color == chess.WHITE:
      balance += values[value.piece_type]
    else:
      balance -= values[value.piece_type]

  return balance



def get_material_balance_fen():
  balance = 0
  fen = board.board_fen()
  for i in range(len(fen)):
    try:
      balance += symbol_values[fen[i]]
    except KeyError:
      pass
  return balance

def test_performance(n=10000):
  for i in range(n):
    get_material_balance_very_raw()



import cProfile
cProfile.run("test_performance()",sort="cumtime")


# n=10000

# raw: 318ms (317, 319)
# very raw: 182ms (173, 198, 177)
# piece map: 1140ms (1116, 1161, 1142)
# fen: 4174ms (3156, 5145, 4220)


# print(board.pieces())
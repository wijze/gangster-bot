def genMoves(board):
  moves = []
  #generate all possible moves (not accounting for check)
  for piece in board.array:
    moves += piece.genMoves()
  
  # loop all moves and if it results in the own king being in check delete this move
  for move in moves:
    local_board = board.makeMove(move, False)
    # local_board.testCheck() (to be added)
    pass

  return moves

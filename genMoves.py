def genMoves(board, recursivelyCalled, whiteToPlay):
  moves = []
  #generate all possible moves (not accounting for check)
  for piece in board.array:
    if piece.isWhite == whiteToPlay:
      moves += piece.genMoves()

  # loop all moves and if it results in the own king being in check delete this move
  for i in range(len(moves)):
    # check for check by generating all moves of the enemy and checking if they are taking the king
    # should only do it in depth zero, not in recursive call 
    if not recursivelyCalled:
      local_board = board.Make_move(moves[i], False)
      #checking for check, returns true if in check
      inCheck = genMoves(local_board, True, not whiteToPlay)
      if inCheck:
        #remove this move from the moves
        moves.pop(i)

    else:
      #checking for check
      king_pos = False
      for x in range(8):
        for y in range(8):
          if board.getSquare(x, y).type == "King" and board.getSquare(x, y).isWhite != whiteToPlay:
            #this is the king of the player to move so it can't be attacked
            king_pos = [x,y]
            break
        if king_pos:
          break
      if not king_pos: print("king not found")
      else:
        #check for check by seeing if an enemy piece can take the king (this is in the next turn)
        if moves[i]["toX"] == king_pos[0] and moves[i]["toY"] == king_pos[1]:
          #can take the king, delete the original move
          return True
  if recursivelyCalled:
    return False
  else:
    return moves


def compareMoves(move1, move2):
  if move1["fromX"]==move2["fromX"] and move1["fromY"]==move2["fromY"] and move1["toX"]==move2["toX"] and move1["toY"]==move2["toY"]: return True
  else: return False
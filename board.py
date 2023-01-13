# contains the board class and a function for making an empty board

# for all chess pieces
import pieces

# the Board class contains an array for all squares
# 64 items for each square one item with zero being a1 and 1 being b1
# each square contains an object of a class for what is on it.

# if you make a new board it makes it empty
# this should be changed later to the beginning position of chess

# the Board class also has a method for printing itself
# this is for debugging purposes

# enable the code at the bottom of the file to see the board

class Board:
  def __init__(self):
    print("constructor")
    self.array = emptyBoard(self)
    # should instead implement starting position

  def Make_move(self, move, apply):
    # move in format {fromX, fromY, toX toY} and if tehy have properties for castling and en passant

    # physically move piece and set old place to no piece
    copy_of_board = self
    copy_of_board.array[move.toX + (move.toY * 7)] = copy_of_board.array[move.fromX + (move.fromY * 7)]
    copy_of_board.array[move.fromX + (move.fromY * 7)] = pieces.NoPiece(move.fromX, move.fromY, copy_of_board)

    #clearing just double moved (for en passant) of pons
    for i in range(len(copy_of_board.array)):
      if copy_of_board.array[i].type == "Pon":
        copy_of_board.array[i].justDoubleMoved == False

    #checking for en passant and castling and applying other things that happen then
    if move["castling"]:
      #you can see wich site the rook was by checking the direction of the move of the king
      if move.fromX-move.toX > 0:
        copy_of_board.Make_move({
          "fromX": 7,
          "fromY": move.fromY,
          "toX": move.toX-1,
          "toY": move.fromY
        }, True)
      else:
        copy_of_board.Make_move({
          "fromX": 0,
          "fromY": move.fromY,
          "toX": move.toX+1,
          "toY": move.fromY
        }, True)
    elif move["en passant"]:
      #take the enemy pon (actually just set it to no piece)
      if copy_of_board.getSquare(move.toX, move.toY).isWhite:
        copy_of_board[move.toX + ((move.toY-1) * 7)] = pieces.NoPiece(move.toX, move.toY-1, copy_of_board)
      else:
        copy_of_board[move.toX + ((move.toY+1) * 7)] = pieces.NoPiece(move.toX, move.toY+1, copy_of_board)
    
    # changing properties if has moved
    if copy_of_board.array[move.toX + (move.toY * 7)].type == "Rook" or copy_of_board.array[move.toX + (move.toY * 7)].type == "King":
      copy_of_board.array[move.toX + (move.toY * 7)].hasMoved = True
    elif copy_of_board.array[move.toX + (move.toY * 7)].type == "Pon" and abs(move.toY-move.fromY) == 2:
      copy_of_board.array[move.toX + (move.toY * 7)].justDoubleMoved = True

    #apply if apply argument is true otherwise return the new board
    if apply:
      self = copy_of_board
    else:
      return copy_of_board


  def Log(self, fromWhite):
    for y in range(8):
      string = ""
      for x in range(8):
        if not fromWhite:
          string += self.array[x + ((7 - y) * 7)].IAM() + " "
        else:
          string += self.array[x + (y * 7)].IAM() + " "
      print(string)

  def getSquare(self, x, y):  # warning in range 0-7!!
    return self.array[x + (y * 7)]


def emptyBoard(board):
  arr = []
  for x in range(8):
    for y in range(8):
      arr.append(pieces.NoPiece(x, y, board))
  return arr


# enable code below this to test:
# creates an empty board
# adds a piece (you can change the piece to test different pieces) to a specified debug square
# you can also change the square to test different squares
# and then prints the moves that piece can make (not yet implemented for all pieces)
# and then prints the board

# the code:

# board = Board()
# debugSquareX = 4
# debugSquareY = 0
# debugSquare = debugSquareY * 7 + debugSquareX
# board.array[debugSquare] = pieces.King(debugSquareX, debugSquareY, True, board)
# print(board.array[debugSquare].genMoves())
# board.Log(True)

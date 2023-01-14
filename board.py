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
    self = StartingBoard(self)

  def Make_move(self, move, apply):
    # move in format {fromX, fromY, toX toY} and if tehy have properties for castling and en passant

    # physically move piece and set old place to no piece
    copy_of_board = self
    copy_of_board.array[move["toX"] + (move["toY"] * 7)] = copy_of_board.array[move["fromX"] + (move["fromY"] * 7)]
    copy_of_board.array[move["fromX"] + (move["fromY"] * 7)] = pieces.NoPiece(move["fromX"], move["fromY"], copy_of_board)

    #clearing just double moved (for en passant) of pons
    for i in range(len(copy_of_board.array)):
      if copy_of_board.array[i].type == "Pon":
        copy_of_board.array[i].justDoubleMoved == False

    #checking for en passant and castling and applying other things that happen then
    if "castling" in move:
      #you can see wich site the rook was by checking the direction of the move of the king
      if move["fromX"]-move["toX"] > 0:
        copy_of_board.Make_move({
          "fromX": 7,
          "fromY": move["fromY"],
          "toX": move["toX"]-1,
          "toY": move["fromY"]
        }, True)
      else:
        copy_of_board.Make_move({
          "fromX": 0,
          "fromY": move["fromY"],
          "toX": move["toX"]+1,
          "toY": move["fromY"]
        }, True)
    elif "en passant" in move:
      #take the enemy pon (actually just set it to no piece)
      if copy_of_board.getSquare(move["toX"], move["toY"]).isWhite:
        copy_of_board[move["toX"] + ((move["toY"]-1) * 7)] = pieces.NoPiece(move["toX"], move["toY"]-1, copy_of_board)
      else:
        copy_of_board[move["toX"] + ((move["toY"]+1) * 7)] = pieces.NoPiece(move["toX"], move["toY"]+1, copy_of_board)
    
    # changing properties if has moved
    if copy_of_board.array[move["toX"] + (move["toY"] * 7)].type == "Rook" or copy_of_board.array[move["toX"] + (move["toY"] * 7)].type == "King":
      copy_of_board.array[move["toX"] + (move["toY"] * 7)].hasMoved = True
    elif copy_of_board.array[move["toX"] + (move["toY"] * 7)].type == "Pon" and abs(move["toY"]-move["fromY"]) == 2:
      copy_of_board.array[move["toX"] + (move["toY"] * 7)].justDoubleMoved = True

    #apply if apply argument is true otherwise return the new board
    if apply:
      self = copy_of_board
    else:
      return copy_of_board


  def Log(self, fromWhite):
    if not fromWhite:
      string = ""
      for i in range (64):
        string+=str(self.array[i].type)+" "
        if (i+1)%8 == 0 and i!=0:
          print(string)
          string=""
    else:
      string = ""
      for i in range (64):
        string+=str(self.array[63-i].type)+" "
        if (i+1)%8 == 0 and i!=0:
          print(string)
          string=""
    

  def getSquare(self, x, y):  # warning in range 0-7!!
    return self.array[x + (y * 8)]


def emptyBoard(board):
  arr = []
  for x in range(8):
    for y in range(8):
      arr.append(pieces.NoPiece(x, y, board))
  return arr

def StartingBoard(board):
  board.array = [
    pieces.Rook(0,0,True,board),pieces.Knight(1,0,True,board),pieces.Bishop(2,0,True,board),pieces.Queen(3,0,True,board),pieces.King(4,0,True,board),pieces.Bishop(5,0,True,board),pieces.Knight(6,0,True,board),pieces.Rook(7,0,True,board),
    pieces.Pon(0,1,True,board),pieces.Pon(1,1,True,board),pieces.Pon(2,1,True,board),pieces.Pon(3,1,True,board),pieces.Pon(4,1,True,board),pieces.Pon(5,1,True,board),pieces.Pon(6,1,True,board),pieces.Pon(7,1,True,board),
    pieces.NoPiece(0,2,board),pieces.NoPiece(1,2,board),pieces.NoPiece(2,2,board),pieces.NoPiece(3,2,board),pieces.NoPiece(4,2,board),pieces.NoPiece(5,2,board),pieces.NoPiece(6,2,board),pieces.NoPiece(7,2,board),
    pieces.NoPiece(0,3,board),pieces.NoPiece(1,3,board),pieces.NoPiece(2,3,board),pieces.NoPiece(3,3,board),pieces.NoPiece(4,3,board),pieces.NoPiece(5,3,board),pieces.NoPiece(6,3,board),pieces.NoPiece(7,3,board),
    pieces.NoPiece(0,4,board),pieces.NoPiece(1,4,board),pieces.NoPiece(2,4,board),pieces.NoPiece(3,4,board),pieces.NoPiece(4,4,board),pieces.NoPiece(5,4,board),pieces.NoPiece(6,4,board),pieces.NoPiece(7,4,board),
    pieces.NoPiece(0,5,board),pieces.NoPiece(1,5,board),pieces.NoPiece(2,5,board),pieces.NoPiece(3,5,board),pieces.NoPiece(4,5,board),pieces.NoPiece(5,5,board),pieces.NoPiece(6,5,board),pieces.NoPiece(7,5,board),
    pieces.Pon(0,6,False,board),pieces.Pon(1,6,False,board),pieces.Pon(2,6,False,board),pieces.Pon(3,6,False,board),pieces.Pon(4,6,False,board),pieces.Pon(5,6,False,board),pieces.Pon(6,6,False,board),pieces.Pon(7,6,False,board),
    pieces.Rook(0,7,False,board),pieces.Knight(1,7,False,board),pieces.Bishop(2,7,False,board),pieces.Queen(3,7,False,board),pieces.King(4,7,False,board),pieces.Bishop(5,7,False,board),pieces.Knight(6,7,False,board),pieces.Rook(7,7,False,board)
  ]

  for piece in board.array:
    piece.board = board
  return board

# enable code below this to test:
# creates an empty board
# adds a piece (you can change the piece to test different pieces) to a specified debug square
# you can also change the square to test different squares
# and then prints the moves that piece can make (not yet implemented for all pieces)
# and then prints the board

# the code:

# board = Board()
# debugSquareX = 0
# debugSquareY = 1
# debugSquare = debugSquareY * 7 + debugSquareX
# board.array[debugSquare] = pieces.Pon(debugSquareX, debugSquareY, True, board)

# board.Log(True)
# print(board.array[debugSquare].genMoves())
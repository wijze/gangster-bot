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

board = Board()
debugSquareX = 5
debugSquareY = 1
debugSquare = debugSquareX * 7 + debugSquareX
board.array[debugSquare] = pieces.Rook(debugSquareX, debugSquareY, False, board)
print(board.array[debugSquare].genMoves())
board.Log(True)
#has bug
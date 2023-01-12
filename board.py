#contains the board class and a function for making an empty board

#for all chess pieces
import pieces

#the Board class contains an array for all squares
#64 items for each square one item with zero being a1 and 1 being b1
#each square contains a object of a class for what is on it.

#if you make a new board it makes it empty
#this should be changed later to the beginning position of chess

#the Board class also has a method for printing itself
#this is for debugging purposes

#enable the code at the bottom of the file to see the board

class Board:
  def __init__(self):
    print("constructor")
    self.array = emptyBoard()
    #should instead implement starting posistion
  
  def Log(self):
    for x in range(8):
      string = ""
      for y in range(8):
        string += self.array[x * 8 + y].IAM() + " "
      print(string)

  def getSquare(x, y): #warning in range 0-7!!
    return self.array[x * 8 + y]


def emptyBoard():
  arr = []
  for x in range(8):
    for y in range(8):
      arr.append(pieces.NoPiece(x, y))
  return arr

#for testing, showes the board from the array
#board = Board()
#board.Log()

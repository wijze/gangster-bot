#the base class Piece has an init method that defines it own posisition and wheter is is white or not
#it also has a method IAM that returns it own type
#and a move method that does nothing for now

#all pieces have their own class that inherits from the Piece class
#these classes only set their type for now
#the rook and king class have a special variable for if they have moved for castling
#the nopiece class has only its position


#genMove functionality has to be adde to each piece (exept nopiece)

class Piece:
  def __init__(self, posX, posY, isWhite, board):
    self.posX = posX
    self.posY = posY
    self.isWhite = isWhite
  
  def IAM(self):
    return self.type

  def Move(self):
    print("move is not implemented yet")

  def addMove(self, toX, toY):
    return {
      "fromX": self.posX,
      "fromY": self.posY,
      "toX": toX,
      "toY": toY
    }

class NoPiece(Piece):
  def __init__(self, posX, posY):
    self.type="NoPiece"
  
  def genMoves():
    return []

class Pon(Piece):
  def __init__(self, posX, posY, isWhite):
    Piece.__init__(posX, posY, isWhite)
    self.type="Pon"
    self.hasMoved = False
  
  def genMoves():
    moves = []
    print("genMoves is not implemented yet")
    if(self.isWhite):
      if(not(self.posX >= 7)):
        if(board.getSquare(self.posX, self.posY+1).type == "NoPiece"):
          moves.append(self.addMove(self.posX, self.posY+1))
          #add double step if not has moved
        #add taking
    else:
      if(not(self.posX <= 1)):
        if(board.getSquare(self.posX, self.posY+1).type == "NoPiece"):
          moves.append(self.addMove(self.posX, self.posY-1))
          #add double step if not has moved
        #add taking
    return moves

class Knight(Piece):
  def __init__(self, posX, posY, isWhite):
    Piece.__init__(posX, posY, isWhite)
    self.type="Knight"
  
  def genMoves():
    print("genMoves is not implemented yet")
    moves = []
    return moves

class Bishop(Piece):
  def __init__(self, posX, posY, isWhite):
    Piece.__init__(posX, posY, isWhite)
    self.type="Bishop"
  
  def genMoves():
    print("genMoves is not implemented yet")
    moves = []
    return moves

class Rook(Piece):
  def __init__(self, posX, posY, isWhite):
    Piece.__init__(posX, posY, isWhite)
    self.type="Rook"
    self.hasMoved = False
  
  def genMoves():
    print("genMoves is not implemented yet")
    moves = []
    return moves

class Queen(Piece):
  def __init__(self, posX, posY, isWhite):
    Piece.__init__(posX, posY, isWhite)
    self.type="Queen"
  
  def genMoves():
    print("genMoves is not implemented yet")
    moves = []
    return moves

class King(Piece):
  def __init__(self, posX, posY, isWhite):
    Piece.__init__(posX, posY, isWhite)
    self.type="King"
    self.hasMoved = False
  
  def genMoves():
    print("genMoves is not implemented yet")
    moves = []
    return moves
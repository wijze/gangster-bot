#the base class Piece has an init method that defines it own posisition and wheter is is white or not
#it also has a method IAM that returns it own type
#and a move method that does nothing for now

#all pieces have their own class that inherits from the Piece class
#these classes only set their type for now
#the rook and king class have a special variable for if they have moved for castling
#the nopiece class has only its position

#I don't know if it's necessary for all pieces to have their position but I will leave it in for now


#genMove functionality has to be adde to each piece (exept nopiece)

class Piece:
  def __init__(self, posX, posY, isWhite):
    self.posX = posX
    self.posY = posY
    self.isWhite = isWhite
  
  def IAM(self):
    return self.type

  def Move(self):
    print("move is not implemented yet")

class NoPiece(Piece):
  def __init__(self, posX, posY):
    self.type="NoPiece"
  
  def genMoves():
    return []

class Pon(Piece):
  def __init__(self, posX, posY, isWhite):
    Piece.__init__(posX, posY, isWhite)
    self.type="Pon"  
  
  def genMoves():
    print("genMoves is not implemented yet")
    return []

class Knight(Piece):
  def __init__(self, posX, posY, isWhite):
    Piece.__init__(posX, posY, isWhite)
    self.type="Knight"
  
  def genMoves():
    print("genMoves is not implemented yet")
    return []

class Bishop(Piece):
  def __init__(self, posX, posY, isWhite):
    Piece.__init__(posX, posY, isWhite)
    self.type="Bishop"
  
  def genMoves():
    print("genMoves is not implemented yet")
    return []

class Rook(Piece):
  def __init__(self, posX, posY, isWhite):
    Piece.__init__(posX, posY, isWhite)
    self.type="Rook"
    self.hasMoved = False
  
  def genMoves():
    print("genMoves is not implemented yet")
    return []

class Queen(Piece):
  def __init__(self, posX, posY, isWhite):
    Piece.__init__(posX, posY, isWhite)
    self.type="Queen"
  
  def genMoves():
    print("genMoves is not implemented yet")
    return []

class King(Piece):
  def __init__(self, posX, posY, isWhite):
    Piece.__init__(posX, posY, isWhite)
    self.type="King"
    self.hasMoved = False
  
  def genMoves():
    print("genMoves is not implemented yet")
    return []
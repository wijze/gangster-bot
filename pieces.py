# the base class Piece has an init method that defines it own position and whether is white or not
# it also has a method IAM that returns it own type
# and a move method that does nothing for now

# all pieces have their own class that inherits from the Piece class
# these classes only set their type for now
# the rook and king class have a special variable for if they have moved for castling
# the nopiece class has only its position


# genMove functionality has to be added to each piece (except nopiece)

class Piece:
  def __init__(self, posX, posY, isWhite, board):
    self.posX = posX
    self.posY = posY
    self.isWhite = isWhite
    self.board = board

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
  def __init__(self, posX, posY, board):
    self.type = "NoPiece"
    self.isWhite = False
    self.posX = posX
    self.posY = posY

  def genMoves(self):
    return []


class Pon(Piece):
  def __init__(self, posX, posY, isWhite, board):
    Piece.__init__(self, posX, posY, isWhite, board)
    self.type = "Pon"
    self.hasMoved = False
    self.justDoubleMoved = False

  def genMoves(self):
    moves = []
    if self.isWhite:
      if self.posY < 7:
        if self.board.getSquare(self.posX, self.posY + 1).type == "NoPiece":
          moves.append(self.addMove(self.posX, self.posY + 1))
          # double if it hasn't moved yet
          if not self.hasMoved and self.board.getSquare(self.posX, self.posY + 2).type == "NoPiece" and self.posY==1:
            moves.append(self.addMove(self.posX, self.posY + 2))
        # taking
        if self.board.getSquare(self.posX - 1, self.posY + 1).type != "NoPiece" and not self.board.getSquare(self.posX - 1, self.posY + 1).isWhite:
          moves.append(self.addMove(self.posX - 1, self.posY + 1))
        if self.board.getSquare(self.posX + 1, self.posY + 1).type != "NoPiece" and not self.board.getSquare(self.posX + 1, self.posY + 1).isWhite:
          moves.append(self.addMove(self.posX + 1, self.posY + 1))
        # en passant
        if self.board.getSquare(self.posX-1, self.posY).type == "Pon" and not self.board.getSquare(self.posX-1, self.posY).isWhite:
          if self.board.getSquare(self.posX-1, self.posY).justDoubleMoved:
            moves.append(self.addMove(self.posX - 1, self.posY + 1))
        if self.board.getSquare(self.posX+1, self.posY).type == "Pon" and not self.board.getSquare(self.posX+1, self.posY).isWhite:
          if self.board.getSquare(self.posX+1, self.posY).justDoubleMoved:
            moves.append(self.addMove(self.posX + 1, self.posY + 1))
    else:
      if self.posY > 0:
        if self.board.getSquare(self.posX, self.posY + 1).type == "NoPiece":
          moves.append(self.addMove(self.posX, self.posY - 1))
          # double if it hasn't moved yet
          if not self.hasMoved and self.board.getSquare(self.posX, self.posY - 2).type == "NoPiece" and self.posY==6:
            moves.append(self.addMove(self.posX, self.posY - 2))
        # taking
        if self.board.getSquare(self.posX - 1, self.posY - 1).type != "NoPiece" and self.board.getSquare(self.posX - 1, self.posY - 1).isWhite:
          moves.append(self.addMove(self.posX - 1, self.posY + 1))
        if self.board.getSquare(self.posX + 1, self.posY - 1).type != "NoPiece" and self.board.getSquare(self.posX + 1, self.posY - 1).isWhite:
          moves.append(self.addMove(self.posX + 1, self.posY - 1))
        # en passant
        if self.board.getSquare(self.posX - 1, self.posY).type == "Pon" and self.board.getSquare(self.posX - 1,self.posY).isWhite:
          if self.board.getSquare(self.posX - 1, self.posY).justDoubleMoved:
            moves.append(self.addMove(self.posX - 1, self.posY - 1))
        if self.board.getSquare(self.posX + 1, self.posY).type == "Pon" and self.board.getSquare(self.posX + 1,self.posY).isWhite:
          if self.board.getSquare(self.posX + 1, self.posY).justDoubleMoved:
            moves.append(self.addMove(self.posX + 1, self.posY - 1))
    return moves


class Knight(Piece):
  def __init__(self, posX, posY, isWhite, board):
    Piece.__init__(self, posX, posY, isWhite, board)
    self.type = "Knight"
    self.relative_moves = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]

  def genMoves(self):
    moves = []
    for move in self.relative_moves:
      if not (self.posY+move[1]>7 or self.posY+move[1]<0 or self.posX+move[0]>7 or self.posX+move[0]<0):
        if self.board.getSquare(self.posX+move[0], self.posY+move[1]).type == "NoPiece":
          #white
          if self.isWhite and not self.board.getSquare(self.posX+move[0], self.posY+move[1]).isWhite:
            moves.append(self.addMove(self.posX+move[0], self.posY+move[1]))
          #black
          if not self.isWhite and self.board.getSquare(self.posX+move[0], self.posY+move[1]).isWhite:
            moves.append(self.addMove(self.posX+move[0], self.posY+move[1]))
    return moves


class Bishop(Piece):
  def __init__(self, posX, posY, isWhite, board):
    Piece.__init__(self, posX, posY, isWhite, board)
    self.type = "Bishop"

  def genMoves(self):
    moves = genMovesSlider([[1, 1], [1, -1], [-1, -1], [-1, 1]], 7, [self.posX, self.posY], self.board)
    for i in range(len(moves)):
      moves[i] = self.addMove(moves[i][0], moves[i][1])
    return moves


class Rook(Piece):
  def __init__(self, posX, posY, isWhite, board):
    Piece.__init__(self, posX, posY, isWhite, board)
    self.type = "Rook"
    self.hasMoved = False

  def genMoves(self):
    moves = genMovesSlider([[1, 0], [0, 1], [-1, 0], [0, -1]], 7, [self.posX, self.posY], self.board)
    for i in range(len(moves)):
      moves[i] = self.addMove(moves[i][0], moves[i][1])
    return moves


class Queen(Piece):
  def __init__(self, posX, posY, isWhite, board):
    Piece.__init__(self, posX, posY, isWhite, board)
    self.type = "Queen"

  def genMoves(self):
    moves = genMovesSlider([[1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1,1], [0, 1]], 7, [self.posX, self.posY], self.board)
    for i in range(len(moves)):
      moves[i] = self.addMove(moves[i][0], moves[i][1])
    return moves


class King(Piece):
  def __init__(self, posX, posY, isWhite, board):
    Piece.__init__(self, posX, posY, isWhite, board)
    self.type = "King"
    self.hasMoved = False

  def genMoves(self):
    moves = genMovesSlider([[1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1,1], [0, 1]], 1, [self.posX, self.posY], self.board)
    for i in range(len(moves)):
      moves[i] = self.addMove(moves[i][0], moves[i][1])
    
    #castling: add castling
    if self.isWhite:
      if (not self.hasMoved) and self.board.getSquare(self.posX-4, self.posY).type == "Rook":
        if not self.board.getSquare(self.posX-4, self.posY).hasMoved:
          if self.board.getSquare(self.posX-1, self.posY).type == "NoPiece" and self.board.getSquare(self.posX-2, self.posY).type == "NoPiece" and self.board.getSquare(self.posX-3, self.posY).type == "NoPiece":
            move = self.addMove(self.posX-2, self.posY)
            move["castling"] = True
            moves.append(move)
      if (not self.hasMoved) and self.board.getSquare(self.posX+3, self.posY).type == "Rook":
        if not self.board.getSquare(self.posX+3, self.posY).hasMoved:
          if self.board.getSquare(self.posX+1, self.posY).type == "NoPiece" and self.board.getSquare(self.posX+2, self.posY).type == "NoPiece":
            move = self.addMove(self.posX+2, self.posY)
            move["castling"] = True
            moves.append(move)
    else:
      if (not self.hasMoved) and self.board.getSquare(self.posX+4, self.posY).type == "Rook":
        if not self.board.getSquare(self.posX+4, self.posY).hasMoved:
          if self.board.getSquare(self.posX+1, self.posY).type == "NoPiece" and self.board.getSquare(self.posX+2, self.posY).type == "NoPiece" and self.board.getSquare(self.posX+3, self.posY).type == "NoPiece":
            move = self.addMove(self.posX+2, self.posY)
            move.castling = True
            moves.append(move)
      if (not self.hasMoved) and self.board.getSquare(self.posX-3, self.posY).type == "Rook":
        if not self.board.getSquare(self.posX-3, self.posY).hasMoved:
          if self.board.getSquare(self.posX-1, self.posY).type == "NoPiece" and self.board.getSquare(self.posX-2, self.posY).type == "NoPiece":
            move = self.addMove(self.posX-2, self.posY)
            move.castling = True
            moves.append(move)
    return moves


def genMovesSlider(directions, distance, position, board):
  moves = []
  for direction in directions:
    for i in range(distance):
      toX = direction[0]*(i+1)+position[0]
      toY = direction[1]*(i+1)+position[1]
      if toX <= 7 and toY <= 7 and toX >= 0 and toY >= 0:
        if board.getSquare(toX, toY).type == "NoPiece":
          moves.append([toX, toY])
        else:
          break
  return moves


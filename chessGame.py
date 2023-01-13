# this the central class that controls the game loop

# import board for keeping the board
import board
# import move genrator for cheking if the player move is legal and later bot
import genMoves as moveGenerator
# the bot, for generating moves
import bot

class Game:
  def __init__(self):
    self.board = board.Board()
    self.white_to_play = True
  
  def playMove(self, playedMove):
    #check if move is in legal moves
    legal_moves = moveGenerator.genMoves(self.board, False, self.white_to_play)
    for move in legal_moves:
      if moveGenerator.compareMoves(move, playedMove):
        print("succes!")
        self.board.Make_move(playedMove, True)
        self.white_to_play = not self.white_to_play
        return True
    # if it was not encountered the move is illegal
    print("failed :( move is illegal")
    return False
  
  def AI_move(self):
    move = bot.generateMove(self.board, self.white_to_play)
    self.board.Make_move(move, True)
    self.white_to_play = not self.white_to_play
    return True
    
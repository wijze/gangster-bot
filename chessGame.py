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
    self.board.Make_move(playedMove, True)
    self.white_to_play = not self.white_to_play
  
  def AI_move(self):
    move = bot.generateMove(self.board, self.white_to_play)
    self.playMove(move)
    
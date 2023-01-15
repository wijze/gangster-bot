# return a random move for now
import random
# for generating all moves
import genMoves as MoveGenerator
# for maipulating board
import board

def generateMove(board, white_to_play):
  possible_moves = MoveGenerator.genMoves(board, False, white_to_play)
  chosen_move = random.randint(0, len(possible_moves)-1)
  return possible_moves[chosen_move]
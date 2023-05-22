import chess

import display
import ai

class Game:
	def __init__(self) -> None:
		self.board = chess.Board()
		self.display = display.Display(self.board)
		

	def enterMove(self, move):
		self.board.push(move)
		self.display.update(self.board)
	
	def PlayerMove(self):
		while True:
			try: # chess.Move.from_uci crashes if move is not in correct format
				move = chess.Move.from_uci(input("move: "))
				if move in list(self.board.legal_moves):
					self.enterMove(move)
					break
				else:
					print("warning: invalid move")
			except chess.InvalidMoveError:
				print("warning invalid move")
			
	
	def ai_move(self):
		move = ai.generate_move(self.board)
		print("ai_move:", str(move['move']))
		print('evaluation:',move['evaluation']/100)
		self.enterMove(move['move'])



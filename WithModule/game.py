import chess
import random
import display

class Game:
	def __init__(self) -> None:
		self.board = chess.Board()
		self.display = display.Display(self.board)
		

	def enterMove(self, move):
		self.board.push(move)
		self.display.update(self.board)
	
	def PlayerMove(self):
		while True:
			#try: # chess.Move.from_uci crashes if move is not in correct format
				move = chess.Move.from_uci(input("move: "))
				if move in list(self.board.legal_moves):
					self.enterMove(move)
					break
				else:
					print("warning: invalid move")
			#except:
			#	print("warning invalid move")
			
	
	def ai_move(self):
		legal_moves = list(self.board.legal_moves)
		move = legal_moves[random.randrange(0, len(legal_moves))]
		print("ai_move:", str(move))
		self.enterMove(move)
		# board.suggest(thinking_time=2)



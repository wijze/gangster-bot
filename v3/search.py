from multiprocessing import Process
from time import sleep

from evaluateBoard import evaluate_board

class Search:
	def __init__(self, settings) -> None:
		self.settings = settings
		self.best_move = None
		# self.current_best_evaluation = -self.settings.matings_score
		self.board = None
		self.search_ended = False
	
	def end_search(self):
		self.search_ended = True
	
	def start_search(self, board):
		self.board = board

		if self.settings.iterative_deepening:
			target_depth = self.settings.depth if self.settings.fixed_depth else 100
			search_process = Process(target = self.iterative_deepening_search, args = (target_depth))
			sleep(self.settings.time_limit)
			self.end_search()
			search_process.join() # wait until it is finished closing
		else:
			self.search(self.settings.depth, -self.settings.matings_score-1, self.settings.matings_score+1)

	
	def iterative_deepening_search(self, target_depth):
		for current_depth in range(target_depth):
			if self.search_ended: break
			self.current_best_move = self.search(current_depth)

	
	def search(self, depth, alpha, beta):
		# time is over
		if self.search_ended:
			return -self.settings.matings_score

		# check for repetition
		# check for transposition

		if depth == 0:
			# return self.capture_and_check_only_search()
			# just return evaluation of position for now
			if self.board.turn:
				return evaluate_board(self.board)
			else:
				return - evaluate_board(self.board)

		moves = self.board.legal_moves
		best_move = None
		if len(list(moves)) == 0:
			if(self.board.is_checkmate()):
				return -self.settings.matings_score
			else:
				return 0 # draw
		# order moves

		for move in moves:
			self.board.push(move)
			eval = -self.search(depth-1, -beta, -alpha)
			self.board.pop()
			if eval >= beta:
				# store eval in transposition table
				return beta # pruned (move was to good)
			if eval > alpha:
				alpha = eval
				best_move = move
				# print("found better move: eval=", eval)

		self.best_move = best_move
		# store eval in transposition table
		return alpha
		
	def capture_and_check_only_search():
		return 
		# returns evaluation after having searched checks and captures to reach a quiet position
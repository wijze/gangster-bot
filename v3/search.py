import multiprocessing
import time

class Search:
	def __init__(self, settings) -> None:
		self.settings = settings
		self.current_best_move = None
		self.board = None
	
	def end_search(self):
		self.search_ended = True
	
	def start_search(self, board):
		self.board = board

		if self.settings.iterative_deepening:
			target_depth = self.settings.depth if self.settings.fixed_depth else 100
			search_process = multiprocessing.Process(target = self.iterative_deepening_search, args = (target_depth))
			time.sleep(self.settings.time_limit)
			self.end_search()
			search_process.join() # wait until it is finished closing

	
	def iterative_deepening_search(self, target_depth):
		for current_depth in range(target_depth):
			if self.search_ended: break
			self.current_best_move = self.search(current_depth)

	
	def search(self, depth, alpha, beta):
		if self.search_ended:
			return -self.settings.matings_score

		# check for repetition
		# check for transposition

		if depth == 0:
			return self.capture_and_check_only_search()
		
		moves = [] # generate moves
		# order moves
		if len(moves) == 0:
			return # 0 for draw, or mate score

		for move in moves:
			# board.make_move(move)
			eval = self.search(depth-1, -beta, -alpha)
			# board.unmake_move()
			if eval >= beta:
				# store eval in transposition table
				return beta # pruned (move was to good)
			if eval > alpha:
				alpha = eval
				# best_move = move

		# store eval in transposition table
		return alpha
		
	def capture_and_check_only_search():
		return 
		# returns evaluation after having searched checks and captures to reach a quiet position
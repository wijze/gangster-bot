from multiprocessing import Process
from time import sleep
from random import shuffle
import chess

from evaluateBoard import evaluate_board, get_material_balance

class Search:
	def __init__(self, settings) -> None:
		self.settings = settings
		self.best_move = None
		self.best_evaluation = -self.settings.matings_score
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
			self.search(current_depth)

	
	def search(self, depth, alpha, beta):
		# time is over
		# if self.search_ended:
		# 	return -self.settings.matings_score
		
		# check for mate or draw
		if(self.board.is_checkmate()):
			return -self.settings.matings_score
		elif self.board.can_claim_draw() or self.board.is_game_over():
			return self.settings.draw_score
		# check for transposition

		if depth == 0:
			# if self.board.turn: evaluation = get_material_balance(self.board)
			# else: evaluation = - get_material_balance(self.board)
			# return evaluation
			return self.not_quiet_search(alpha, beta)

		best_move = None
		best_eval = -self.settings.matings_score
		moves = list(self.board.legal_moves)
		shuffle(moves)

		for move in moves:
			self.board.push(move)
			# print("start, normal, depth:",depth, "move:", move)
			evaluation = -self.search(depth-1, -beta, -alpha)
			# print("end, normal, depth:",depth, "move:", move, "eval:",evaluation)
			self.board.pop()
			if evaluation >= beta:
				# store eval in transposition table
				return beta # pruned (move was to good)
			if evaluation > alpha:
				alpha = evaluation
				best_move = move
				best_eval = evaluation

		self.best_move = best_move
		self.best_evaluation = best_eval
		# store eval in transposition table
		return alpha
		
	# returns evaluation after having searched checks and captures to reach a quiet position
	def not_quiet_search(self, alpha, beta, depth=0):
		if depth>self.settings.capture_search_depth: return beta # TODO come up with a better solution 
		if self.board.turn: evaluation = evaluate_board(self.board)
		else: evaluation = - evaluate_board(self.board)

		if evaluation > beta: return beta # this position won't be reached because it's to good
		if evaluation > alpha: alpha = evaluation

		# generate not quiet moves (captures etc)
		moves = list(self.board.generate_legal_moves(chess.BB_ALL, self.board.occupied_co[not self.board.turn]))

		for move in moves:
			self.board.push(move)
			# print("start, extended, depth:",depth, "move:", move)
			evaluation = -self.not_quiet_search(-beta, -alpha, depth+1)
			# print("end, extended, depth:",depth, "move:", move, "eval:",evaluation)
			self.board.pop()

			if evaluation > beta: return beta
			if evaluation > alpha: alpha = evaluation
		
		return alpha

from window import Window
from players import *
from search_settings import Search_settings
from game import Game

from multiprocessing import Process, Queue
from queue import Empty
from time import sleep

def get_results_formatted(results_array):
    result = ""
    result += "white: " + str(results_array.count("white")) + "\n"
    result += "black: " + str(results_array.count("black")) + "\n"
    result += "draw: " + str(results_array.count("draw")) + "\n"
    return result

class Main():
    def __init__(self, n_games):
        self.results = []
        self.n_games_left = n_games
        self.game = Game() # temporary game for display
        self.update_board_qeue = Queue()
        self.user_move_qeue = Queue()

    def set_players(self, player1, player2):
        self.white_player = player1
        self.black_player = player2

    def open_window(self):
        self.drawing_process = Process(target=self.display_loop)
        self.drawing_process.start()

    def make_move(self, move): # players can call this to make a move
        if not self.game.make_move(move): 
            return False # move was illegal

    def handle_user_move(self): # is called when an user finishes a move
        if not self.user_move_qeue.empty():
            move = self.user_move_qeue.get_nowait()
            if not self.white_player.user_move(move):
                self.black_player.user_move(move)
    
    def display_loop(self): # updates the display
        self.window = Window(self.user_move_qeue)
        while self.window.running:
            if not self.update_board_qeue.empty():
                updated_board = self.update_board_qeue.get_nowait()
                self.window.update(updated_board)
            elif self.update_board_qeue.empty(): 
                self.window.update()
    
    def start_games_loop(self):
        while self.n_games_left > 0:
            print("new game", self.n_games_left, "games left after this")
            self.start_new_game()
        print("\n", get_results_formatted(self.results), "\n", self.results)


    def start_new_game(self):
        self.n_games_left-=1
        self.game = Game()
        self.update_board_qeue.put_nowait(self.game.board)
        self.black_player.turn = False
        self.white_player.turn = False
        while not self.game.is_over:
            # sleep(0.5)
            if(self.game.white_turn):
                self.white_player.request_move(self.game.board)
            else:
                self.black_player.request_move(self.game.board)
            self.handle_user_move()
            self.update_board_qeue.put_nowait(self.game.board)
        self.end_game()
    
    def end_game(self):
        self.results.append(self.game.outcome)
        print("game outcome: ", self.game.outcome)

def main(window = True):
    m = Main(1)
    m.set_players(
        User(m, None),
        AI(m, Search_settings())
    )
    if window:
        m.open_window()
    m.start_games_loop()

if __name__ == '__main__':
    main(True)
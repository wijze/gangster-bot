from window import Window
from players import *
from search_settings import Search_settings
from game import Game

from multiprocessing import Process
from time import sleep

class Main():
    def __init__(self, n_games):
        self.results = []
        self.n_games_left = n_games
        self.game = Game(self) # temporary game for display

    def set_players(self, player1, player2):
        self.white_player = player1
        self.black_player = player2

    def open_window(self):
        self.drawing_process = Process(target=self.main_loop)
        self.drawing_process.start()

    def make_move(self, move): # players can call this to make a move
        if not self.game.make_move(move): 
            return False # move was illegal
        if self.game.is_over: return
        sleep(0.2)
        
        if self.game.white_turn:
            self.white_player.request_move(self.game.board)
        else:
            self.black_player.request_move(self.game.board)

    def handle_player_move_attempt(self, move): # is called when an user finishes a move
        if not self.white_player.user_move(move):
            self.black_player.user_move(move)
    
    def main_loop(self): # updates the display
        self.window = Window(self.handle_player_move_attempt)
        while self.window.running:
            self.window.update(self.game.board)
    
    def start_new_game(self):
        print("new game")
        self.n_games_left -= 1
        self.game = Game(self)
        self.white_player.request_move(self.game.board)
    
    def end_game(self):
        self.results.append(self.game.outcome)
        print("game outcome: ", self.game.outcome)
        print(self.n_games_left, " games left")
        if self.n_games_left > 0:
            self.start_new_game()
        else: 
            print(self.results)


def main():
    m = Main(0)
    m.set_players(
        User(m.make_move, None),
        First_move_AI(m.make_move, Search_settings())
    )
    m.open_window()
    m.start_new_game()

if __name__ == '__main__':
    main()
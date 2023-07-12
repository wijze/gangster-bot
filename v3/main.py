from window import Window
from players import *
from search_settings import Search_settings
from game import Game

from multiprocessing import Process, Queue
from time import sleep

def get_results_formatted(results_array):
    result = ""
    result += "white: " + str(results_array.count("white")) + "\n"
    result += "black: " + str(results_array.count("black")) + "\n"
    result += "draw: " + str(results_array.count("draw")) + "\n"
    return result

class Settings:
    def __init__(self, n_games=1, wait_time=0.5) -> None:
        self.wait_time = wait_time
        self.n_games = n_games
        self.print_turns = False
        self.print_moves = False
        self.print_raw_results = True
        self.open_window = True

class Main():
    def __init__(self, settings):
        self.settings = settings
        self.results = []
        self.n_games_left = settings.n_games
        self.game = Game() # temporary game for display
        self.update_board_qeue = Queue()
        self.user_move_qeue = Queue()
        if self.settings.open_window: self.open_window()

    def set_players(self, player1, player2):
        self.white_player = player1
        self.black_player = player2

    def open_window(self):
        self.drawing_process = Process(target=self.display_loop)
        self.drawing_process.start()

    def make_move(self, move): # players can call this to make a move
        if not self.game.make_move(move): 
            return False # move was illegal
        else: 
            if self.settings.print_moves: print(move)
            if self.settings.print_turns: print("white:" if self.game.white_turn else "black:")

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
        
        # finished
        print("\n")
        if self.settings.print_raw_results: print(self.results)
        print(get_results_formatted(self.results))
        self.white_player.close()
        self.black_player.close()

    def start_new_game(self):
        self.n_games_left-=1
        self.game = Game()
        self.update_board_qeue.put_nowait(self.game.board)
        self.black_player.turn = False
        self.white_player.turn = False
        while not self.game.is_over:
            if(self.game.white_turn):
                self.white_player.request_move(self.game.board)
            else:
                self.black_player.request_move(self.game.board)
            self.handle_user_move()
            self.update_board_qeue.put_nowait(self.game.board)
            sleep(self.settings.wait_time)
        self.end_game()
    
    def end_game(self):
        self.results.append(self.game.outcome)
        print("game outcome: ", self.game.outcome)


def main():
    m = Main(Settings(n_games=1))
    m.set_players(
        AI(m, Search_settings(depth=2)),
        AI(m, Search_settings(depth=2))
    )
    m.start_games_loop()


if __name__ == '__main__':
    main(True)
from window import Window
from players import Player, First_move_AI, AI, User
from search_settings import Search_settings
from game import Game

from multiprocessing import Process

class Main():
    def __init__(self):
        self.results = []
        self.running = True

        self.white_player = Player(None, None) # temporary
        self.black_player = Player(None, None) # temporary

        self.start_new_game()

    def open_window(self):
        self.drawing_process = Process(target=self.main_loop)
        self.drawing_process.start()

    def set_players(self, player1, player2):
        self.white_player = player1
        self.black_player = player2

    def make_move(self, move): # players can call this to make a move
        if not self.game.make_move(move): 
            return False # move was illegal
        if self.game.is_over: return
        
        if self.game.white_turn:
            self.white_player.request_move(self.game.board)
        else:
            self.black_player.request_move(self.game.board)

    def handle_player_move_attempt(self, move): # is called when an user finishes a move
        self.white_player.user_move(move)
        self.black_player.user_move(move)
    
    def main_loop(self): # updates the display
        self.window = Window(self.handle_player_move_attempt)
        while self.running and self.window.running:
            self.window.update(self.game.board)
    
    def start_new_game(self):
        self.game = Game()
        self.white_player.request_move(self.game.board)
    
    def play_multiple_games(self, n):
        # maybe change it to be done in parralel
        for i in range(n):
            self.start_new_game()
            while (not self.game.is_over) and self.running:
                pass # infinite loop to wait for game to be over
            self.results.append(self.game.outcome)
        print("total results: ", self.results)


def main():
    m = Main()
    m.set_players(
        User(m.make_move, None),
        First_move_AI(m.make_move, Search_settings())
    )
    m.open_window()
    m.start_new_game()

if __name__ == '__main__':
    main()
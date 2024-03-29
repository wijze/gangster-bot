from window import Window
from players import *
from search_settings import Search_settings
from game import Game

from multiprocessing import Process, Queue, Pool
from time import sleep


def get_results_formatted(results_array):
    result = ""
    result += "white: " + str(results_array.count("white")) + "\n"
    result += "black: " + str(results_array.count("black")) + "\n"
    result += "draw: " + str(results_array.count("draw")) + "\n"
    return result


class Settings:
    def __init__(
        self,
        n_games=1,
        wait_time=0,
        parralel_simulations=1,
        print_individual_results=False,
        print_games_left_every=1,
    ) -> None:
        self.wait_time = wait_time
        self.n_games = n_games

        self.print_turns = False
        self.print_moves = False

        self.print_games_left_every = print_games_left_every
        self.print_individual_results = print_individual_results

        self.print_raw_results = True

        self.open_window = True

        self.n_parallel_simulations = parralel_simulations
        self.parallel_simulating = parralel_simulations > 1
        if self.parallel_simulating:
            self.open_window = False  # TODO maybe change


class Simulating_settings(Settings):
    def __init__(
        self, n_games=100, parralel_simulations=5, print_games_left_every=10
    ) -> None:
        if parralel_simulations > 20:
            parralel_simulations = 20  # can't handle to many
        super().__init__(
            n_games, 0, parralel_simulations, print_individual_results=True
        )
        self.open_window = False
        self.print_individual_results = False
        self.print_games_left_every = print_games_left_every


class Debug_settings(Settings):
    def __init__(self, n_games=1, wait_time=0.5, print_moves=False) -> None:
        super().__init__(n_games, 0.5, 1, print_individual_results=True)
        self.print_moves = print_moves
        self.wait_time = wait_time


# TODO maybe add settings to game


class Main:
    def __init__(self, settings):
        self.settings = settings
        self.results = []
        self.n_games_left = settings.n_games
        self.game = Game()  # temporary game for display
        if not self.settings.parallel_simulating:
            self.update_board_qeue = Queue()
            self.user_move_qeue = Queue()
        if self.settings.open_window:
            self.open_window()

    def set_players(self, player1, player2):
        self.white_player = player1
        self.black_player = player2

    def open_window(self):
        self.drawing_process = Process(target=self.display_loop)
        self.drawing_process.start()

    def make_move(self, move):  # players can call this to make a move
        if not self.settings.parallel_simulating:
            self.update_board_qeue.put_nowait((None, move.to_square))

    def handle_user_move(self):
        if not self.user_move_qeue.empty():
            move = self.user_move_qeue.get_nowait()
            if not self.white_player.user_move(move):  # attempt fails
                self.black_player.user_move(move)

    def display_loop(self):  # updates the display
        self.window = Window(self.user_move_qeue)
        while self.window.running:
            if not self.update_board_qeue.empty():
                updated_board, move_square = self.update_board_qeue.get_nowait()
                self.window.update(updated_board, move_square)
            elif self.update_board_qeue.empty():
                self.window.update()

    def start_games_loop(self):
        if self.settings.parallel_simulating:
            pool = Pool(processes=self.settings.n_parallel_simulations)
            self.results = pool.map(self.start_new_game, range(self.settings.n_games))
            pool.close()
            pool.join()
        else:
            for i in range(self.settings.n_games):
                self.results.append(self.start_new_game(i))

        # finished
        print("\n")
        if self.settings.print_raw_results:
            print(self.results)
        print(get_results_formatted(self.results))
        self.white_player.close()
        self.black_player.close()

    def start_new_game(self, n_game):
        if n_game % self.settings.print_games_left_every == 0:
            print("new game", self.settings.n_games - n_game, "games left after this")
        game = Game(self.make_move)
        if not self.settings.parallel_simulating:
            self.update_board_qeue.put_nowait((game.board, None))

        self.black_player.turn = False
        self.white_player.turn = False
        while not game.is_over:
            if game.white_turn:
                self.white_player.request_move(game)
            else:
                self.black_player.request_move(game)
            if not self.settings.parallel_simulating:
                self.handle_user_move()
            if not self.settings.parallel_simulating:
                self.update_board_qeue.put_nowait((game.board, None))
            sleep(self.settings.wait_time)
        if self.settings.print_individual_results:
            print("game outcome: ", game.outcome)
        return game.outcome


def main():
    m = Main(Debug_settings(wait_time=0.1))
    m.set_players(
        User(),
        AI(Search_settings(depth=3)),
    )
    m.start_games_loop()


if __name__ == "__main__":
    main()

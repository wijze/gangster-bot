import game # does handling the game

def main():
    current_game = game.Game()
    while not(current_game.board.is_checkmate()) and not(current_game.board.is_stalemate()):
        current_game.PlayerMove()
        current_game.ai_move()

main()
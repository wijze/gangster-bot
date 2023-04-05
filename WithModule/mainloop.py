import game # does handling the gamea2

def main():
    current_game = game.Game()
    while True:
        if not(current_game.board.is_checkmate()) and (not(current_game.board.is_stalemate())):
            current_game.PlayerMove()
        else: break
        if not(current_game.board.is_checkmate()) and (not(current_game.board.is_stalemate())):
            current_game.ai_move()
        else: break
    print("game over")
main()
import chess


def main():
    board = chess.Board()
    while not(board.is_checkmate()) and not(board.is_stalemate()):
        board.push(ask(board))
        # ai move


def ask(board):
    while True:
        print(board)
        move = chess.Move.from_uci(input("move: "))
        if move in list(board.legal_moves):
            return move
        else:
            print("invalid")


main()

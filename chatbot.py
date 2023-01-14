import validator

import chessGame as Game

def main():
    welcome()

def verifyInpStr(inputStr):
    return validator.checkStringFormat(inputStr)

def answer(move):
    #should generate the answer (the best move)
    return "answer"

def printHelp(playing):
    print("exit to exit")
    if(playing):
        print("a chess move to play it")
    else:
        print("start to start")
    


def welcome():
    running = True
    while running:
        print("hello I am a (not finished) chat/chess bot")
        inpString = input("Enter a start to start or help for all commands: ")
        if inpString == "help":
            printHelp(False)
        elif inpString == "exit":
            running = False
            print("exited")
        elif inpString == "start":
            game()
            return
        else:
            print("sorry I didn't understand that")


def game():
    game = Game.Game()
    running = True
    while running:
        inpString = input("Enter a move or help for all commands: ")

        if verifyInpStr(inpString):
            #returns false if not in correct format
            parcedMove = validator.parce_inp_string(inpString)
            if parcedMove:
                game.playMove(parcedMove)
                game.AI_move()
            else: continue
        elif inpString=="help":
            printHelp(True)
        elif inpString == "exit":
            running = False
            print("exited")
        else:
            print("sorry I didn't understand that")
        game.board.Log(True)

main()
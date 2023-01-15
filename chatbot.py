import validator


def Help(playing):
    print("help for all commands")
    print("exit to exit")
    if playing: print("a chess move to play it")
    else: print("start to start")


def Ask(playing, game):
    if playing:
        inpString = input("Enter a move or help for all commands: ")
        move = validator.validateMove(inpString, game)
        if inpString == "help": 
            Help(playing)
            return Ask(playing, game)
        elif inpString == "exit": return False
        else:
            if move == "invalid":
                print("sorry this move was invalid")
                return Ask(playing, game)
            elif move:
                return move
            else:
                print("sorry I didn't understand you")
                return Ask(playing, game)
    else:
        inpString = input("Enter start to start or help for all commands: ")
        if inpString == "help": 
            Help(playing)
            return Ask(playing, game)
        elif inpString == "exit": return False
        elif inpString == "start": return True
        else:
            print("sorry I didn't understand you")
            return Ask(playing, game)

import validator


def Help(playing):
    print("help for all commands")
    print("exit to exit")
    if playing: print("a chess move to play it")
    else: print("start to start")


def Ask(playing):
    if playing:
        inpString = input("Enter a move or help for all commands: ")
        move = validator.checkStringFormat(inpString)
        if inpString == "help": 
            Help(playing)
            return Ask(playing)
        elif inpString == "exit": return False
        else:
            if move == "invalid":
                return Ask(playing)
            elif move:
                return move
            else:
                print("sorry I didn't understand you")
                return Ask(playing)
    else:
        inpString = input("Enter start to start or help for all commands: ")
        if inpString == "help": 
            Help(playing)
            return Ask(playing)
        elif inpString == "exit": return False
        elif inpString == "start": return True
        else:
            print("sorry I didn't understand you")
            return Ask(playing)

import validator

running = True

#shouldn't start at run but rather first ask you what to do and if you answer start then start
while running:
    inpString = input("Enter a move or exit to exit: ")
    #we should implement a more commands like help and start
    #we should use a switch thing  for all possible kinds of answers
    if inpString == "exit":
        running = False
        print("exited")
    elif verifyInpStr(inpString):
        print(answer())
        continue
    else:
        print("sorry I didn't understand that")

def verifyInpStr(input):
    return validator.checkStringFormat(input)

def answer():
    #should generate the answer (the best move)
    return "answer"

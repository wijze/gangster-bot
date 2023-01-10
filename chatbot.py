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

def verifyInpStr(input):
    #should implement a way to check if the input is valid
    return True

def answer():
    #should generate the answer (the best move)
    return "answer"
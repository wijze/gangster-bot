running = True

#shouldn't start at run but rather first ask you what to do and if you answer start then start
while running:
    inpString = input("Enter a move or exit to exit: ")
    #we should implement a more command like help and start
    if verifyInpStr(inpString):
        print(answer())
        continue
    elif inpString == "exit":
        running = False
        print("exited")

def verifyInpStr(input):
    #should implement a way to check if the input is valid
    return True

def answer():
    #should generate the answer (the best move)
    return "answer"
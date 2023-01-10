running = True

while running:
    inpString = input("Enter a number or exit to exit: ")
    if inpString.isdigit():
        print(int(inpString) + 1)
        continue
    elif inpString == "exit":
        running = False
        print("exited")

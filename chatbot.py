running = True
while running:
    while True:
        try:
            inpString = input("Please enter a number: ")
            inp = int(inpString)
        except ValueError:
            if inpString == "exit":
                running = False
                break
            else:
                print("Sorry, I didn't understand that.")
            continue
        else:
            print(inp + 1)
            break

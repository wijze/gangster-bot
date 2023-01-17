import tkinter as tk

root = tk.Tk()
root.title("test")

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack()

dimensions = 8
square_size = 32

colors = ["white", "gray"]

board = tk.Canvas(root, width=dimensions*square_size, height=dimensions*square_size)
board.pack()

for row in range (dimensions):
  for column in range (dimensions):
    if (((row+column)/2)%1) == 0: color = colors[0]
    else: color = colors[1]
    board.create_rectangle(column*square_size, row*square_size, (column+1) * square_size, (row+1) * square_size, fill=color, outline="black")

root.mainloop()
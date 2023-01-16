import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("test")

quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack()

board_img = ImageTk.PhotoImage(Image.open("chessboard.jpg"))
board_label = tk.Label(image=board_img)
board_label.pack()

root.mainloop()
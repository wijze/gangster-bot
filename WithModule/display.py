import tkinter as tk

import getpieces
import loadImages

from sys import exit


class Display:
    def __init__(self, board):
        self.root = tk.Tk()
        self.root.title("test")

        self.images = loadImages.loadImages()
        self.colors = ["white", "gray"]
        self.square_size = 60

        self.root.protocol("WM_DELETE_WINDOW", self.exitProgram)

        self.update(board)

    def update(self, board):
        pieces = getpieces.getpieces(board)
        self.drawBoard(pieces)
        self.root.update()

    def drawBoard(self, pieces):
        if hasattr(self,"boardCanvas"): self.boardCanvas.delete("all")
        else: self.boardCanvas = tk.Canvas(self.root, width=8*self.square_size, height=8*self.square_size)
        self.boardCanvas.pack()

        for row in range (8):
            for column in range (8):
                if (((row+column)/2)%1) == 0: color = self.colors[0]
                else: color = self.colors[1]

                self.boardCanvas.create_rectangle(column*self.square_size, row*self.square_size, (column+1) * self.square_size, (row+1) * self.square_size, fill=color, outline="black")

                if(pieces[row][column] != "None"):
                    self.boardCanvas.create_image(((column+0.5)*self.square_size, (row+0.5)*self.square_size),
                                       image=self.images[pieces[row][column]])
    
    def exitProgram(self):
        exit()


# panel = tk.Label(root, image = images["B"])
# panel.pack()

# quit_button = tk.Button(root, text="Quit", command=root.quit)
# quit_button.pack()

from sys import exit
import math
import threading

import tkinter as tk
from chess import square

from loadImages import loadImages

def getpieces(board):
    returnMap = []
    for y in range(8):
        returnMap.append([])
        for x in range(8):
            returnMap[y].append(str(board.piece_at(square(x,7-y))))
    return returnMap

class Window(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True

        self.root = tk.Tk()
        self.root.title("test")
        self.root.protocol("WM_DELETE_WINDOW", self.exitProgram)

        self.colors = ["white", "gray", "orange", "yellow"] # white, black, clicked, marked
        self.square_size = 60
        self.piece_images = loadImages()

        self.marked_squares = []
        self.first_square = None

        self.canvas = tk.Canvas(self.root, width=8* self.square_size, height=8* self.square_size)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.onclick)

        self.loop()

    def loop(self):
        while self.running:
            self.update()
            self.root.update()

    def update(self):
        self.drawBoard()
        # self.draw_pieces(self.board)  to implement in a class with acces to the board
    
    def drawBoard(self):
        for row in range (8):
            for column in range (8):
                if self.first_square==(column,7-row): color = self.colors[2]
                elif (column,7-row) in self.marked_squares: color = self.colors[3]
                elif (((row+column)/2)%1) == 0: color = self.colors[0]
                else: color = self.colors[1]
                self.canvas.create_rectangle(column*self.square_size, row*self.square_size, (column+1) * self.square_size, (row+1) * self.square_size, fill=color, outline="black")

    def draw_pieces(self, board):
        pieces = getpieces(board)
        for row in range (8):
            for column in range (8):
                if(pieces[row][column] != "None"):
                    self.canvas.create_image(((column+0.5)*self.square_size, (row+0.5)*self.square_size),
                                       image=self.piece_images[pieces[row][column]])

    def onclick(self, event):
        square_x = math.floor(event.x / self.square_size)
        square_y = math.floor(event.y / self.square_size)
        return (square_x, 7-square_y)

    def exitProgram(self):
        self.running = False
        exit()
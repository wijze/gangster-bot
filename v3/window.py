import math

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

class Window():
    def __init__(self, user_move_que):
        self.user_move_que = user_move_que

        self.running = True

        self.colors = ["white", "gray", "orange", "yellow"] # white, black, clicked, marked
        self.square_size = 60

        self.marked_squares = []
        self.first_square = None

        self.board = None
        self.first_square = None

        self.root = tk.Tk()
        self.root.title("Chess")
        self.root.protocol("WM_DELETE_WINDOW", self.exitProgram)

        self.piece_images = loadImages()

        self.canvas = tk.Canvas(self.root, width=8* self.square_size, height=8* self.square_size)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.onclick)

    def update(self, new_board=None):
        if not self.running: return
        self.canvas.delete("all")
        if new_board:
            self.board = new_board
        self.drawBoard()
        self.draw_pieces(getpieces(self.board))
        self.root.update()
    
    def drawBoard(self):
        for row in range (8):
            for column in range (8):
                if self.first_square==(column,7-row): color = self.colors[2]
                elif (column,7-row) in self.marked_squares: color = self.colors[3]
                elif (((row+column)/2)%1) == 0: color = self.colors[0]
                else: color = self.colors[1]
                self.canvas.create_rectangle(column*self.square_size, row*self.square_size, (column+1) * self.square_size, (row+1) * self.square_size, fill=color, outline="black")

    def draw_pieces(self, pieces):
        for row in range (8):
            for column in range (8):
                if(pieces[row][column] != "None"):
                    self.canvas.create_image(((column+0.5)*self.square_size, (row+0.5)*self.square_size),
                                       image=self.piece_images[pieces[row][column]])

    def onclick(self, event):
        square_x = math.floor(event.x / self.square_size)
        square_y = math.floor(event.y / self.square_size)
        coordinates = (square_x, 7-square_y)
        if self.first_square:
            self.user_move_que.put_nowait((self.first_square, coordinates))
            self.first_square = None
        else:
            self.first_square = coordinates

    def exitProgram(self):
        self.running = False
        self.root.destroy()
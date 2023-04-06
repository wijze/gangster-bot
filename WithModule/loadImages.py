from PIL import ImageTk, Image
import pathlib

def loadImages():
    return {
        "R":ImageTk.PhotoImage(Image.open(pathlib.Path("../chess_images/wR.png"))),
        "N":ImageTk.PhotoImage(Image.open(pathlib.Path("../chess_images/wN.png"))),
        "B":ImageTk.PhotoImage(Image.open(pathlib.Path("../chess_images/wB.png"))),
        "Q":ImageTk.PhotoImage(Image.open(pathlib.Path("../chess_images/wQ.png"))),
        "K":ImageTk.PhotoImage(Image.open(pathlib.Path("../chess_images/wK.png"))),
        "P":ImageTk.PhotoImage(Image.open(pathlib.Path("../chess_images/wp.png"))),
        "r":ImageTk.PhotoImage(Image.open(pathlib.Path("../chess_images/bR.png"))),
        "n":ImageTk.PhotoImage(Image.open(pathlib.Path("../chess_images/bN.png"))),
        "b":ImageTk.PhotoImage(Image.open(pathlib.Path("../chess_images/bB.png"))),
        "q":ImageTk.PhotoImage(Image.open(pathlib.Path("../chess_images/bQ.png"))),
        "k":ImageTk.PhotoImage(Image.open(pathlib.Path("../chess_images/bK.png"))),
        "p":ImageTk.PhotoImage(Image.open(pathlib.Path("../chess_images/bp.png"))),
    }
from PIL import ImageTk, Image
import os.path

def loadImages():
    script_path = os.path.realpath(__file__)
    script_dir = os.path.dirname(script_path)
    images_dir = os.path.join(script_dir, '..', 'chess_images')

    return {
        "R":ImageTk.PhotoImage(Image.open(os.path.join(images_dir, "wR.png"))),
        "N":ImageTk.PhotoImage(Image.open(os.path.join(images_dir, "wN.png"))),
        "B":ImageTk.PhotoImage(Image.open(os.path.join(images_dir, "wB.png"))),
        "Q":ImageTk.PhotoImage(Image.open(os.path.join(images_dir, "wQ.png"))),
        "K":ImageTk.PhotoImage(Image.open(os.path.join(images_dir, "wK.png"))),
        "P":ImageTk.PhotoImage(Image.open(os.path.join(images_dir, "wp.png"))),
        "r":ImageTk.PhotoImage(Image.open(os.path.join(images_dir, "bR.png"))),
        "n":ImageTk.PhotoImage(Image.open(os.path.join(images_dir, "bN.png"))),
        "b":ImageTk.PhotoImage(Image.open(os.path.join(images_dir, "bB.png"))),
        "q":ImageTk.PhotoImage(Image.open(os.path.join(images_dir, "bQ.png"))),
        "k":ImageTk.PhotoImage(Image.open(os.path.join(images_dir, "bK.png"))),
        "p":ImageTk.PhotoImage(Image.open(os.path.join(images_dir, "bp.png"))),
    }
    
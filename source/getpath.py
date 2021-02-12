from tkinter import filedialog
from tkinter import *

class Path:
    def run():
        root = Tk()
        root.withdraw()
        path = filedialog.askdirectory()
        return path


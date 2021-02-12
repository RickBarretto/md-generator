#Python Code

""" What I want?
+ Name
+ Description
+ Functions, to codeblocks, h1 - h6, quotes and lists.
"""

from help import Help
from app import App
from getpath import Path

class Terminal:
    def run():
        print("Welcome to Mardown - README - generator.\nWhat do you want?\nA) Help\tB) Create")
        input1 = input(">> ")

        # Help system
        if input1 == "a" or input1 == "A":
            Help.run()
        # Application system
        elif input1 == "b" or input1 == "B":
            path = Path.run()
            Save.run(path)
            App.init(path)
            App.run()
        # Error
        else:
            print("[!] Choose the options beetwen A or B!")
            Terminal.run()
        
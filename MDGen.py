#Python Code

""" What I want?
+ Name
+ Description
+ Functions, to codeblocks, h1 - h6, quotes and lists.
"""

from help import Help
from app import App

class Terminal:
    def run():
        print("Welcome to Mardown - README - generator.\nWhat do you want?\nA) Help\tB) Create")
        input1 = input(">> ")
        if input1 == "a" or input1 == "A":
            Terminal.run_help()
        elif input1 == "b" or input1 == "B":
            Terminal.run_app()
        else:
            print("[!] Choose the options beetwen A or B!")
            Terminal.run()

    def run_help():
        pass
    def run_app():
        pass
        
class Help:
    def run():
        with open("help.txt", "r") as f:
            h = f.read()
            print(h)

Help.run()
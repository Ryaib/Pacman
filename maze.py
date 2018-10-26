
class Maze:
    def __init__(self, settings):
        self.settings = settings
        self.list = []
        with open('MAZE.txt', 'r') as f:
            while True:
                self.c = f.read(1)
                if not self.c:
                    print("EoF")
                    break
                else:
                    self.list.append(self.c)

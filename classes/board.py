from random import randint
from cell import Cell


class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[0 for i in range(self.width)] for j in range(self.height)]

    # this function will run the game
    def simGeneration(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c]:
                    self.grid[r][c].update(self.grid, r, c)

    def __str__(self):
        res = ""
        for i in range(self.height):
            for j in range(self.width):
                # iterate through the board
                if self.grid[i][j]:
                    res += str(self.grid[i][j]) + " "
                else:
                    res += "  "
            res += "\n"
        return res

    def init_random(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if randint(0, 1) == 1:
                    self.grid[r][c] = Cell(r, c, self.grid, 1, 10, 1)
                else:
                    self.grid[r][c] = None

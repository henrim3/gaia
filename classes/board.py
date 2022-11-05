from random import randint
from cell import Cell
from food import Food
from copy import deepcopy


class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[0 for i in range(self.width)] for j in range(self.height)]
        self.foodSpots = dict()

    # this function will run the game
    def simGeneration(self):
        grid_copy = deepcopy(self.grid)
        for r in range(len(grid_copy)):
            for c in range(len(grid_copy[0])):
                if grid_copy[r][c]:
                    grid_copy[r][c].update(grid_copy, r, c)
        self.grid = grid_copy

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
                if randint(0, 5) == 1:
                    self.grid[r][c] = Cell(r, c, 1, 10, 1, self.foodSpots)
                elif randint(0, 3) == 1:
                    self.grid[r][c] = Food(r, c, 50)
                    self.foodSpots[(r, c)] = None
                else:
                    self.grid[r][c] = None
                    
    def add_food(self, foodSpots, low, mid, high):
        mid = len(foodSpots / 2)
        if(len(foodSpots) == 2):
            self.foodSpots.insert()
            return
        #split the food into a smaller array
        self.add_food(foodSpots[].start, foodSpots.begin, mid)
        #split the food into a bigger array
        self.add_food(foodSpots[].start, mid + 1, foodSpots.end)

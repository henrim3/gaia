from cell import Cell
from food import Food
from copy import deepcopy
from random import randint

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        self.food_positions = set()
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(None)
            self.grid.append(row)

    def update(self):
        next_grid = deepcopy(self.grid)
        for r in range(self.height):
            for c in range(self.width):
                item = self.grid[r][c]
                item_type = type(item) 
                if item_type == Cell:
                    res = item.update(self.grid, next_grid, self.food_positions)
                    if res:
                        next_grid[r][c] = None
        self.grid = next_grid

    def display(self):
        out_string = ""
        for row in self.grid:
            for val in row:
                if val:
                    out_string += str(val) + " "
                else:
                    out_string += ". "
            out_string += "\n"
        print(out_string)
    def add_cell(self, row, column, food, food_rate, speed):
        self.grid[row][column] = Cell(row, column, food, food_rate, speed)

    def add_food(self, row, column, food):
        self.grid[row][column] = Food(row, column, food)
        self.food_positions.add((row, column))
        
    def add_cell_amount(self,count):
        for _ in range(count):
            row = randint(0, self.height -1)
            col = randint(0, self.width - 1)
            food = randint(45, 65)
            food_rate = randint(1, 5)
            speed = randint(1, 5)
            self.add_cell(row, col, food, food_rate, speed) 

    def add_food_amount(self, count):
        for _ in range(count):
            row = randint(0, self.height - 1)
            col = randint(0, self.width - 1)
            food = randint(40, 60)
            self.add_food(row, col, food)
    
    
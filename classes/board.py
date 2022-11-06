from random import randint
from cell import Cell
from food import Food
from copy import deepcopy


class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[None for i in range(self.width)] for j in range(self.height)]
        self.food_spots = []

    # this function will run the game
    def sim_generation(self):   
        new_grid = [[None for i in range(self.width)] for j in range(self.height)]
        for r in range(self.height):
            for c in range(self.width):
                pos = self.grid[r][c]
                if pos and pos.type == "cell":
                    res = pos.update(self.grid, self.food_spots)
                    if res:
                        new_grid = res
                    else:
                        del new_grid[r][c]
                        del self.grid[r][c]
                        new_grid[r].insert(c, None)
                        self.grid[r].insert(c, None)
    
        self.grid = deepcopy(new_grid)

    def __str__(self):
        res = ""
        for i in range(self.height):
            for j in range(self.width):
                # iterate through the board
                if self.grid[i][j]:
                    res += str(self.grid[i][j])
                else:
                    res += " "
            res += "\n"
        return res

    def add_cell(self, row, col, speed, food, food_rate):
         cell = Cell(row, col, speed, food, food_rate)
         self.grid[row][col] = cell
         return cell

    def add_food(self, row, col):
        self.grid[row][col] = Food(2, row, col)
        self.add_food_spots((row, col))
        # self.add_food_spots(self.food_spots, (row, col), 0, len(self.food_spots) - 1)

    def add_cell_amount(self, amount):
        for _ in range(amount):
            row = randint(0, self.height - 1)
            col = randint(0, self.width - 1)
            self.grid[row][col] = Cell(row, col, 1, 10, 1)

    def add_food_spots(self, pos):
        self.food_spots.append(pos)
        self.food_spots.sort() 

    # def add_food_spots(self, foodSpots, pos, low, high):
    #     mid = (low + high) // 2
    #     if len(foodSpots) <= 2:
    #         self.foodSpots.insert(1, pos)
    #         return
    #     # split the food into an array from mid to end is the coord at mid is bigger than pos
    #     print(len(foodSpots))
    #     if foodSpots[mid] > pos:
    #         self.add_food_spots(foodSpots[mid + 1 : high + 1].start, pos, mid + 1, high)
    #     else:
    #         self.add_food_spots(foodSpots[low : mid + 1], pos, low, mid)

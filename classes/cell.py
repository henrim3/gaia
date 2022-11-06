import sys
from copy import deepcopy

class Cell:
    def __init__(
        self,
        row,
        column,
        speed,
        food,
        food_rate,
    ):
        self.row = row
        self.column = column
        self.speed = speed
        self.food = food
        self.food_rate = food_rate
        self.type = "cell"

    def kill(self, grid):
        grid[self.row][self.column] = None 
        del self

    def get_neighbors(self, grid):
        neighbors = []
        startRow = self.row - 1
        startColumn = self.column - 1
        for i in range(startRow + 3):
            for j in range(startColumn + 3):
                if i == self.row and j == self.column:
                    continue
                if not (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])):
                    neighbors.append(grid[i][j])
        return neighbors
    
    def update(self, grid, food_spots):
        new_grid = deepcopy(grid)
        self.food -= self.food_rate
        if self.food <= 0:
            return
            # print("dead")
            # self.kill(new_grid)
            # return

        neighbors = self.get_neighbors(grid)
        food_neighbors = []
        for neighbor in neighbors:
            if neighbor:
                if neighbor.type == "food":
                    food_neighbors.append(neighbor)

        nearest_food = self.get_nearest_food(food_spots)

        if nearest_food:
            if len(food_neighbors) > 0:
                for food_neighbor in food_neighbors:
                    res = food_neighbor.update(1, food_spots)
                    if type(res) == tuple:
                        print("jose gay")
                        del new_grid[res[1][0], res[1][1]]
                        new_grid.insert(res[1][1], None)
                        self.food += res[0]
                        food_spots.remove((res[1][0], res[1][1]))
                    else:
                        self.food += res
            else:
                self.moveCell(nearest_food[0], nearest_food[1], new_grid)
            return new_grid        

    # def update(self, old_grid, new_grid, row, column, foodSpots):
    #     """
    #     updates a single cell
    #     """ 
    #     # check neighboring cells
    #     self.food -= self.food_rate
    #     neighbors = self.get_neighbors(old_grid)
    #     surrCells = 0
    #     # check type of neighbors
    #     for n in neighbors:
    #         if n:
    #             if n.type == "cell":
    #                 surrCells += 1
    #             elif n.type == "food":
    #                 pass

    #     if self.food <= 0:
    #         self.kill(new_grid, row, column)
    #     # nearest = self.get_nearest_food(
    #     #     foodSpots, (self.row, self.column), 0, len(foodSpots)
    #     # )

    #     nearest = self.get_nearest_food(foodSpots)

    #     self.moveCell(nearest[0], nearest[1], grid)

    def __str__(self):
        return "x"

    def get_nearest_food(self, food_spots):
        min_distance = sys.maxsize
        min_pos = None
        for pos in food_spots:
            distance = abs(pos[0] - self.row) + abs(pos[1] - self.column)
            if distance < min_distance:
                min_distance = distance
                min_pos = pos
        return min_pos

    # def get_nearest_food(self, foodSpots, x, low, high):
    #     mid = (low + high) // 2
    #     if len(foodSpots) <= 2:
    #         return foodSpots[mid]
    #     # split the food into an array from mid to end is the coord at mid is bigger than x
    #     if foodSpots[mid] > x:
    #         self.get_nearest_food(foodSpots[mid + 1 : high + 1].start, x, mid + 1, high)
    #     else:
    #         self.get_nearest_food(foodSpots[low : mid + 1], x, low, mid)

    def moveCell(self, target_row, target_column, grid):
        grid[self.row][self.column] = None
        if self.row != target_row:
            row_diff = target_row - self.row
            if row_diff > 0:
                self.row += 1
            else:
                self.row -= 1
        else:
            col_diff = target_column - self.column
            if col_diff > 0:
                self.column += 1
            else:
                self.column -= 1
        grid[self.row][self.column] = self

    # def moveCell(self, target_row, target_column, grid):
    #     row_diff = abs(self.row - target_row)
    #     col_diff = abs(self.column - target_column)
    #     if row_diff < self.speed and col_diff < self.speed:
    #         if grid[self.row + self.speed][self.column] != None:
    #             offset = 1
    #             while grid[self.row + self.speed + offset][self.column] != None:
    #                 offset += 1
    #             grid[self.row + self.speed + offset][self.column] = self
    #             grid[self.row][self.column] = None
    #     else:
    #         for i in range((self.row - 1) + 3):
    #             for j in range((self.column - 1) + 3):
    #                 if i == self.row and j == self.column:
    #                     continue
    #                 if grid[i][j] != None:
    #                     grid[i][j] = self
    #                     grid[self.row][self.column] = None

    #         pass

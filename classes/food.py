class Food:
    def __init__(
        self,
        currFood: int,
        row:int,
        column:int,
    ):
        self.currFood = currFood
        self.row = row
        self.column = column
        self.type = "food"
    def kill(self, grid:list, row:int, column:int, foodSpots: list):
        grid[row][column] = None
        foodSpots.remove((self.row, self.column))
        del self
    def findFood(self, grid:list):
        pass
    def update(self, grid: list, row: int, column: int, foodRate:int, foodSpots: list):
        foodEaten = self.currFood - foodRate
        if(self.currFood - foodRate <= 0):
            self.kill(grid, row, column)
            return self.currFood
        return foodEaten
    def __str__(self):
        return "f"

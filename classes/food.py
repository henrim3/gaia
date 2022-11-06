class Food:
    def __init__(
        self,
        food,
        row,
        column,
    ):
        self.food = food
        self.row = row
        self.column = column
        self.type = "food"

    def kill(self, grid, foodSpots):
        grid[self.row][self.column] = None
        foodSpots.remove((self.row, self.column))
        del self

    def update(self, food_rate, food_spots):
        self.food -= food_rate
        print(self.food)
        if self.food <= 1:
            food = self.food
            print("running")
            return food, (self.row, self.column)
        return food_rate

    def __str__(self):
        return "f"

class Cell:
    def __init__(
        self,
        row: int,
        column: int,
        speed: float,
        food: float,
        food_rate: float,
    ):
        self.row = row
        self.column = column
        self.speed = speed
        self.food = food
        self.food_rate = food_rate
        self.type = "cell"

    def kill(self, grid: list, row: int, column: int):
        grid[row][column] = None
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

    def update(self, grid: list, row: int, column: int):
        # check neighboring cells
        self.food -= self.food_rate
        neighbors = self.get_neighbors(grid)
        surrCells = 0
        # check type of neighbors
        for n in neighbors:
            if n:
                if n.type == "cell":
                    surrCells += 1
                elif n.type == "food":
                    pass

        if self.food <= 0:
            self.kill(grid, row, column)

    def __str__(self):
        return "x"

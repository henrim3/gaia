class Cell:
    def __init__(
        self,
        row: int,
        column: int,
        grid: list,
        speed: float,
        food: float,
        food_rate: float,
    ):
        self.row = row
        self.column = column
        self.grid = grid
        self.speed = speed
        self.food = food
        self.food_rate = food_rate
        self.type = "cell"

    def kill(self, grid: list, row: int, column: int):
        grid[row][column] = None
        del self

    def get_neighbors(self):
        neighbors = []
        startRow = self.row - 1
        startColumn = self.row - 1
        for i in range(startRow + 3):
            for j in range(startColumn + 3):
                if i == self.row and j == self.column:
                    continue
                if not (
                    i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0])
                ):
                    neighbors.append(self.grid[i][j])
        return neighbors

    def update(self, grid: list, row: int, column: int):
        # check neighboring cells
        self.food -= self.food_rate
        neighbors = self.get_neighbors()
        surrCells = 0
        for n in neighbors:
            if n:
                surrCells += 1
            # if n.type == "food":
            #     pass
            # if n.type == "cell":
            #     surrCells += 1
        if self.food <= 0:
            self.kill(grid, row, column)
        elif surrCells <= 1 or surrCells >= 4:
             self.kill(grid, row, column)

    def __str__(self):
        return "x"

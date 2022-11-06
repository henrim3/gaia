class Food:
    def __init__(self, row, column, food):
        self.row = row
        self.col = column
        self.food = food
        
    def update(self, food_change, next_grid):
        """
        param curr_grid (list(list)): current grid
        param next_grid (list(list)): grid of next generation to be modified
        param cells_set (set(list)): set of positions of cells
        param food_positions (list(tuple)): positions of food (row, column)
        """
        if self.food - food_change <= 0:
            return self.food
        self.food += food_change
        next_grid[self.row][self.col] = self
    
    def __str__(self):
        return "O"

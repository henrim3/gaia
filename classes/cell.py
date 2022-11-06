class Cell:
    def __init__(self, row, column, food, food_rate):
        self.row = row
        self.col = column
        self.food = food
        self.food_rate = food_rate

    def get_neighbors(self, prev_grid):
        """
        param prev_grid (list(list)): grid of previous generation
        returns (list): neighbors of cell
        """
        neighbors = []
        for row in range(self.row - 1, self.row + 2):
            for col in range(self.col - 1, self.col + 2):
                if row >= 0 and row < len(prev_grid) and col >= 0 and col < len(prev_grid[0]):
                    if row == self.row and col == self.col:
                        continue
                    neighbors.append(prev_grid[row][col])
        return neighbors
    
    def get_pos_diff(self, pos1, pos2):
        r1, c1 = pos1
        r2, c2 = pos2
        return abs(r2 - r1) + abs(c2 - c1)

    def nearest_position(self, positions):
        """
        param positions (list(tuple)): positions (row, column)
        returns (tuple): tuple nearest position in set
        """
        curr_pos = (self.row, self.col)
        min_diff = self.get_pos_diff(curr_pos, positions[0])
        near_pos = positions[0]
        for pos in positions:
            diff = self.get_pos_diff(curr_pos, pos)
            if diff < min_diff:
                min_diff = diff
                near_pos = pos
        return near_pos

    def move_towards(self, position):
        """
        param position (tuple): position to move towards (row, column)
        """
        ro

    def update_in_grid(self, prev_grid, next_grid, cells_set):
        """
        param prev_grid (list(list)): grid of previous generation
        param next_grid (list(list)): grid of next generation to be modified
        param cells_set (set(list)): set of positions of cells
        """
        pass
    
    def eat(self, food):
        """
        param food (Food): food object to eat
        """
        pass

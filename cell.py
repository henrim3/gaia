from food import Food

class Cell:
    def __init__(self, row, column, food, food_rate):
        self.row = row
        self.col = column
        self.food = food
        self.food_rate = food_rate

    def get_neighbors(self, curr_grid):
        """
        param curr_grid (list(list)): grid of previous generation
        returns (list): neighbors of cell
        """
        neighbors = []
        for row in range(self.row - 1, self.row + 2):
            for col in range(self.col - 1, self.col + 2):
                if row >= 0 and row < len(curr_grid) and col >= 0 and col < len(curr_grid[0]):
                    if row == self.row and col == self.col:
                        continue
                    neighbors.append(curr_grid[row][col])
        return neighbors

    def get_neighbor_positions(self, position, curr_grid):
        """
        param position (tuple): position (row, col)
        param curr_grid (list(list)): grid of previous generation
        returns (list): neighbor positions of position
        """
        pos_row, pos_col = position
        neighbors = []
        for row in range(pos_row - 1, pos_row + 2):
            for col in range(pos_col - 1, pos_col + 2):
                if row >= 0 and row < len(curr_grid) and col >= 0 and col < len(curr_grid[0]):
                    if row == pos_row and col == pos_col:
                        continue
                    neighbors.append((row, col))
        return neighbors

    def pos_diff(self, pos1, pos2):
        """
        param pos1 (tuple): first position
        para pos2 (tuple): second position
        """
        r1, c1 = pos1
        r2, c2 = pos2
        return abs(r2 - r1) + abs(c2 - c1)

    def get_nearest_position(self, positions):
        """
        param positions (list(tuple)): positions (row, column)
        returns (tuple): tuple nearest position in set
        """
        curr_pos = (self.row, self.col)
        min_diff = self.pos_diff(curr_pos, positions[0])
        near_pos = positions[0]
        for pos in positions:
            diff = self.pos_diff(curr_pos, pos)
            if diff < min_diff:
                min_diff = diff
                near_pos = pos
        return near_pos

    def move_towards(self, position):
        """
        param position (tuple): position to move towards (row, column)
        returns (tuple): new position
        """
        row, col = position
        if self.row != row:
            row_diff = self.row - row
            if row_diff < 0:
                return (self.row - 1, self.col)
            else:
                return (self.row + 1, self.col)
        elif self.col != col:
            col_diff = self.col - col
            if col_diff < 0:
                return (self.row, self.col - 1)
            else:
                return (self.row, self.col + 1)
                
    def update_food(self, curr_grid, next_grid):
        """
        eats food and updates food
        
        param curr_grid (list(list)): current grid
        param next_grid (list(list)): grid of next generation to be modified
        """
        neighbors = self.get_neighbors(curr_grid)
        food_nbrs = []
        for nbr in neighbors:
            if type(nbr) == Food:
                food_nbrs.append(nbr)
        
        if len(food_nbrs) > 0:
            for food_nbr in food_nbrs:
                if food_nbr.food - (1 / len(food_nbrs)) < 0:
                    self.food += food_nbr.food
                    curr_grid[food_nbr.row][food_nbr.col] = None
                    next_grid[food_nbr.row][food_nbr.col] = None
                else:
                    food_nbr.food -= (1 / len(food_nbrs))
                    self.food += (1 / len(food_nbrs))
                    
        self.food -= self.food_rate

    def update(self, curr_grid, next_grid, food_set):
        """
        param curr_grid (list(list)): current grid
        param next_grid (list(list)): grid of next generation to be modified
        param cells_set (set(list)): set of positions of cells
        param food_set (set(tuple)): positions of food (row, column)
        """
        self.update_food(curr_grid, next_grid)
        nearest_food = self.get_nearest_position(food_set)
        next_pos = self.move_towards(nearest_food)
        # next_grid[self.row][self.col].append(self)
        next_grid[self.row][self.col] = None
        self.row, self.col = next_pos
        next_grid[self.row][self.col] = self
        
    def __str__(self):
        return "x"

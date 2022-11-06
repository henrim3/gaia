from food import Food
from family import Family
from random import randint


class Cell:
    def __init__(
        self,
        row,
        column,
        food,
        food_rate,
        speed,
        family=None,
        can_reproduce=True,
    ):
        self.row = row
        self.col = column
        self.food = food
        self.food_rate = food_rate
        self.speed = speed
        if family:
            self.family = family
        else:
            self.family = Family(set())
        self.can_reproduce = True

    def get_neighbors(self, curr_grid):
        """
        param curr_grid (list(list)): grid of previous generation
        returns (list): neighbors of cell
        """
        neighbors = []
        for row in range(self.row - 1, self.row + 2):
            for col in range(self.col - 1, self.col + 2):
                if (
                    row >= 0
                    and row < len(curr_grid)
                    and col >= 0
                    and col < len(curr_grid[0])
                ):
                    if row == self.row and col == self.col:
                        continue
                    neighbors.append(curr_grid[row][col])
        return neighbors

    def get_neighbor_positions(self, position, grid):
        """
        param position (tuple): position (row, col)
        param grid (list(list)): grid
        returns (list): neighbor positions of position
        """
        pos_row, pos_col = position
        neighbors = []
        for row in range(pos_row - 1, pos_row + 2):
            for col in range(pos_col - 1, pos_col + 2):
                if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
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
        if len(positions) == 0:
            return
        curr_pos = (self.row, self.col)
        min_diff = self.pos_diff(curr_pos, positions[0])
        near_pos = positions[0]
        for pos in positions:
            diff = self.pos_diff(curr_pos, pos)
            if diff < min_diff:
                min_diff = diff
                near_pos = pos
        return near_pos

    def get_move_dimension(self, start, end, diff):
        if diff < self.speed:
            return end
        if start < end:
            return start + self.speed
        elif start > end:
            return start - self.speed
        return start

    def move_towards(self, position, next_grid):
        """
        param position (tuple): position to move towards (row, column)
        returns (tuple): new position
        """
        row, col = position

        row_diff = abs(self.row - row)
        col_diff = abs(self.col - col)

        if row_diff < 2 and col_diff < 2:
            return self.row, self.col

        end_row = int(self.get_move_dimension(self.row, row, row_diff))
        end_col = int(self.get_move_dimension(self.col, col, col_diff))

        if not next_grid[end_row][end_col]:
            return end_row, end_col

        empty_nbrs = []
        for nbr_pos in self.get_neighbor_positions((self.row, self.col), next_grid):
            nbr_row, nbr_col = nbr_pos
            if not next_grid[nbr_row][nbr_col]:
                empty_nbrs.append((nbr_row, nbr_col))

        if len(empty_nbrs) > 0:
            return empty_nbrs[randint(0, len(empty_nbrs) - 1)]

        return self.row, self.col

    def update_food(self, curr_grid, next_grid, food_positions):
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
                res = food_nbr.update(-1 / len(food_nbrs), next_grid)
                if res:
                    self.food += res
                    food_positions.remove((food_nbr.row, food_nbr.col))
                    curr_grid[food_nbr.row][food_nbr.col] = None
                    next_grid[food_nbr.row][food_nbr.col] = None
                else:
                    self.food += 1 / len(food_nbrs)

        self.food -= self.food_rate
        if self.food <= 0:
            return 1

    def update(self, curr_grid, next_grid, food_positions):
        """

        param curr_grid (list(list)): current grid
        param next_grid (list(list)): grid of next generation to be modified
        param cells_set (set(list)): set of positions of cells
        param food_set (list(tuple)): positions of food (row, column)
        """
        res = self.update_food(curr_grid, next_grid, food_positions)
        if res:
            return 1
        nearest_food = self.get_nearest_position(sorted(food_positions))
        next_pos = self.row, self.col
        if nearest_food:
            next_pos = self.move_towards(nearest_food, next_grid)
        # next_grid[self.row][self.col].append(self)
        next_grid[self.row][self.col] = None
        self.row, self.col = next_pos
        next_grid[self.row][self.col] = self

    def __str__(self):
        return self.family.character

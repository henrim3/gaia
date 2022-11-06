from cell import Cell
from food import Food
from copy import deepcopy
from random import randint, random
from family import Family

# VALUES
food_difference = 5
food_cost = 12  # per parent

reproduce_odds = 2 / 3
speed_trait_odds = 1 / 3
trait_passed_odds = 2 / 3

speed_trait_speed = 4


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        self.food_positions = set()
        self.families = set()
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(None)
            self.grid.append(row)

    def update(self):
        next_grid = deepcopy(self.grid)
        for r in range(self.height):
            for c in range(self.width):
                item = self.grid[r][c]
                item_type = type(item)
                if item_type == Cell:
                    res = item.update(self.grid, next_grid, self.food_positions)
                    if res:
                        next_grid[r][c] = None
        self.grid = next_grid

    def __str__(self):
        out_string = ""
        for row in self.grid:
            for val in row:
                if val:
                    out_string += str(val) + " "
                else:
                    out_string += ". "
            out_string += "\n"
        return out_string

    def add_cell(self, row, column, food, food_rate, speed):
        self.grid[row][column] = Cell(row, column, food, food_rate, speed)

    def add_food(self, row, column, food):
        self.grid[row][column] = Food(row, column, food)
        self.food_positions.add((row, column))

    def add_cell_amount(self, count, food_range, food_rate_range, speed_range):
        for _ in range(count):
            row = randint(0, self.height - 1)
            col = randint(0, self.width - 1)
            food = randint(food_range[0], food_range[1])
            food_rate = randint(food_rate_range[0], food_rate_range[1])
            speed = randint(speed_range[0], speed_range[1])
            self.add_cell(row, col, food, food_rate, speed)

    def add_food_amount(self, count, food_range):
        for _ in range(count):
            row = randint(0, self.height - 1)
            col = randint(0, self.width - 1)
            food = randint(food_range[0], food_range[1])
            self.add_food(row, col, food)

    def avg(self, n1, n2):
        return (n1 + n2) / 2

    def fight(self, cell1, cell2, next_grid):
        if cell1.food < cell2.food:
            next_grid[cell1.row][cell1.col] = None
        elif cell1.food > cell2.food:
            next_grid[cell2.row][cell2.col] = None

    def reproduce(self, cell1, cell2, next_grid):
        if random() > reproduce_odds:
            return
        parent_nbrs = cell1.get_neighbor_positions(
            (cell1.row, cell1.col), self.grid
        ) + cell2.get_neighbor_positions((cell2.row, cell2.col), self.grid)
        for nbr in parent_nbrs:
            if not self.grid[nbr[0]][nbr[1]]:
                baby_row = nbr[0]
                baby_col = nbr[1]
                break
        else:
            next_grid[cell1.row][cell1.col] = None
            next_grid[cell2.row][cell2.col] = None
            return
        cell1.food -= food_cost
        cell2.food -= food_cost
        speed_trait = random() < speed_trait_odds
        if len(cell1.family.members) > len(cell2.family.members):
            new_character = cell1.family.character
        else:
            new_character = cell2.family.character
        new_family = Family(cell1.family.members | cell2.family.members, character=new_character)
        for member in new_family.members:
            member.family = new_family
        baby = Cell(
            baby_row,
            baby_col,
            food_cost * 2,
            self.avg(cell1.food_rate, cell2.food_rate),
            self.avg(cell1.speed, cell2.speed),
            new_family,
        )
        if speed_trait:
            baby.speed = speed_trait_speed
        next_grid[baby_row][baby_col] = baby
        new_family.members.add(baby)

    def post_update(self):
        next_grid = deepcopy(self.grid)
        for r in range(self.height):
            for c in range(self.width):
                item = self.grid[r][c]
                item_type = type(item)
                if item_type == Cell:
                    for n in item.get_neighbors(self.grid):
                        if type(n) == Cell:
                            if abs(n.food - item.food) <= food_difference:
                                pass
                                self.reproduce(item, n, next_grid)
                            else:
                                self.fight(item, n, next_grid)

        self.grid = next_grid

    def sim_generation(self):
        self.update()
        self.post_update()

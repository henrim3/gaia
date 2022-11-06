from cell import Cell
class Swarm:
    def __init__(
        self,
        total_food,
        food_required,
        members
      ):
        self.total_food = total_food
        self.members = members
        self.food_required = food_required

    def reproduce(self, grid, row, column):
      if(self.food_required < self.total_food):
        start_row = row - 1
        start_column = column - 1
        for i in range (start_row + 3):
          for j in range (start_column + 3):
            if(i < 0 or j < 0 or j > len(grid[0]) or i > len(grid[0])):
              continue
            elif(grid[i][j] == None):
              grid[i][j] = Cell(i, j, 1, 1, 1, [])

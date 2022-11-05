from cell import Cell
class Swarm:
    def __init__(
        self,
        totalFood: int,
        foodRequired: int,
        familyMembers: list
      ):
        self.totalFood = totalFood
        self.familyMembers = familyMembers
        self.foodRequired = foodRequired

    def reproduce(self, grid, row, column):
      if(self.foodRequired < self.totalFood):
        startRow = row - 1
        startColumn = column - 1
        for i in range (startRow + 3):
          for j in range (startColumn + 3):
            if(i < 0 or j < 0 or j > len(grid[0]) or i > len(grid[0])):
              continue
            elif(grid[i][j] == None):
              grid[i][j] = Cell(i, j, 1, 1, 1, [])





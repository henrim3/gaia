class Cell:
  food = 2
  def killCell(cells, height, width):
    cells[height][width] = 0
  def simulate(cells, height, width):
    #check neighboring cells
    surrLivingCells = 0
    surrLivingCells += cells[height - 1][width - 1]
    surrLivingCells += cells[height - 1][width]
    surrLivingCells += cells[height - 1][width + 1]
    surrLivingCells += cells[height][width - 1]
    surrLivingCells += cells[height][width + 1]
    surrLivingCells += cells[height + 1][width - 1]
    surrLivingCells += cells[height + 1][width]
    surrLivingCells += cells[height + 1][width + 1]
    if(surrLivingCells >= 4 or surrLivingCells <= 1):
      killCell(cells, height, width)
      return
    #subtract food from this cell
    food -= 1
    if(food == 0):
      killCell(cells, height, width)
      return

    

class Board:
  height = 0
  width = 0
  cells = [[0 for i in range(width)] for j in range(height)]
  #this function will run the game
  def simulateBoard():
    
    for i in range(height):
      for j in range(width):
        #iterate through the board
        if(cells[i][j] != 0):
          #if a cell is not equal to zero, then we know that it is something that is not dead
          cells[i][j].simulate(cells, i, j)
          


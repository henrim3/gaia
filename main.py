import sys
sys.path.append("./classes")
from board import Board
from cell import Cell
from time import sleep

board = Board(20, 20)

board.init_random()

print(board)
print(sorted(board.foodSpots))
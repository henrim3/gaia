import sys

sys.path.append("./classes")
from board import Board
from cell import Cell
from time import sleep

b = Board(10, 10)
# b.add_cell_amount(5)
c1 = b.add_cell(4, 0, 1, 10, 1)
# c2 = b.add_cell(0, 5, 1, 10, 1)
b.add_food(5, 3)
b.add_food(5, 6)

while True:
    print(b)
    b.sim_generation()
    sleep(1)

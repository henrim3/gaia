from classes from board import Board
from classes\cell import Cell
from time import sleep

board = Board(20, 20)

board.init_random()

while True:
    print(board)
    board.simGeneration()
    sleep(1)

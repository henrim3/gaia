from cell import Cell     
from map import Map
from food import Food
from time import sleep
from copy import deepcopy

l = [(5,5)]
m = Map(50, 50)
m.add_cell_amount(50)
m.add_food_amount(10)

i = 1
while True:
    m.display()
    m.update()
    print()
    i += 1
    sleep(1)

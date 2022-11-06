from map import Map
from time import sleep

m = Map(70, 70)
m.add_cell_amount(20, (20, 20), (1, 2), (1, 2))
m.add_food_amount(20, (20, 30))

while True:
    m.display()
    m.sim_generation()
    m.add_food_amount(1, (20, 30))
    print()
    sleep(1)

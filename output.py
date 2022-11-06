from map import Map

outfile = open("output.txt", "w")

m = Map(50, 50)
m.add_cell_amount(150, (20, 20), (1, 2), (1, 2))
m.add_food_amount(20, (20, 30))

max_generations = 20

for gen in range(max_generations + 1):
    print("Output in progress... ({}/{})".format(gen, max_generations))
    m.sim_generation()
    m.add_food_amount(1, (20, 30))
    outfile.write(str(m) + "\n")

outfile.close()

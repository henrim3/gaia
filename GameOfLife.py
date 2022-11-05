import pygame
import sys
from time import sleep
import random

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# THINGS TO CHANGE
WIDTH = 1920
HEIGHT = 1080
cell_width = 20  # width of each cell in pixels
live_color = GREEN  # color of live cells
dead_color = WHITE  # color of dead cells
generations = -1  # -1 for infinite
delay = 0  # delay between generations
rand = True  # if true, cells will be random
chance = 2  # possibility that cell is live to start is 1/chance

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")

rows = HEIGHT // cell_width
cols = WIDTH // cell_width
grid0 = []
grid1 = []

current_grid = grid0
next_grid = grid1

current_grid_num = 0

sim_running = False
clicked = False


class Cell:
    def __init__(self, row, col, width):
        self.x = col * width
        self.y = row * width
        self.row = row
        self.col = col
        self.width = width
        self.color = WHITE
        self.neighbors = []

    def set_live(self):
        self.color = live_color
        self.draw()

    def set_dead(self):
        self.color = dead_color
        self.draw()

    def is_live(self):
        return self.color == live_color

    def is_dead(self):
        return self.color == dead_color

    def update_neighbors(self):
        self.neighbors = []

        up = self.row - 1 >= 0
        down = self.row + 1 < len(current_grid)
        left = self.col - 1 >= 0
        right = self.col + 1 < len(current_grid[0])

        if up and left:
            self.neighbors.append(current_grid[self.row - 1][self.col - 1])

        if up:
            self.neighbors.append(current_grid[self.row - 1][self.col])

        if up and right:
            self.neighbors.append(current_grid[self.row - 1][self.col + 1])

        if left:
            self.neighbors.append(current_grid[self.row][self.col - 1])

        if right:
            self.neighbors.append(current_grid[self.row][self.col + 1])

        if down and left:
            self.neighbors.append(current_grid[self.row + 1][self.col - 1])

        if down:
            self.neighbors.append(current_grid[self.row + 1][self.col])

        if down and right:
            self.neighbors.append(current_grid[self.row + 1][self.col + 1])

    def get_live_neighbors(self):
        live = 0
        self.update_neighbors()
        for cell in self.neighbors:
            if cell.is_live():
                live += 1

        return live

    def draw(self):
        pygame.draw.rect(WIN, self.color, (int(self.x), int(self.y), int(self.width), int(self.width)))


def get_clicked_pos(pos):
    x, y = pos
    row = y // (HEIGHT // rows)
    col = x // (WIDTH // cols)
    return row, col


def check_inputs():
    global clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            row, col = get_clicked_pos(pos)
            cell = current_grid[row][col]
            if clicked:
                cell.set_live()
            else:
                if cell.is_dead():
                    cell.set_live()
                else:
                    cell.set_dead()
            update(current_grid)
            clicked = True
        else:
            clicked = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not sim_running:
                run_sim(generations)


def update(grid):
    for row in grid:
        for cell in row:
            cell.draw()

    pygame.display.update()


def make_grid(rndm):
    for i in range(rows):
        grid0.append([])
        grid1.append([])
        for j in range(cols):
            cell = Cell(i, j, cell_width)
            cell2 = Cell(i, j, cell_width)
            if rndm:
                r = random.randint(0, chance - 1)
                if r == 1:
                    cell.set_live()
            grid0[i].append(cell)
            grid1[i].append(cell2)


def swap_grids():
    global current_grid_num
    global current_grid
    global next_grid
    current_grid_num = (current_grid_num + 1) % 2
    if current_grid_num == 0:
        current_grid = grid0
        next_grid = grid1
    else:
        current_grid = grid1
        next_grid = grid0


def run_gen():
    for row in range(rows):
        for col in range(cols):
            check_inputs()
            current_cell = current_grid[row][col]
            next_cell = next_grid[row][col]
            live = current_cell.get_live_neighbors()
            if current_cell.is_live():
                next_cell.set_live()
                if live < 2 or live > 3:
                    next_cell.set_dead()
            else:
                next_cell.set_dead()
                if live == 3:
                    next_cell.set_live()
    update(next_grid)
    swap_grids()
    sleep(delay)


def run_sim(gens):
    global sim_running
    sim_running = True
    if gens == -1:
        while True:
            run_gen()
    else:
        for i in range(gens):
            run_gen()
    sim_running = False


make_grid(rand)
update(current_grid)

while True:
    check_inputs()
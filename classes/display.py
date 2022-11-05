import pygame
import sys

BLACK = (200, 200, 200)
WHITE = (50, 50, 50)
WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280
GREEN = (0,255,0)

def display():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

cord = (100,200)

def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            if (x,y) == cord:
                #cell = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.circle(SCREEN, GREEN, (x,y), blockSize/2)
            # else:
            #     rect = pygame.Rect(x, y, blockSize, blockSize)
            #     pygame.draw.circle(SCREEN, WHITE, (x,y), 1)

display()

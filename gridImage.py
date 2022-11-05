import pygame
import sys

background = (0, 0, 0)
lines = (50, 50, 50)
cells = (255,0,0)
WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280
gridW = 500
gridH = 500
GREEN = (0,255,0)
cord = (0,0)

def display(gridW,gridH,background):
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((gridW, gridH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(background)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()



def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, gridW, blockSize):
        for y in range(0, gridH, blockSize):
            if (x,y) == cord:
                #cell = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.circle(SCREEN, GREEN, (x+10,y+10), blockSize/2)
            else:
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.circle(SCREEN, (100,100,100), (x+10,y+10), 1)

display(gridW,gridH,background)


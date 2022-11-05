import numpy
import pygame

gridarray = numpy.random.randint(3, size=(20, 20))
print(gridarray)

colour0=(120,250,90)
colour1=(250,90,120)
colour2=(255,255,255)

(width,height)=(300,300)

screen = pygame.pixelcopy.make_surface(gridarray)
pygame.display.flip()
screen.fill(colour2)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

'''
Car racing game 
'''
import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((300, 300))
BLACK = (0, 0, 0)
# game loop begins
while True:
    # events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # data changes
    pygame.draw.circle(DISPLAYSURF, BLACK, (200, 50), 30)

    # update the display
    pygame.display.update()


'''
Car racing game 
'''
import pygame, sys
from pygame.locals import *
import random

pygame.init()

# frames per second
FPS = 60
clock = pygame.time.Clock()

# set up color variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE = (0, 0, 255)

# setup 300x300 display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# classes
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# game loop begins
while True:
    # events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # data changes

    # update the display
    pygame.display.update()

    # control FPS
    clock.tick(FPS)

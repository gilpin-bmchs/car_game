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

# setup 400x600 display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# classes
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()

# game loop begins
while True:
    # events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # data changes
    P1.update()
    E1.move()

    # update the display
    pygame.display.update()

    # control FPS
    clock.tick(FPS)

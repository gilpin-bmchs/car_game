'''
Car racing game 
'''
import pygame, sys
from pygame.locals import *
import random, time

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

# Other variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5

# Create a white screen
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
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    # def draw(self, surface):
    #     surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[K_UP]:
        #     self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        #     self.rect.move_ip(0,5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    # def draw(self, surface):
    #     surface.blit(self.image, self.rect)

# Creating player and enemy objects
P1 = Player()
E1 = Enemy()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(E1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
print(pygame.USEREVENT)
pygame.time.set_timer(INC_SPEED, 1000)

# game loop begins
while True:

    # Cycle through all events occuring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 2

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Refresh the screen
    DISPLAYSURF.fill(WHITE)
    
    # Moves and redraws all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between player and enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(RED)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # update the display
    pygame.display.update()

    # control FPS
    clock.tick(FPS)

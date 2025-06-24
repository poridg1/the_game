# imports n stuff
import pygame
from pygame.locals import *
import sys 
import random
import time

FPS = 60
FramePerSec = pygame.time.Clock()

# Colors 
BLACK = (0, 0, 0)           # Black
WHITE = (255, 255, 255)     # White
GREY = (128, 128, 128)     # Grey
RED = (255, 0, 0)         # Red\
GREEN = (0, 255, 0)

# Initializing 
pygame.init()

# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# game variables
SPEED = 5
INC_TIME = 3 # In seconds


DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Cars")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0)

    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self):
        DISPLAYSURF.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self):
        DISPLAYSURF.blit(self.image, self.rect)        

P1 = Player()
E1 = Enemy()

# Creating Sprite Groups 
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, INC_TIME*1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 2

        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.fill(WHITE)

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
        entity.draw()

    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(RED)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()


    pygame.display.update() 
    FramePerSec.tick(FPS)



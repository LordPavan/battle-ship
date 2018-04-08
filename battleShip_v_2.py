# Battle Ship with Enemy Sprite
import os
import random

import pygame

# Settings
WIDTH = 400
HEIGHT = 600
FPS = 60

# set-up assets and graphics
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# Colors
WHITE = (233, 233, 233)
BLACK = (0, 0, 0)
RED = (233, 0, 0)
GREEN = (0, 233, 0)
BLUE = (0, 0, 233)
YELLOW = (233, 233, 0)
CYAN = (0, 233, 233)
MAGENTA = (233, 0, 0)

# pygame initialize and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Enemy")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    # Sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((55, 34))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        # check key is pressed by the user
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.speedx = 5
        if keystate[pygame.K_UP]:
            self.speedy = 5
        if keystate[pygame.K_DOWN]:
            self.speedy = -5
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speedx = -5
        # update sprite location
        self.rect.x += self.speedx
        self.rect.y -= self.speedy

        # check edge
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Mob(pygame.sprite.Sprite):
    # sprite for the Enemy or Mob


    # Sprite Groups
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game-loop
running = True
while running:
    # check loop running at right speed
    clock.tick(FPS)
    # Process input(events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()
    # draw
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything flip the display
    pygame.display.flip()
pygame.quit()

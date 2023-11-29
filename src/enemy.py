import pygame
import random
from pygame.locals import *

class Enemy:
    def __init__(self, screen_width, screen_height):
        self.sprites = []
        for i in range(0, 16):
            self.sprites.append(pygame.image.load('src/assets/images/enemy/skeleton-move_' + str(i) + '.png'))

        self.current_sprite = 0
        self.original_image = self.sprites[self.current_sprite]

        self.image = self.original_image
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect = self.image.get_rect(topright=(120, 120))

        self.rect.x = random.randint(screen_width, screen_width + 100)
        self.rect.y = random.randint(0, screen_height - 30)

        self.speed = random.randint(2, 5)

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.hitted = False

    def update(self):
        self.image = pygame.transform.rotate(self.original_image, 180)
        self.image = pygame.transform.scale(self.image, (159, 140))
        self.update_sprite()

        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = random.randint(self.screen_width, self.screen_width + 100)
            self.rect.y = random.randint(0, self.screen_height - 30)
            self.hitted = False

    def update_sprite(self):
        self.current_sprite += 0.5

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.original_image = self.sprites[int(self.current_sprite)]

    def generate_enemys(self):
        enemys = []
        for i in range(0, 5):
            enemys.append(Enemy(self.screen_width, self.screen_height))

        return enemys

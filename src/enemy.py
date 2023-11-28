import math
import pygame
import random
from pygame.locals import *

class Enemy:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(screen_width, screen_width + 100)
        self.rect.y = random.randint(0, screen_height - 30)

        self.speed = random.randint(10, 12)

        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = random.randint(self.screen_width, self.screen_width + 100)
            self.rect.y = random.randint(0, self.screen_height - 30)

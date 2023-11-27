import pygame
import math

class Bullet:

    bullet_image = pygame.image.load('assets/images/bullet_sprite_2.png')

    def __init__(self, pos, angle):
        self.image = Bullet.bullet_image
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)
        self.speed = 15
        self.angle = angle
        self.dx = self.speed * math.cos(math.radians(angle))
        self.dy = self.speed * math.sin(math.radians(angle))

    def update(self, width, height):
        self.pos.x += self.dx
        self.pos.y += self.dy
        self.rect.center = self.pos

        if (self.pos.x < 0 or self.pos.x > width or
                self.pos.y < 0 or self.pos.y > height):
            return self.pos.x < 0 or self.pos.x > width or self.pos.y < 0 or self.pos.y > height

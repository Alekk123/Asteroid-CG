import pygame
import math

class Player:
    def __init__(self, pos, width, height):
        self.original_image = pygame.image.load('assets/images/player_sprite.png')
        self.original_image = pygame.transform.scale(self.original_image, (129, 110))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)
        self.speed = 5
        self.health = 100
        self.ammo = [30, 90]  # Representa balas no carregador e balas totais, respectivamente.
        self.money = 0
        self.width = width
        self.height = height
        self.count_steps = 0

        # pygame.mixer.init()
        # self.steps = pygame.mixer.Sound('music/steps_player.wav')

    def update(self):
        self.rotate()
        self.move()

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - self.pos.y, mouse_x - self.pos.x)
        angle = math.degrees(angle)
        self.image = pygame.transform.rotate(self.original_image, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self):
        # pygame.mixer.music.load('music/steps_player.wav')
        # pygame.mixer.music.play(-1)

        if self.pos.x < 20:
            self.pos.x = 20
        elif self.pos.x > 1580:
            self.pos.x = 1580

        if self.pos.y < 20:
            self.pos.y = 20
        elif self.pos.y > 880:
            self.pos.y = 880

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_a]:
            dx = -self.speed
        if keys[pygame.K_d]:
            dx = self.speed
        if keys[pygame.K_w]:
            dy = -self.speed
        if keys[pygame.K_s]:
            dy = self.speed

        self.pos.x += dx
        self.pos.y += dy
        self.rect.center = self.pos
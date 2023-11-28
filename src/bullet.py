import pygame
import math

class Bullet:
    bullet_image = pygame.image.load('assets/images/bullet_sprite_2.png')

    def __init__(self, pos, angle, offset):
        self.original_image = Bullet.bullet_image
        self.angle = math.degrees(angle)  # Convertendo para graus para a rotação da imagem
        # Rotaciona a imagem da bala para corresponder ao ângulo de disparo
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        # Aplica o offset para a posição inicial da bala
        self.pos = pos + pygame.math.Vector2(offset, 0).rotate(-self.angle)
        self.rect = self.image.get_rect(center=self.pos)
        self.speed = 30
        # A direção da bala é calculada com base no ângulo em radianos
        self.dx = self.speed * math.cos(angle)
        self.dy = self.speed * math.sin(angle)

    def update(self, width, height):
        self.pos.x += self.dx
        self.pos.y += self.dy
        self.rect.center = self.pos

        # Verifica se a bala saiu dos limites da tela
        return (self.pos.x < 0 or self.pos.x > width or
                self.pos.y < 0 or self.pos.y > height)
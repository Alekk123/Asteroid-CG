import pygame
import math
from settings import *
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, group):
        super().__init__(group)

        # general setup
        self.original_image = pygame.image.load('assets/images/player_sprite.png').convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        self.health = 100

        # movement attributes
        self.direction = pygame.math.Vector2()

        # Inicialização de munição atualizada para ter dois valores: munição no carregador e total
        self.ammo = [30, 90]  # Representa balas no carregador e balas totais, respectivamente.
        self.money = 0
        self.width = width
        self.height = height
        self.count_steps = 0

        self.bullets = []

        # pygame.mixer.init()
        # self.steps = pygame.mixer.Sound('music/steps_player.wav')

    def update(self, dt):
        self.rotate()
        self.input()
        self.move(dt)

    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - self.pos.y, mouse_x - self.pos.x)
        angle = math.degrees(angle)
        self.image = pygame.transform.rotate(self.original_image, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def input(self):
        keys = pygame.key.get_pressed()

        # teclas de movimentacao
        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def move(self, dt):
        # pygame.mixer.music.load('music/steps_player.wav')
        # pygame.mixer.music.play(-1)

        # limitando o movimento do usuário
        # verticalmente
        if self.pos.x < 20:
            self.pos.x = 20
        elif self.pos.x > SCREEN_WIDTH:
            self.pos.x = SCREEN_WIDTH
        # horizontalmente
        if self.pos.y < 20:
            self.pos.y = 20
        elif self.pos.y > SCREEN_HEIGHT:
            self.pos.y = SCREEN_HEIGHT

        # normalizing a vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # movimento horizontal
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        # movimento vertical
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

        # self.pos.x += dx
        # self.pos.y += dy
        # self.rect.center = self.pos

    # Método para disparar uma bala
    def shoot(self):
        if self.ammo[0] > 0:
            self.ammo[0] -= 1  # Diminui uma bala do carregador
            # Adicione aqui a lógica para criar a bala e adicionar à lista de sprites, por exemplo
            print("Disparo!")  # Placeholder para o som de disparo
        else:
            # Aqui você pode querer tocar um som de clique ou similar
            print("Sem munição no carregador!")  # Placeholder

    # Método para recarregar a arma
    def reload(self):
        if self.ammo[1] > 0:
            bullets_to_reload = 30 - self.ammo[0]
            if self.ammo[1] >= bullets_to_reload:
                self.ammo[1] -= bullets_to_reload
                self.ammo[0] = 30
            else:
                self.ammo[0] += self.ammo[1]
                self.ammo[1] = 0
            # Adicione aqui a lógica para tocar o som de recarga, por exemplo
            print("Recarregando...")  # Placeholder
        else:
            # Aqui você pode querer informar o jogador que não há munição reserva
            print("Sem munição reserva!")  # Placeholder

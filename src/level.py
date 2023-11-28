import pygame
from enemy import Enemy
from player import Player
from settings import *
from sprites import Generic
from hud import HUD


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        # self.all_sprites = pygame.sprite.Group()
        self.all_sprites = GameGroup()

        self.setup()

    def setup(self):
        Generic(
            pos=(0, 0),
            surf=pygame.image.load('assets/images/mapa_rua.png').convert_alpha(),
            groups=self.all_sprites)
        self.player = Player((15, 360), SCREEN_WIDTH, SCREEN_HEIGHT, self.all_sprites)
        self.enemy = Enemy((640, 360), self.all_sprites, self.player)
        self.hud = HUD()


    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.custom_draw()
        self.all_sprites.update(dt)
        self.hud.draw(screen=self.display_surface,
                      health=self.player.health,
                      shield=100,
                      ammo=self.player.ammo,
                      money=self.player.money)
        # self.monster.run()
        # print("Hello")


class GameGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def custom_draw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)

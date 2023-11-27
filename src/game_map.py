import pygame

class GameMap:
    def __init__(self, path, screen_dimensions):
        self.map_image = pygame.image.load(path)
        self.width, self.height = screen_dimensions
        self.map_image = pygame.transform.scale(self.map_image, (self.width, self.height))

    def draw(self, screen):
        screen.blit(self.map_image, (0, 0))
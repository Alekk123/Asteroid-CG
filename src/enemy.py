import math
import pygame
from settings import *
from pygame.locals import *
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group, player):
        super().__init__(group)

        self.target = player

        self.image = pygame.Surface((32, 64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=pos)

        self.original_image = self.load_image('assets/images/vortigaunt.png')
        self.original_image = pygame.transform.scale(self.original_image, (ENEMY_WIDTH, ENEMY_HEIGHT))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        self.health = 100

    def load_image(self, path):
        # O convert() é usado para converter para o pygame e tem o objetivo de melhorar a perfomance
        img = pygame.image.load(path).convert_alpha()

        # set_colorkey() vai transformar a cor que você passou no argumento em transparente
        img.set_colorkey((255, 0, 255))
        return img

    def run(self):
        self.move_towards_player2(self.target)

    def move_towards_player(self, player):
        # Find direction vector (dx, dy) between enemy and player.
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    # Same thing using only pygame utilities
    def move_towards_player2(self, player):
        # Find direction vector (dx, dy) between enemy and player.
        dirvect = pygame.math.Vector2(player.rect.x - self.rect.x,
                                      player.rect.y - self.rect.y)
        dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length(self.speed)
        self.rect.move_ip(dirvect)


# class Enemy(pygame.sprite.Sprite):
#     def __init__(self, name, position, group, player):
#         super().__init__(group)
#         self.alive = True
#         self.position = pygame.math.Vector2(position)
#         self.direction_index = random.randint(0, 3)
#         self.steps = random.randint(3, 6) * TILESIZE
#         self.name = name
#
#         self.player = player
#
#         enemy_info = monster_data[self.name]
#         self.health = enemy_info["health"]
#         self.roaming_speed = enemy_info["roaming_speed"]
#         self.hunting_speed = random.choice(enemy_info["hunting_speed"])
#         self.image_scale = enemy_info["image_scale"]
#         self.image = enemy_info["image"].convert_alpha()
#         self.image = pygame.transform.rotozoom(self.image, 0, self.image_scale)
#         self.animation_speed = enemy_info["animation_speed"]
#         self.roam_animation_speed = enemy_info["roam_animation_speed"]
#         self.death_animation_speed = enemy_info["death_animation_speed"]
#         self.notice_radius = enemy_info["notice_radius"]
#         self.attack_damage = enemy_info["attack_damage"]
#         self.import_graphics(name)
#
#         self.current_index = 0
#
#         self.image.set_colorkey((0, 0, 0))
#         # self.base_zombie_image = self.image
#
#         self.rect = self.image.get_rect()
#         self.rect.center = position
#
#         self.hitbox_rect = enemy_info["hitbox_rect"]
#         self.base_zombie_rect = self.hitbox_rect.copy()
#         self.base_zombie_rect.center = self.rect.center
#
#         self.velocity = pygame.math.Vector2()
#         self.direction = pygame.math.Vector2()
#         self.direction_list = [(1, 1), (1, -1), (-1, 1),
#                                (-1, -1)]  # [(-1, 0), (1, 0), (0, -1), (0, 1), (1,1), (1,-1), (-1,1), (-1,-1)]
#
#         self.collide = False
#
#         self.coin_dropped = False
#
#     # def check_alive(self):  # checks if enemy dies
#     #     if self.health <= 0:
#     #         self.alive = False
#     #         if self.name == "necromancer":
#     #             necromancer_death_sound.play()
#     #             game_stats["necromancer_death_count"] += 1
#     #         if self.name == "nightborne":
#     #             nightborne_death_sound.play()
#     #             game_stats["nightborne_death_count"] += 1
#     #         game_stats["enemies_killed_or_removed"] += 1
#
#     def roam(self):
#         self.direction.x, self.direction.y = self.direction_list[self.direction_index]  # gets a random direction
#         self.velocity = self.direction * self.roaming_speed
#         self.position += self.velocity
#
#         self.base_zombie_rect.centerx = self.position.x
#         self.check_collision("horizontal", "roam")
#
#         self.base_zombie_rect.centery = self.position.y
#         self.check_collision("vertical", "roam")
#
#         self.rect.center = self.base_zombie_rect.center
#         self.position = (self.base_zombie_rect.centerx, self.base_zombie_rect.centery)
#
#         self.steps -= 1
#
#         if self.steps == 0:
#             self.get_new_direction_and_distance()
#
#     def get_new_direction_and_distance(self):
#         self.direction_index = random.randint(0, len(self.direction_list) - 1)
#         self.steps = random.randint(3, 6) * TILESIZE
#
#     # def check_collision(self, direction, move_state):
#     #     for sprite in obstacles_group:
#     #         if sprite.rect.colliderect(self.base_zombie_rect):
#     #             self.collide = True
#     #             if direction == "horizontal":
#     #                 if self.velocity.x > 0:
#     #                     self.base_zombie_rect.right = sprite.rect.left
#     #                 if self.velocity.x < 0:
#     #                     self.base_zombie_rect.left = sprite.rect.right
#     #             if direction == "vertical":
#     #                 if self.velocity.y < 0:
#     #                     self.base_zombie_rect.top = sprite.rect.bottom
#     #                 if self.velocity.y > 0:
#     #                     self.base_zombie_rect.bottom = sprite.rect.top
#     #             if move_state == "roam":
#     #                 self.get_new_direction_and_distance()
#
#     def hunt_player(self):
#         if self.velocity.x > 0:
#             self.current_movement_sprite = 0
#         else:
#             self.current_movement_sprite = 1
#
#         player_vector = pygame.math.Vector2(self.player.rect.center)
#         enemy_vector = pygame.math.Vector2(self.base_zombie_rect.center)
#         distance = self.get_vector_distance(player_vector, enemy_vector)
#
#         if distance > 0:
#             self.direction = (player_vector - enemy_vector).normalize()
#         else:
#             self.direction = pygame.math.Vector2()
#
#         self.velocity = self.direction * self.hunting_speed
#         self.position += self.velocity
#
#         self.base_zombie_rect.centerx = self.position.x
#         # self.check_collision("horizontal", "hunt")
#
#         self.base_zombie_rect.centery = self.position.y
#         # self.check_collision("vertical", "hunt")
#
#         self.rect.center = self.base_zombie_rect.center
#
#         self.position = (self.base_zombie_rect.centerx, self.base_zombie_rect.centery)
#
#     def get_vector_distance(self, vector_1, vector_2):
#         return (vector_1 - vector_2).magnitude()
#
#     # def import_graphics(self, name):
#     #     self.animations = {'roam': [], 'death': [], 'hunt': []}
#     #
#     #     main_path = f'{name}/'
#     #     for animation in self.animations.keys():
#     #         self.animations[animation] = import_folder(main_path + animation)
#
#     # def animate(self, index, animation_speed, sprite, type):
#     #     index += animation_speed
#     #
#     #     if index >= len(sprite):  # animation over
#     #         index = 0
#     #         if type == "death":
#     #             self.kill()
#     #
#     #     self.image = sprite[int(index)]
#     #     self.image = pygame.transform.rotozoom(self.image, 0, self.image_scale)
#     #
#     #     if type == "hunt" or type == "idle" or "death":
#     #         if self.velocity.x < 0:
#     #             self.image = pygame.transform.flip(self.image, flip_x=180, flip_y=0)
#     #
#     #     return index
#
#     # def check_player_collision(self):
#     #     if pygame.Rect.colliderect(self.base_zombie_rect, player.base_player_rect):  # player and enemy collides
#     #         self.kill()
#     #         player.get_damage(self.attack_damage)
#     #         game_stats["enemies_killed_or_removed"] += 1
#     #         # scream_sound.play()
#
#     # def draw_enemy_health(self, x, y):
#     #     if self.health > 60:
#     #         col = GREEN
#     #     elif self.health > 30:
#     #         col = YELLOW
#     #     else:
#     #         col = RED
#     #     width = int(self.base_zombie_rect.width * self.health / 100)
#     #     pygame.draw.rect(screen, col, (x - 40 - game_level.offset.x, y - 45 - game_level.offset.y, width, 5))
#
#     def update(self):
#
#         # self.draw_enemy_health(self.position[0], self.position[1])
#
#         if self.alive:
#             self.check_alive()
#             if self.get_vector_distance(pygame.math.Vector2(self.player.rect.center),
#                                         pygame.math.Vector2(self.base_zombie_rect.center)) < 100:
#                 self.check_player_collision()
#
#             if self.get_vector_distance(pygame.math.Vector2(self.player.rect.center),
#                                         pygame.math.Vector2(
#                                             self.base_zombie_rect.center)) < self.notice_radius:  # nightborne 400, necromancer 500
#                 self.hunt_player()
#                 self.current_index = self.animate(self.current_index, self.animation_speed, self.animations["hunt"],
#                                                   "hunt")
#             else:
#                 self.roam()
#                 if self.get_vector_distance(pygame.math.Vector2(self.player.rect.center),
#                                             pygame.math.Vector2(self.base_zombie_rect.center)) < 700:
#                     self.current_index = self.animate(self.current_index, self.roam_animation_speed,
#                                                       self.animations["roam"], "idle")
#         else:  # drop coin and play death animation
#             if not self.coin_dropped:
#                 self.coin_dropped = True
#                 # Item(self.position, "coin")
#             self.current_index = self.animate(self.current_index, self.death_animation_speed, self.animations["death"],
#                                               "death")

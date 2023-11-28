import pygame

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

PLAYER_WIDTH = 129 / 2
PLAYER_HEIGHT = 110 / 2

ENEMY_WIDTH = 32 * 2
ENEMY_HEIGHT = 32 * 2

TILESIZE = 32

monster_data = {
    "zombi_N1": {"health": 100, "attack_damage": 20, "roaming_speed": 2, "hunting_speed": [4,4,7,7,7], "image": pygame.image.load("assets/images/vortigaunt.png"), "image_scale": 1.5, "hitbox_rect": pygame.Rect(0,0,75,100), "animation_speed": 0.2, "roam_animation_speed": 0.05, "death_animation_speed": 0.12, "notice_radius": 500},
}

import pygame
import math
from player import Player
from bullet import Bullet
from hud import HUD
from game_map import GameMap

def game_loop():
    clock = pygame.time.Clock()
    pygame.init()

    width, height = 1600, 900
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('CS2D')

    player = Player((width // 2, height // 2), width, height)
    bullets = []

    game_map = GameMap('assets/images/mapa.png', (width, height))
    hud = HUD()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Se a tecla R for pressionada, recarregue
                    player.reload()
                # Aqui você pode adicionar outras condições de teclas se necessário

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o botão esquerdo do mouse foi pressionado
                if event.button == 1:  # 1 é o botão esquerdo do mouse
                    # Chamada para o método shoot() do jogador
                    player.shoot()
                    # Se a munição for maior que zero, dispara
                    if player.ammo[0] > 0:
                        bullet_sound = pygame.mixer.Sound('music/sounds_gunshot.wav')
                        bullet_sound.play()
                        angle = math.degrees(
                            math.atan2(pygame.mouse.get_pos()[1] - player.pos.y,
                                       pygame.mouse.get_pos()[0] - player.pos.x))
                        bullet = Bullet(player.pos, angle)
                        bullets.append(bullet)

        # Atualiza o jogador
        player.update()
        screen.fill((0, 0, 0))

        # Desenha o mapa
        game_map.draw(screen)

        # Desenha o HUD
        hud.draw(screen, player.health, 100, player.ammo, player.money)

        # Atualiza e desenha as balas
        for bullet in bullets[:]:
            if bullet.update(width, height):
                bullets.remove(bullet)
            else:
                screen.blit(bullet.image, bullet.rect.topleft)

        # Desenha o jogador
        screen.blit(player.image, player.rect.topleft)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    game_loop()

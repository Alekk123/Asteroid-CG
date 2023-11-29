import pygame
import math
import random
from player import Player
from bullet import Bullet
from hud import HUD
from game_map import GameMap
from enemy import Enemy
from hit import Hit

def game_loop():
    clock = pygame.time.Clock()
    pygame.init()

    width, height = 1600, 900
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('CS2D')

    player = Player((width // 3, height // 3), width, height)
    bullets = []

    game_map = GameMap('src/assets/images/mapa_rua.png', (width, height))
    hud = HUD(width, height)

    monster_qtd = 10
    enemies = [Enemy(width, height) for _ in range(monster_qtd)]

    enemy = Enemy(width, height)

    enemy_killed_count = 0

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
                        bullet_sound = pygame.mixer.Sound('src/music/sounds_gunshot.wav')
                        bullet_sound.play()
                        # Correção: o ângulo deve ser passado em radianos para a classe Bullet
                        angle = math.atan2(pygame.mouse.get_pos()[1] - player.pos.y,
                                           pygame.mouse.get_pos()[0] - player.pos.x)
                        # Definir o offset aqui - ajuste este valor conforme necessário
                        offset = 0  # O offset é a distância da posição do jogador até onde a bala é criada
                        # Correção: passar o ângulo em radianos e o offset para a classe Bullet
                        bullet = Bullet(player.pos, angle, offset)
                        bullets.append(bullet)

        # Atualiza o jogador
        player.update()
        screen.fill((0, 0, 0))

        # Desenha o mapa
        game_map.draw(screen)

        # Desenha o HUD
        hud.draw(screen, player.health, player.ammo)

        if enemy_killed_count == 10:
            monster_qtd += 10
            enemies.extend([Enemy(width, height) for _ in range(10)])
            enemy_killed_count = 0


        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    print("Colisão!")
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    enemy_killed_count += 1


        for enemy in enemies:
            enemy.update()
            screen.blit(enemy.image, enemy.rect)


        # Atualiza e desenha as balas
        for bullet in bullets[:]:
            if bullet.update(width, height):
                bullets.remove(bullet)
            else:
                screen.blit(bullet.image, bullet.rect.topleft)

        # Desenha o jogador
        screen.blit(player.image, player.rect.topleft)

        for enemy in enemies:
            enemy.update()
            screen.blit(enemy.image, enemy.rect)
            pygame.draw.rect(screen, (255, 0, 0), enemy.rect, 10)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    game_loop()

import pygame

class HUD:
    def __init__(self):
        # Carregar os ícones para o HUD e redimensioná-los
        icon_scale = 1.3  # Aumentar em 30%
        icon_size = (int(32 * icon_scale), int(32 * icon_scale))  # Tamanho com aumento
        self.heart_icon = pygame.transform.scale(pygame.image.load('assets/images/health_icon.png'), icon_size)
        self.shield_icon = pygame.transform.scale(pygame.image.load('assets/images/shield_icon.png'), icon_size)

        # Carregar uma fonte bonita
        self.font = pygame.font.Font('assets/fonts/cs_regular.ttf', 36)

    def draw(self, screen, health, shield, ammo, money):
        # Definir cores
        red = (255, 0, 0)
        yellow = (255, 255, 0)

        # Posições das barras
        health_bar_width = 100 * (health / 100)  # Assumindo que a saúde máxima é 100

        # Posições dos ícones
        icon_pos_health = (20, screen.get_height() - 20 - self.heart_icon.get_height())

        # Posições das barras atrás dos ícones
        health_bar_rect = pygame.Rect(icon_pos_health[0] + self.heart_icon.get_width() + 10,
                                      icon_pos_health[1] + self.heart_icon.get_height() // 2 - 7, health_bar_width, 15)

        # Desenhar barra de saúde
        pygame.draw.rect(screen, red, health_bar_rect)

        # Desenhar ícone de vida
        screen.blit(self.heart_icon, icon_pos_health)

        # Tamanho da fonte proporcional ao tamanho da tela
        font_size = int(24 * (screen.get_width() / 1600))  # Ajuste proporcional
        self.font = pygame.font.Font('assets/fonts/cs_regular.ttf', font_size)

        # Posições do texto Ammo (agora $) e Money (números sem a palavra Ammo)
        ammo_text_pos = (screen.get_width() - 150 * (screen.get_width() / 1600), screen.get_height() - 50 * (screen.get_height() / 900))
        money_text_pos = (screen.get_width() - 150 * (screen.get_width() / 1600), ammo_text_pos[1] - 30 * (screen.get_height() / 900))

        # Desenhar texto para munição (agora $) e dinheiro (números sem a palavra Ammo)
        money_text = self.font.render(f'{ammo}', True, yellow)  # Removi a palavra "Ammo"
        screen.blit(money_text, money_text_pos)  # Money acima

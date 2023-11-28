import pygame

class HUD:
    def __init__(self, screen_width, screen_height):
        # Define um fator de escala para aumentar os ícones
        icon_scale = 3  # Aumentar para quatro vezes o tamanho original

        # Carrega e escala o ícone de saúde de acordo com o fator de escala
        self.heart_icon = pygame.transform.scale(
            pygame.image.load('src/assets/images/health_icon.png'),
            (int(32 * icon_scale), int(32 * icon_scale))
        )

        # Carrega e escala o ícone de munição de acordo com o fator de escala
        self.ammo_icon = pygame.transform.scale(
            pygame.image.load('src/assets/images/ammo.png'),
            (int(36 * icon_scale), int(36 * icon_scale))
        )

        # Aumenta o tamanho da fonte proporcionalmente ao aumento dos ícones
        self.font_size = int(36 * icon_scale)  # Tamanho da fonte baseado no fator de escala
        self.font = pygame.font.Font('src/assets/fonts/cs_regular.ttf', self.font_size)

        # Guarda as dimensões da tela para uso no método draw
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self, screen, health, ammo):
        # Define cores para o texto
        yellow = (255, 255, 0)

        # Define a posição do ícone de saúde
        icon_pos_health = (20, self.screen_height - self.heart_icon.get_height() - 20)

        # Desenha o ícone de saúde
        screen.blit(self.heart_icon, icon_pos_health)

        # Renderiza o texto da saúde com opacidade de 70% e posiciona à direita do ícone de saúde
        health_font = pygame.font.Font('src/assets/fonts/cs_regular.ttf', self.font_size // 2)
        health_text = health_font.render(f'HP: {health}', True, yellow)
        health_text_surface = pygame.Surface(health_text.get_size(), pygame.SRCALPHA)
        health_text_surface.set_alpha(178)  # 70% opacidade
        health_text_surface.blit(health_text, (0, 0))

        # Posiciona o texto da saúde à direita do ícone de saúde
        health_text_pos = (icon_pos_health[0] + self.heart_icon.get_width() + 10,
                           icon_pos_health[1] + (self.heart_icon.get_height() - health_text_surface.get_height()) // 2)

        # Desenha a Surface do texto da saúde na tela
        screen.blit(health_text_surface, health_text_pos)

        # Define a nova fonte para o texto da munição com metade do tamanho original
        smaller_font = pygame.font.Font('src/assets/fonts/cs_regular.ttf', self.font_size // 2)

        # Renderiza o texto da munição com o novo formato "xx | xx"
        ammo_text = smaller_font.render(f'{ammo[0]} | {ammo[1]}', True, yellow)

        # Cria uma nova Surface para o texto da munição com opacidade ajustada
        ammo_text_surface = pygame.Surface((ammo_text.get_width(), ammo_text.get_height()), pygame.SRCALPHA)
        ammo_text_surface.set_alpha(178)  # 70% opacidade
        ammo_text_surface.blit(ammo_text, (0, 0))

        # Define a posição do ícone de munição para a direita do texto
        icon_pos_ammo = (self.screen_width - self.ammo_icon.get_width() - 20,
                         self.screen_height - self.ammo_icon.get_height() - 20)

        # Desenha o ícone de munição
        screen.blit(self.ammo_icon, icon_pos_ammo)

        # Define a posição do texto da munição para a esquerda do ícone
        ammo_text_pos = (icon_pos_ammo[0] - ammo_text_surface.get_width() - 10,
                         icon_pos_ammo[1] + (self.ammo_icon.get_height() // 2) - (ammo_text_surface.get_height() // 2))

        # Desenha a Surface do texto da munição na tela
        screen.blit(ammo_text_surface, ammo_text_pos)

import pygame
import sys
from Game import game_loop


def quit_game():
    pygame.quit()
    sys.exit()
def draw_button(screen, msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    small_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surf, text_rect = text_objects(msg, small_text)
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(text_surf, text_rect)


def text_objects(text, font, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def draw_text_with_outline(screen, text, font, x, y, text_color, outline_color):
    text_surface, text_rect = text_objects(text, font, text_color)
    outline_surface, _ = text_objects(text, font, outline_color)

    positions = [(x - 2, y - 2), (x + 2, y - 2), (x - 2, y + 2), (x + 2, y + 2)]

    for position in positions:
        text_rect.center = position
        screen.blit(outline_surface, text_rect)

    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)


def options_menu():
    # Placeholder for the options menu
    print("Menu de opção nao tem nada implementado ainda.")


def main_menu():
    pygame.init()
    pygame.font.init()
    # pygame.mixer.init()
    # pygame.mixer.music.load('music/musica_fundo_menu.mp3')
    # pygame.mixer.music.play(-1)

    width, height = 1600, 900
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Menu do CS2D')

    bg = pygame.image.load('src/assets/images/fundo_menu.jpg')
    bg = pygame.transform.scale(bg, (width, height))

    clock = pygame.time.Clock()

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        screen.blit(bg, (0, 0))

        # Draw CS2D Logo
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        draw_text_with_outline(screen, "CS2D", large_text, 1100, 100, (128, 0, 0), (0, 0, 0))

        # Draw buttons
        draw_button(screen, "GO!", 1050, 200, 100, 50, (0, 255, 0), (0, 200, 0), game_loop)
        draw_button(screen, "Quit", 1050, 300, 100, 50, (255, 0, 0), (200, 0, 0), quit_game)

        pygame.display.update()
        clock.tick(15)


if __name__ == "__main__":
    main_menu()

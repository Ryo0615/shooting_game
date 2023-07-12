import pygame

def draw_text(screen, text, size, x, y, color):
    font = pygame.font.Font(None, size)
    surface = font.render(text, True, color)
    x = x - surface.get_width() / 2
    y = y - surface.get_height() / 2
    screen.blit(surface, (x, y))
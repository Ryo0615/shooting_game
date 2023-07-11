import pygame
from setting import *

class Game():

    def __init__(self):
        self.screen = pygame.display.get_surface()

        # 背景
        self.pre_bg_img = pygame.image.load('assets/img/background/bg.png')
        self.bg_img = pygame.transform.scale(self.pre_bg_img, (screen_width, screen_height))
        self.bg_y = 0
        self.scroll_speed = 0.5

    def scroll_bg(self):
        self.bg_y = (self.bg_y + self.scroll_speed) % screen_height
        self.screen.blit(self.bg_img, (0, self.bg_y - screen_height)) # y: -600 ~ -1
        self.screen.blit(self.bg_img, (0, self.bg_y)) # y: 0 ~ 599

    def run(self):
        self.scroll_bg()
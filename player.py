import pygame
from setting import *

class Player(pygame.sprite.Sprite):

    def __init__(self, groups, x, y):
        super().__init__(groups)

        # 画像
        self.image_list = []
        for i in range(3):
            image = pygame.image.load(f'assets/img/player/{i}.png')
            self.image_list.append(image)

        self.index = 0 # 0:idle, 1:left, 2:right
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(self.pre_image, (50, 50))
        self.rect = self.image.get_rect(center = (x, y))

        # 移動
        self.direction = pygame.math.Vector2()
        self.speed = 5

    def move(self):
        if self.direction.magnitude() != 0: # ベクトルの長さが0でないとき
            self.direction.normalize()      # ベクトルの長さを1にする
        
        self.rect.x += self.direction.x * self.speed
        self.check_out_of_screen('horizontal')
        self.rect.y += self.direction.y * self.speed
        self.check_out_of_screen('vertical')

    def input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.direction.x = -1
            self.index = 1
        elif key[pygame.K_RIGHT]:
            self.direction.x = 1
            self.index = 2
        else:
            self.direction.x = 0
            self.index = 0
        
        if key[pygame.K_UP]:
            self.direction.y = -1
        elif key[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def check_out_of_screen(self, direction):
        if direction == 'horizontal':
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > screen_width:
                self.rect.right = screen_width
        
        elif direction == 'vertical':
            if self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > screen_height:
                self.rect.bottom = screen_height

    def update_image(self):
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(self.pre_image, (50, 50))

    def update(self):
        self.input()
        self.move()
        self.update_image()
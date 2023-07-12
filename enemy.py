import pygame
from setting import *
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, bullet_group):
        super().__init__(groups)

        # 弾のグループ
        self.bullet_group = bullet_group

        # 画像
        self.image_list = []
        for i in range(5):
            image = pygame.image.load(f'assets/img/enemy/{i}.png')
            self.image_list.append(image)
        
        self.index = 0
        self.pre_image = self.image_list[self.index]
        self.image = pygame.transform.scale(self.pre_image, (50, 50))
        self.rect = self.image.get_rect(center = (x, y))

        # 移動
        move_list = [1, -1]
        self.direction = pygame.math.Vector2((random.choice(move_list), 1))
        self.speed = 1
        self.timer = 0

        # 体力
        self.health = 3
        self.alive = True

    def move(self):
        self.timer += 1
        if self.timer > 80:
            self.direction.x *= -1
            self.timer = 0

        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def animation(self):
        self.index += 0.15

        if self.index >= len(self.image_list):
            self.index = 0
        
        self.pre_image = self.image_list[int(self.index)]
        self.image = pygame.transform.scale(self.pre_image, (50, 50))

    def check_out_of_screen(self):
        if self.rect.top > screen_height:
            self.kill()

    def collision_bullet(self):
        for bullet in self.bullet_group:
            if self.rect.colliderect(bullet.rect):
                bullet.kill()
                self.health -= 1

        if self.health <= 0:
            self.kill()

    def check_death(self):
        if not self.alive:
            self.kill()
        
    def update(self):
        self.move()
        self.check_out_of_screen()
        self.animation()
        self.collision_bullet()
        self.check_death()
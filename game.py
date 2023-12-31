import pygame
from setting import *
from player import Player
from enemy import Enemy
import random
from support import draw_text

class Game():

    def __init__(self):
        self.screen = pygame.display.get_surface()

        # グループの作成
        self.create_group()

        # プレイヤーの作成
        self.player = Player(self.player_group, 300, 500, self.enemy_group)

        # 敵の作成
        self.timer = 0

        # 背景
        self.pre_bg_img = pygame.image.load(asset_path(f'assets/img/background/bg.png'))
        self.bg_img = pygame.transform.scale(self.pre_bg_img, (screen_width, screen_height))
        self.bg_y = 0
        self.scroll_speed = 0.5

        # ゲームオーバー
        self.game_over = False

        # BGM
        pygame.mixer.music.load(asset_path(f'assets/sound/bgm.mp3'))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

    def create_group(self):
        self.player_group = pygame.sprite.GroupSingle()
        self.enemy_group = pygame.sprite.Group()

    def create_enemy(self):
        self.timer += 1
        if self.timer > 50:
            enemy = Enemy(self.enemy_group, random.randint(50, 550), 0, self.player.bullet_group)
            self.timer = 0

    def check_player_death(self):
        if len(self.player_group) == 0:
            self.game_over = True
            draw_text(self.screen, 'GAME OVER', 75, screen_width/2, screen_height/2, RED)
            draw_text(self.screen, 'Press SPACE KEY to restart', 50, screen_width/2, screen_height/2 + 100, RED)

    def restart(self):
        key = pygame.key.get_pressed()
        if self.game_over and key[pygame.K_SPACE]:
            self.player = Player(self.player_group, 300, 500, self.enemy_group)
            self.enemy_group.empty()
            self.game_over = False

    def scroll_bg(self):
        self.bg_y = (self.bg_y + self.scroll_speed) % screen_height
        self.screen.blit(self.bg_img, (0, self.bg_y - screen_height)) # y: -600 ~ -1
        self.screen.blit(self.bg_img, (0, self.bg_y)) # y: 0 ~ 599

    def run(self):
        self.scroll_bg()

        self.create_enemy()

        self.check_player_death()
        self.restart()

        # グループの描画と更新
        self.player_group.draw(self.screen)
        self.player_group.update()
        self.enemy_group.draw(self.screen)
        self.enemy_group.update()
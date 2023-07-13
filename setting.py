import sys
import os

# ウィンドウの設定
screen_width = 600
screen_height = 600

# FPSの設定
FPS = 60

# 色の設定
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRREN = (0, 255, 0)
BLUE = (0, 0, 255)

# EXE化
# pyinstaller -F -w main.py
# debug: EXE化するときはFalseにする 
debug = False
asset_path = lambda path: path if debug == True else os.path.join(sys._MEIPASS, path.split('/')[-1])
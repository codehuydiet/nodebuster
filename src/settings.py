import pygame
from os.path import join
from os import walk

class infomation:
    def __init__(self):
        self.WINDOW_WIDTH = 1280
        self.WINDOW_HEIGHT = 720
        self.SPAWN_RATE = 10000
        self.FPS = 60
        self.FONT_SIZE = int(((self.WINDOW_WIDTH + self.WINDOW_HEIGHT)/ 2)/41.666666)
        self.PLAYER_HEALTH = 10.0
        self.PLAYER_MAX_HEALTH = 10.0
        self.PLAYER_ATK = 10
        self.HP_LOST_PER_SEC = 0.01
        self.TOTAL_BITS = 0
        self.BITS = 0
        self.CURRENT_LEVEL = 0
        self.IS_TERMINATED = False
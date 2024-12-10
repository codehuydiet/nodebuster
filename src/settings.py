import pygame
from os.path import join
from os import walk
import json

class infomation:
    def __init__(self):
        self.skills = self.load_skills()
        self.damage = self.skills[0]
        # print(self.damage)
        self.hp = self.skills[1]
        self.shield = self.skills[2]
        self.options = self.load_options()
        self.save_data = self.load_save()
        # print(self.save_data["state"])

        self.WINDOW_WIDTH = 1280
        self.WINDOW_HEIGHT = 720
        self.SPAWN_RATE = self.save_data["state"]["spawn_rate"]
        self.FPS = 60
        self.FONT_SIZE = int(((self.WINDOW_WIDTH + self.WINDOW_HEIGHT)/ 2)/41.666666)
        self.PLAYER_MAX_HEALTH = self.save_data["state"]["max_health"]
        self.PLAYER_HEALTH = self.PLAYER_MAX_HEALTH
        self.PLAYER_ATK = self.save_data["state"]["atk"]
        self.PLAYER_SHIELD = self.save_data["state"]["shield"]
        self.HP_LOST_PER_SEC = 0.01
        self.TOTAL_BITS = self.save_data["state"]["bits"]
        self.BITS = 0
        self.CURRENT_LEVEL = self.save_data["state"]["curr_level"]
        self.IS_TERMINATED = False
        self.bgm_volume = self.options.get('bgm_volume', 60)
        self.current_bits = self.save_data.get('state', {}).get('bits', 0)

        self.ARMOR = self.save_data["upgrades"]["Armor"]
        self.DAMAGE = self.save_data["upgrades"]["Damage"]
        self.HEALTH = self.save_data["upgrades"]["Health"]
        
    
    def load_skills(self):
        try:
            with open('skills.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Warning: skills.json not found")
            return []
    def load_options(self):
        try:
            with open('options.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Warning: options.json not found")
            return {}

    def load_save(self):
        try:
            with open('save.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Warning: save.json not found")
            return {}
        
info = infomation()
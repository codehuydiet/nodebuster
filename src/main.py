from settings import *
from player import *
from group import *
from menu import Menu
from skills import Skills
from gamesetting import *
from game import *
from credit import *
from terminate import Terminate
class Main:
    def __init__(self):
        pygame.init()
        self.infomation = infomation()
        self.display_surf = pygame.display.set_mode((self.infomation.WINDOW_WIDTH, self.infomation.WINDOW_HEIGHT))
        pygame.display.set_caption('Nodebuster')
        self.clock = pygame.time.Clock()
        self.running = True

        # Initialize all states
        self.menu = Menu(self)
        self.settings = GameSetting(self)
        self.credit = Credit(self)
        self.skills = Skills(self)  
        self.terminate = Terminate(self)
        self.current_screen = self.menu
        
        # State management
        self.states = {
            "MENU": self.menu,
            "SETTINGS": self.settings,
            "SKILLS": self.skills,
            "CREDIT": self.credit,
            "TERMINATE" : self.terminate,
        }
    def init_game(self):
        self.game = self.game = Game(self.clock.tick(self.infomation.FPS)/1000, self)
        self.states["GAME"] = self.game

    def set_screen(self, name):
        if name in self.states:
            self.current_screen = self.states[name]

    def reset(self):
        self.infomation = infomation()

    def save_infomation(self):
        data_to_save = {
            "state": {
                "bits": self.infomation.TOTAL_BITS,
                "atk": self.infomation.PLAYER_ATK,
                "max_health": self.infomation.PLAYER_MAX_HEALTH,
                "shield": self.infomation.PLAYER_SHIELD,
                "curr_level": self.infomation.CURRENT_LEVEL,
                "spawn_rate": self.infomation.SPAWN_RATE
            },
            "upgrades": {
                "Armor": self.infomation.ARMOR,
                "Damage": self.infomation.DAMAGE,
                "Health": self.infomation.HEALTH
            }
        }
        with open('save.json', 'w') as save_file:
            json.dump(data_to_save, save_file, indent=4)
        data_to_save =[
                {
                    "id": "Damage",
                    "name": "power",
                    "curr_lvl": self.infomation.damage["curr_lvl"],
                    "max_lvl": 16,
                    "currency": "bits",
                    "is_open": 1,
                    "cost": {
                        "0": {
                            "value": 0,
                            "cost": 0
                        },
                        "1": {
                            "value": 1,
                            "cost": 1
                        },
                        "2": {
                            "value": 3,
                            "cost": 3
                        },
                        "3": {
                            "value": 5,
                            "cost": 8
                        },
                        "4": {
                            "value": 7,
                            "cost": 15
                        },
                        "5": {
                            "value": 9,
                            "cost": 26
                        },
                        "6": {
                            "value": 11,
                            "cost": 42
                        },
                        "7": {
                            "value": 12,
                            "cost": 57
                        },
                        "8": {
                            "value": 14,
                            "cost": 75
                        },
                        "9": {
                            "value": 15,
                            "cost": 93
                        },
                        "10": {
                            "value": 16,
                            "cost": 131
                        },
                        "11": {
                            "value": 17,
                            "cost": 172
                        },
                        "12": {
                            "value": 18,
                            "cost": 184
                        },
                        "13": {
                            "value": 19,
                            "cost": 256
                        },
                        "14": {
                            "value": 20,
                            "cost": 347
                        },
                        "15": {
                            "value": 21,
                            "cost": 498
                        },
                        "16": {
                            "value": "Max Level",
                            "cost": "Max Level"
                        },
                        "17": {
                            "value": "Max Level",
                            "cost": "Max Level"
                        }
                    }
                },
                {
                    "id": "hp",
                    "name": "heath",
                    "curr_lvl": self.infomation.hp["curr_lvl"],
                    "max_lvl": 16,
                    "currency": "bits",
                    "is_open": 1,
                    "cost": {
                        "0": {
                            "value": 0,
                            "cost": 0
                        },
                        "1": {
                            "value": 1,
                            "cost": 1
                        },
                        "2": {
                            "value": 3,
                            "cost": 3
                        },
                        "3": {
                            "value": 5,
                            "cost": 8
                        },
                        "4": {
                            "value": 7,
                            "cost": 15
                        },
                        "5": {
                            "value": 9,
                            "cost": 26
                        },
                        "6": {
                            "value": 11,
                            "cost": 42
                        },
                        "7": {
                            "value": 12,
                            "cost": 57
                        },
                        "8": {
                            "value": 14,
                            "cost": 75
                        },
                        "9": {
                            "value": 15,
                            "cost": 93
                        },
                        "10": {
                            "value": 16,
                            "cost": 131
                        },
                        "11": {
                            "value": 17,
                            "cost": 172
                        },
                        "12": {
                            "value": 18,
                            "cost": 184
                        },
                        "13": {
                            "value": 19,
                            "cost": 256
                        },
                        "14": {
                            "value": 20,
                            "cost": 347
                        },
                        "15": {
                            "value": 21,
                            "cost": 498
                        },
                        "16": {
                            "value": "Max Level",
                            "cost": "Max Level"
                        },
                        "17": {
                            "value": "Max Level",
                            "cost": "Max Level"
                        }
                    }
                },
                {
                    "id": "Shield",
                    "name": "defend",
                    "value": 3,
                    "curr_lvl": self.infomation.shield["curr_lvl"],
                    "max_lvl": 16,
                    "currency": "bits",
                    "is_open": 0,
                    "cost": {
                        "0": {
                            "value": 0,
                            "cost": 0
                        },
                        "1": {
                            "value": 1,
                            "cost": 1
                        },
                        "2": {
                            "value": 3,
                            "cost": 3
                        },
                        "3": {
                            "value": 5,
                            "cost": 8
                        },
                        "4": {
                            "value": 7,
                            "cost": 15
                        },
                        "5": {
                            "value": 9,
                            "cost": 26
                        },
                        "6": {
                            "value": 11,
                            "cost": 42
                        },
                        "7": {
                            "value": 12,
                            "cost": 57
                        },
                        "8": {
                            "value": 14,
                            "cost": 75
                        },
                        "9": {
                            "value": 15,
                            "cost": 93
                        },
                        "10": {
                            "value": 16,
                            "cost": 131
                        },
                        "11": {
                            "value": 17,
                            "cost": 172
                        },
                        "12": {
                            "value": 18,
                            "cost": 184
                        },
                        "13": {
                            "value": 19,
                            "cost": 256
                        },
                        "14": {
                            "value": 20,
                            "cost": 347
                        },
                        "15": {
                            "value": 21,
                            "cost": 498
                        },
                        "16": {
                            "value": "Max Level",
                            "cost": "Max Level"
                        },
                        "17": {
                            "value": "Max Level",
                            "cost": "Max Level"
                        }
                    }
                }
            ]

        with open('skills.json', 'w') as save_file:
            json.dump(data_to_save, save_file, indent=4)
    
    def run(self): 
        while self.running:
            dt = self.clock.tick(self.infomation.FPS)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_infomation()
                    self.running = False
                    
                self.current_screen.handle_event(event)
            if self.current_screen == self.states['SETTINGS'] or self.current_screen == self.states['CREDIT']:
                self.current_screen.update(dt, self.menu)
            elif self.current_screen == self.states['TERMINATE']:
                self.current_screen.update(dt, self.game)
            else:
                self.current_screen.update(dt)

            pygame.display.update()
        pygame.quit()


if __name__ ==  '__main__':
    game = Main()
    game.run()


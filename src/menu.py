from settings import *
from components.button import Button
from game import *
import time

finished_typing = False
start_time = time.time()

class Menu:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(join('images', 'PixelOperator.ttf'), self.game.infomation.FONT_SIZE)
        # Create buttons
        self.play_button = Button(
            self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*85), 
            self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*40), 
            ((self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*25))/4)-(self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*95)), 
            self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*91), 
            "New game", 
            self.font, 
            (89, 164, 255), 
            (255, 255, 255)
        )

        self.continue_button = Button(
            self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*85) + ((self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*25))/4),
            self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*40),
            ((self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*25))/4)-(self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*95)),
            self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*91),
            "Continue",
            self.font,
            (45, 162, 64),
            (255, 255, 255)
        )

        self.settings_button = Button(
            self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*85) + ((self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*25))/4)*2,
            self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*40) + (self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*99)),
            ((self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*25))/4)-(self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*95)),
            self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*93),
            "Settings",
            self.font,
            (255, 100, 231),
            (255, 255, 255)
        )

        self.quit_button = Button(
            self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*85) + ((self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*25))/4)*3,
            self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*40) + (self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*99)),
            ((self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*25))/4)-(self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*95)),
            self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*93),
            "Quit",
            self.font,
            (255, 75, 80),
            (255, 255, 255)
        )

        self.credit_button = Button(
            self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*98),
            self.game.infomation.WINDOW_HEIGHT - (self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*98)) - (self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*95)),
            self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*93),
            self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*95),
            "Credit",
            self.font,
            (31, 31, 31),
            (255, 255, 255)
        )

        self.font = pygame.font.Font(join('images', 'PixelOperator.ttf'), 80)
        self.text = "NODEBUSTER"
        self.typing_speed = 0.3
        self.TEXT_COLOR = (255, 255, 255)
        self.text_surface = self.font.render(self.text, True, self.TEXT_COLOR)
        

    def reset_infomation(self):
        data_to_save = {
            "state": {
                "bits": 0,
                "atk": 10.0,
                "max_health": 10.0,
                "shield": 0.0,
                "curr_level": 0,
                "spawn_rate": 50000
            },
            "upgrades": {
                "Armor": 0,
                "Damage": 0,
                "Health": 0
            }
        }
        with open('save.json', 'w') as save_file:
            json.dump(data_to_save, save_file, indent=4)
        data_to_save =[
                {
                    "id": "Damage",
                    "name": "power",
                    "curr_lvl": 0,
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
                    "curr_lvl": 0,
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
                    "curr_lvl": 0,
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

    def handle_event(self, event):
        if self.play_button.handle_event(event, self.game.press):
            self.reset_infomation()
            self.game.reset()
            self.game.set_screen("SKILLS")
        elif self.settings_button.handle_event(event, self.game.press):
            self.game.set_screen("SETTINGS")
        elif self.continue_button.handle_event(event, self.game.press):
            self.game.set_screen("SKILLS")
        elif self.quit_button.handle_event(event, self.game.press):
            self.game.save_infomation()
            self.game.running = False
        elif self.credit_button.handle_event(event, self.game.press):
            self.game.set_screen("CREDIT")


    def update(self, dt):
        self.display_surf = pygame.display.get_surface()
        self.display_surf.fill("#1f1f1f")
        x, y = (self.game.infomation.WINDOW_WIDTH - self.text_surface.get_width())//2, self.game.infomation.WINDOW_HEIGHT // 4
        print(x, y)
        elapsed_time = time.time() - start_time
        finished_typing = self.game.typewriter_effect(self.text, self.font, self.TEXT_COLOR, x, y, elapsed_time, self.typing_speed)
        self.play_button.draw(self.display_surf, dt)
        self.continue_button.draw(self.display_surf, dt)
        self.settings_button.draw(self.display_surf, dt)
        self.quit_button.draw(self.display_surf, dt)
        self.credit_button.draw(self.display_surf, dt)

        
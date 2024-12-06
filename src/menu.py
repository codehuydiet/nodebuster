from settings import *
from components.button import Button
from game import *

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
            "new game", 
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

    def handle_event(self, event):
        if self.play_button.handle_event(event):
            # print('vgbneiwughviewrbwb')
            self.game.init_game()
            self.game.infomation.IS_TERMINATED = False
            self.game.set_screen("GAME")
        elif self.settings_button.handle_event(event):
            self.game.set_screen("SETTINGS")
        elif self.continue_button.handle_event(event):
            # self.game.set_screen("SETTINGS")
            pass
        elif self.quit_button.handle_event(event):
            self.game.running = False
        elif self.credit_button.handle_event(event):
            self.game.set_screen("CREDIT")


    def update(self, dt):
        self.display_surf = pygame.display.get_surface()
        self.display_surf.fill("#1f1f1f")
        self.play_button.draw(self.display_surf, dt)
        self.continue_button.draw(self.display_surf, dt)
        self.settings_button.draw(self.display_surf, dt)
        self.quit_button.draw(self.display_surf, dt)
        self.credit_button.draw(self.display_surf, dt)

        
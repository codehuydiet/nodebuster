import pygame
from settings import *
from components.button import Button

class Terminate:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(join('images', 'PixelOperator.ttf'), self.game.infomation.FONT_SIZE)

        self.ok_button = Button(
            self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*85), 
            self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*40), 
            ((self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*25))/4)-(self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*95)), 
            self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*91), 
            "ok", 
            self.font, 
            (89, 164, 255), 
            (255, 255, 255)
        )
    
    def handle_event(self, event):
        if self.ok_button.handle_event(event):
            self.game.set_screen("MENU")
        
    def update(self, dt, game):
        self.display_surf = pygame.display.get_surface()
        self.display_surf.fill("#1f1f1f")
        self.ok_button.draw(self.display_surf, dt)
        
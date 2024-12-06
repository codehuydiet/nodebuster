import pygame
from settings import *
from components.button import Button

class Credit:
    def __init__(self, game):
        self.infomation = infomation
        # Popup dimensions
        self.game = game
        self.display_surf = pygame.display.get_surface()
        self.display_surf.fill('#00000055')
        self.width = self.game.infomation.WINDOW_WIDTH // 2
        self.height = self.game.infomation.WINDOW_HEIGHT // 10 * 8
        self.font = pygame.font.Font(join('images', 'PixelOperator.ttf'), self.game.infomation.FONT_SIZE + 3)
        
        
        # Calculate center position
        self.x = (self.game.infomation.WINDOW_WIDTH - self.width) // 2
        self.y = (self.game.infomation.WINDOW_HEIGHT - self.height) // 2
        
        # Create popup surface
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        # Settings
        self.background_color = (31, 31, 31)
        self.border_color = (200, 200, 200)
        self.overlay = pygame.Surface((self.game.infomation.WINDOW_WIDTH, self.game.infomation.WINDOW_HEIGHT), pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, 128))

        self.ok_button = Button(
            self.x + 8, 
            self.y + self.height -(self.height - (self.height / 10)*9) -8,
            self.width - 16, 
            self.height - (self.height / 10)*9,
            'ok',
            self.font, 
            (255, 75, 80),
            (255, 255, 255)
        )
    
    def handle_event(self, event):
        if self.ok_button.handle_event(event):
            self.game.set_screen("MENU")
        
    def update(self, dt, menu):
        menu.update(dt)
        self.surface.fill(self.background_color)
        self.display_surf.blit(self.overlay, (0, 0))
        pygame.draw.rect(self.surface, self.border_color, (0, 0, self.width, self.height), 2)
        self.display_surf.blit(self.surface, (self.x, self.y))
        self.ok_button.draw(self.display_surf, dt)
        
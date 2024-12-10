import pygame
from settings import *
from components.button import Button

class Terminate:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(join('images', 'PixelOperator.ttf'), self.game.infomation.FONT_SIZE)
        self.font2 = pygame.font.Font(join('images', 'PixelOperator.ttf'), self.game.infomation.FONT_SIZE + 12)
        self.font3 = pygame.font.Font(join('images', 'PixelOperator.ttf'), self.game.infomation.FONT_SIZE + 2)

        self.home_button = Button(
            (self.game.infomation.WINDOW_WIDTH - ( self.game.infomation.WINDOW_HEIGHT // 2))//2, 
            (self.game.infomation.WINDOW_HEIGHT - self.game.infomation.WINDOW_HEIGHT //3), 
            self.game.infomation.WINDOW_HEIGHT // 2, 
            self.game.infomation.WINDOW_HEIGHT // 20, 
            "go to home", 
            self.font, 
            (89, 164, 255), 
            (255, 255, 255)
        )
        self.new_button = Button(
            (self.game.infomation.WINDOW_WIDTH - ( self.game.infomation.WINDOW_HEIGHT // 2))//2, 
            (self.game.infomation.WINDOW_HEIGHT - self.game.infomation.WINDOW_HEIGHT //2.2), 
            self.game.infomation.WINDOW_HEIGHT // 2, 
            self.game.infomation.WINDOW_HEIGHT // 20,
            "new session", 
            self.font, 
            (255, 75, 80), 
            (255, 255, 255)
        )
        self.text_terminate = self.font2.render('SESSION TERMINATED', False, (255, 75, 80))
        self.text_acpuire = self.font3.render('acquired resources', False, (255, 255, 255))

    def handle_event(self, event):
        if self.home_button.handle_event(event, self.game.press):
            self.game.infomation.TOTAL_BITS += self.game.infomation.BITS
            self.game.infomation.BITS = 0
            self.game.set_screen("SKILLS")
        if self.new_button.handle_event(event, self.game.press):
            self.game.infomation.TOTAL_BITS += self.game.infomation.BITS
            self.game.infomation.BITS = 0
            self.game.init_game()
            self.game.infomation.IS_TERMINATED = False
            self.game.set_screen("GAME")
        
    def update(self, dt, game):
        self.display_surf = pygame.display.get_surface()
        self.display_surf.fill("#1f1f1f")
        self.display_surf.blit(
            self.text_terminate, 
            (
                (self.game.infomation.WINDOW_WIDTH - self.text_terminate.get_width())//2, 
                self.game.infomation.WINDOW_HEIGHT//4.5
            )
        )
        self.display_surf.blit(
            self.text_acpuire, 
            (
                (self.game.infomation.WINDOW_WIDTH - self.text_acpuire.get_width())//2, 
                self.game.infomation.WINDOW_HEIGHT//3.4
            )
        )

        
        text = self.font3.render(str(self.game.infomation.BITS), False, (255, 75, 80))
        self.bit = pygame.Surface((text.get_width()+60, text.get_height()+10), pygame.SRCALPHA)
        self.image_bit = pygame.image.load(join('images', 'exp.png')).convert_alpha()
        # self.rect = self.image_bit.get_frect(center = (100, 100))
        self.bit.fill((0, 0, 0, 0)) 
        border_width = 2
        self.bit.blit(
            pygame.transform.scale(
                self.image_bit, 
                (
                    self.image_bit.get_width() * ((text.get_height()//2)/self.image_bit.get_height()), 
                    self.image_bit.get_height() * ((text.get_height()//2)/self.image_bit.get_height())
                )
            ), (
                (text.get_width()+60 - (self.image_bit.get_width() * ((text.get_height()//2)/self.image_bit.get_height()) + text.get_width() + 10))//2, 
                (text.get_height()+10 - self.image_bit.get_height() * ((text.get_height()//2)/self.image_bit.get_height()))//2
            )
        )
        self.bit.blit(
            text,
            (
                (text.get_width()+60 - (self.image_bit.get_width() * ((text.get_height()//2)/self.image_bit.get_height()) + text.get_width() + 10))//2 + self.image_bit.get_width() * ((text.get_height()//2)/self.image_bit.get_height()) + 5,
                (text.get_height()+10 - text.get_height())//2
            )
        )
        pygame.draw.rect(self.bit, 'red', self.bit.get_rect(), border_width)
        self.display_surf.blit(self.bit, ((self.game.infomation.WINDOW_WIDTH - 50) // 2, self.game.infomation.WINDOW_HEIGHT//2.5))

        self.home_button.draw(self.display_surf, dt)
        self.new_button.draw(self.display_surf, dt)
        
        
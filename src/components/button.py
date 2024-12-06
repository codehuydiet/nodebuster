import pygame
import math

class Button:
    def __init__(self, x, y, width, height, text, font, bg_color, text_color):
        self.original_rect = pygame.Rect(x, y, width, height)
        self.rect = self.original_rect.copy()
        self.text = text
        self.font = font
        self.bg_color = bg_color
        self.original_bg_color = bg_color
        self.hovered_bg_color = self._brighten_color(bg_color, 1.4)
        self.clicked_bg_color = self._brighten_color(bg_color, 1.6)
        self.text_color = text_color

        self.hovered = False
        self.clicked = False
        self.click_animation = 0

    def _brighten_color(self, color, factor=1.2):
        return tuple(min(int(c * factor), 255) for c in color)

    def draw(self, screen, dt):
        scale = 1.0
        if self.click_animation > 0:
            scale = 1 - math.sin(self.click_animation * math.pi) * 0.1
            self.click_animation -= dt

        scaled_width = int(self.rect.width * scale)
        scaled_height = int(self.rect.height * scale)
        scaled_rect = self.rect.inflate(scaled_width - self.rect.width, scaled_height - self.rect.height)

        if self.clicked:
            current_bg_color = self.clicked_bg_color
        elif self.hovered:
            current_bg_color = self.hovered_bg_color
        else:
            current_bg_color = self.original_bg_color

        pygame.draw.rect(screen, (255, 255, 255), scaled_rect.inflate(8, 8))
        pygame.draw.rect(screen, (0, 0, 0), scaled_rect.inflate(4, 4))
        pygame.draw.rect(screen, current_bg_color, scaled_rect)

        text_surface = self.font.render(self.text, False, (0, 0, 0))
        text_rect = text_surface.get_rect(center=scaled_rect.center)
        screen.blit(text_surface, (text_rect.x + 2, text_rect.y + 2))

        text_surface = self.font.render(self.text, False, self.text_color)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(mouse_pos):
            if not self.hovered:
                self.hovered = True
        else:
            self.hovered = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(mouse_pos):
            self.clicked = True
            self.click_animation = 0.3  
            return True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.clicked = False
        return False
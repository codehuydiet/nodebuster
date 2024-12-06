import pygame

class Slider:
    def __init__(self, x, y, width, height, min_val, max_val, start_val):
        self.rect = pygame.Rect(x, y, width, height) 
        self.handle_rect = pygame.Rect(0, 0, height, height+10) 
        self.handle_rect.center = (x + width * (start_val - min_val) / (max_val - min_val), y + height // 2)

        self.min_val = min_val
        self.max_val = max_val
        self.value = start_val
        self.dragging = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.handle_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.handle_rect.centerx = max(self.rect.left, min(event.pos[0], self.rect.right))
            self.value = self.min_val + (self.handle_rect.centerx - self.rect.left) / self.rect.width * (self.max_val - self.min_val)

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), self.rect)
        pygame.draw.rect(screen, (255, 0, 0), self.handle_rect)

    def get_value(self):
        return self.value
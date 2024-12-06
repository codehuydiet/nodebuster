from settings import *

class PlayerSprite(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surf = pygame.display.get_surface()

    def draw(self):
        for sprite in self:
            self.display_surf.blit(sprite.image, sprite.rect)

class ExpSprite(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surf = pygame.display.get_surface()

    def draw(self):
        for sprite in self:
            self.display_surf.blit(sprite.image, sprite.rect)

class AllSprite(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surf = pygame.display.get_surface()

    def draw(self):
        for sprite in self:
            self.display_surf.blit(sprite.image, sprite.rect)

from settings import *

class Player():
    def __init__(self, groups):
        super().__init__()
        self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pygame.mouse.get_pos())

    def update(self):
        print("hello")
        


        
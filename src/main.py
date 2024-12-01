from settings import *
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Nodebuster')
        self.clock = pygame.time.Clock()
        self.running = True
        self.sprite = pygame.sprite.Group()
        self.cusor = pygame.mouse.set_visible(False)


    def run(self):
        while self.running:
            self.display_surf.fill("#3a2f4a")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            player = Player(self.sprite)
            self.display_surf.blit(player.image, player.rect)
            pygame.display.update()
        
        
        pygame.quit()


if __name__ ==  '__main__':
    game = Game()
    game.run()



 


from settings import *
from player import *
from group import *
from menu import Menu
from skills import Skills
from gamesetting import *
from game import *
from credit import *
from terminate import Terminate
class Main:
    def __init__(self):
        pygame.init()
        self.infomation = infomation()
        self.display_surf = pygame.display.set_mode((self.infomation.WINDOW_WIDTH, self.infomation.WINDOW_HEIGHT))
        pygame.display.set_caption('Nodebuster')
        self.clock = pygame.time.Clock()
        self.running = True

        # Initialize all states
        self.menu = Menu(self)
        self.settings = GameSetting(self)
        self.credit = Credit(self)
        self.skills = Skills()
        self.terminate = Terminate(self)
        self.current_screen = self.menu
        
        # State management
        self.states = {
            "MENU": self.menu,
            "SETTINGS": self.settings,
            "SKILLS": self.skills,
            "CREDIT": self.credit,
            "TERMINATE" : self.terminate
        }
    def init_game(self):
        self.game = self.game = Game(self.clock.tick(self.infomation.FPS)/1000, self)
        self.states["GAME"] = self.game

    def set_screen(self, name):
        if name in self.states:
            self.current_screen = self.states[name]

    def run(self): 
        while self.running:
            print(self.infomation.TOTAL_BITS)
            dt = self.clock.tick(self.infomation.FPS)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.current_screen.handle_event(event)
            if self.current_screen == self.states['SETTINGS'] or self.current_screen == self.states['CREDIT']:
                self.current_screen.update(dt, self.menu)
            elif self.current_screen == self.states['TERMINATE']:
                self.current_screen.update(dt, self.game)
            else:
                self.current_screen.update(dt)


            pygame.display.update()
        pygame.quit()


if __name__ ==  '__main__':
    game = Main()
    game.run()



 


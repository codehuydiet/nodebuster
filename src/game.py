from settings import *
from player import *
from group import *
from components.button import Button


class Game:
    def __init__(self, dt, game):
        pygame.init()
        self.display_surf = pygame.display.get_surface()
        pygame.display.set_caption('Nodebuster')
        self.clock = pygame.time.Clock()
        self.running = True
        self.game = game

        #fps 
        self.dt = pygame.time.Clock()
        self.dt = dt
        #sprite
        self.sprite = AllSprite()
        self.collision_sprites = pygame.sprite.Group()
        self.player_sprite = PlayerSprite()
        self.exp_sprite = ExpSprite()


        self.cusor = pygame.mouse.set_visible(True)
        self.enemy_event = pygame.event.custom_type()
        pygame.time.set_timer(self.enemy_event, int(self.game.infomation.SPAWN_RATE*self.dt))
        self.player = Player(self.player_sprite, self.collision_sprites, self.exp_sprite, self, game)

        self.font = pygame.font.Font(join('images', 'PixelOperator.ttf'), self.game.infomation.FONT_SIZE)
        self.font2 = pygame.font.Font(join('images', 'PixelOperator.ttf'), self.game.infomation.FONT_SIZE - 2)
        self.text_lvl = self.font.render("level " + str(self.game.infomation.CURRENT_LEVEL), False, (255, 255, 255))
        self.text_heath = self.font.render("heath", False, (255, 255, 255))
        # print(self.text_lvl.get_width())


        #hp bar
        self.hp = pygame.Surface((self.game.infomation.WINDOW_WIDTH//5, self.game.infomation.WINDOW_HEIGHT//22), pygame.SRCALPHA)
        self.bar = self.hp
        self.update_image()

        self.terminate_button = Button(
            self.game.infomation.WINDOW_WIDTH - (self.game.infomation.WINDOW_WIDTH//100)*2 - (self.game.infomation.WINDOW_WIDTH // 9), 
            self.game.infomation.WINDOW_HEIGHT - (self.game.infomation.WINDOW_HEIGHT//100)*8 - (self.game.infomation.WINDOW_HEIGHT // 15),
            self.game.infomation.WINDOW_WIDTH // 9, 
            self.game.infomation.WINDOW_HEIGHT // 15,
            'TERMINATE',
            self.font, 
            (255, 75, 80),
            (255, 255, 255)
        )
    
    def update_image(self):
        self.hp.fill((0, 0, 0, 0)) 
        
        border_width = 2
        pygame.draw.rect(self.hp, 'red', self.hp.get_rect(), border_width)

        inner_size_width = self.game.infomation.WINDOW_WIDTH//5 - 4 * border_width
        inner_size_height = self.game.infomation.WINDOW_HEIGHT//22 - 4 * border_width
        if self.game.infomation.PLAYER_HEALTH <= 0:
            self.game.infomation.PLAYER_HEALTH = 0
        inner_rect = pygame.Rect(border_width+2, border_width+2, inner_size_width * ((self.game.infomation.PLAYER_HEALTH/self.game.infomation.PLAYER_MAX_HEALTH)), inner_size_height)
        pygame.draw.rect(self.hp, 'red', inner_rect)

    def handle_event(self, event):
        if self.terminate_button.handle_event(event, self.game.press) or self.game.infomation.IS_TERMINATED:
            self.game.infomation.IS_TERMINATED = False
            self.game.infomation.PLAYER_HEALTH = self.game.infomation.PLAYER_MAX_HEALTH
            self.running = False
            self.game.set_screen("TERMINATE")


    def update(self, dt):
        while self.running:
            self.display_surf.fill("#1f1f1f")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == self.enemy_event:
                    Enemy((self.sprite, self.collision_sprites), self.sprite, self.exp_sprite, self.game)
                self.handle_event(event)
            self.sprite.update(dt)
            self.player_sprite.update(dt, self)
            self.exp_sprite.update(dt)

            self.exp_sprite.draw()
            self.sprite.draw()
            self.display_surf.blit(self.text_lvl, (self.game.infomation.WINDOW_WIDTH - (self.text_lvl.get_width()+(self.text_lvl.get_width()/3)), self.game.infomation.WINDOW_HEIGHT/50))
            self.display_surf.blit(self.text_heath, (self.text_heath.get_width()/3, self.text_heath.get_height()/3))
            self.display_surf.blit(self.bar, (self.text_heath.get_width()/3, self.text_heath.get_height()*1.3))
            text = self.font.render(str(f"{self.game.infomation.PLAYER_HEALTH:.1f}") + "/" + str(self.game.infomation.PLAYER_MAX_HEALTH), False, (255, 255, 255))
            self.display_surf.blit(text, (
                self.text_heath.get_width()/3 + (self.game.infomation.WINDOW_WIDTH//5 - text.get_width())/2,
                self.text_heath.get_height()*1.3 + (self.game.infomation.WINDOW_HEIGHT//22 - text.get_height())/2
            ))
            self.terminate_button.draw(self.display_surf, dt)
            self.player_sprite.draw()
            
            pygame.display.update()
from settings import *
from components.button import Button
from game import *

class Skills:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(join('images', 'PixelOperator.ttf'), self.game.infomation.FONT_SIZE)

        self.breach_button = Button(
            self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*18), 
            self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*11), 
            ((self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*85))), 
            self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*94), 
            "Breach", 
            self.font, 
            (89, 164, 255), 
            (255, 255, 255)
        )

        self.upgrade_button = Button(
            self.game.infomation.WINDOW_WIDTH //50, 
            self.game.infomation.WINDOW_HEIGHT //50, 
            ((self.game.infomation.WINDOW_WIDTH - ((self.game.infomation.WINDOW_WIDTH/100)*85))), 
            self.game.infomation.WINDOW_HEIGHT - ((self.game.infomation.WINDOW_HEIGHT/100)*94), 
            "Upgrades", 
            self.font, 
            (89, 164, 255), 
            (255, 255, 255)
        )

        self.font3 = pygame.font.Font(join('images', 'PixelOperator.ttf'), self.game.infomation.FONT_SIZE + 2)

        self.image_atk = pygame.image.load(join('src', 'skill_images', "atk.png")).convert_alpha()
        self.image_def = pygame.image.load(join('src', 'skill_images', "def.png")).convert_alpha()
        self.image_health = pygame.image.load(join('src', 'skill_images', "health.png")).convert_alpha()
        self.image_bit = pygame.image.load(join('images', 'exp.png')).convert_alpha()
        self.border_width = 2


    def handle_event(self, event):
        if self.breach_button.handle_event(event):
            self.game.init_game()
            self.game.infomation.IS_TERMINATED = False
            self.game.set_screen("GAME")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.set_screen("MENU")
        if self.damage_button.handle_event(event):
            if self.game.infomation.damage["curr_lvl"] < self.game.infomation.damage["max_lvl"] and self.game.infomation.TOTAL_BITS >= self.game.infomation.damage["cost"][str(self.game.infomation.damage["curr_lvl"] + 1)]["cost"]:
                self.game.infomation.damage["curr_lvl"] += 1
                if not self.game.infomation.damage["curr_lvl"] == self.game.infomation.damage["max_lvl"]:
                    self.game.infomation.TOTAL_BITS -= self.game.infomation.damage["cost"][str(self.game.infomation.damage["curr_lvl"])]["cost"]
                    self.game.infomation.PLAYER_ATK += self.game.infomation.damage["cost"][str(self.game.infomation.damage["curr_lvl"])]["value"]
        if self.hp_button.handle_event(event):
            if self.game.infomation.hp["curr_lvl"] < self.game.infomation.hp["max_lvl"] and self.game.infomation.TOTAL_BITS >= self.game.infomation.hp["cost"][str(self.game.infomation.hp["curr_lvl"] + 1)]["cost"]:
                self.game.infomation.hp["curr_lvl"] += 1
                if not self.game.infomation.hp["curr_lvl"] == self.game.infomation.hp["max_lvl"]:
                    self.game.infomation.TOTAL_BITS -= self.game.infomation.hp["cost"][str(self.game.infomation.hp["curr_lvl"])]["cost"]
                    self.game.infomation.PLAYER_MAX_HEALTH += self.game.infomation.hp["cost"][str(self.game.infomation.hp["curr_lvl"])]["value"]
                    self.game.infomation.PLAYER_HEALTH = self.game.infomation.PLAYER_MAX_HEALTH
        if self.shield_button.handle_event(event):
            if self.game.infomation.shield["curr_lvl"] < self.game.infomation.shield["max_lvl"] and self.game.infomation.TOTAL_BITS >= self.game.infomation.shield["cost"][str(self.game.infomation.shield["curr_lvl"] + 1)]["cost"]:
                self.game.infomation.shield["curr_lvl"] += 1
                if not self.game.infomation.shield["curr_lvl"] == self.game.infomation.shield["max_lvl"]:
                    self.game.infomation.TOTAL_BITS -= self.game.infomation.shield["cost"][str(self.game.infomation.shield["curr_lvl"])]["cost"]
                    self.game.infomation.PLAYER_SHIELD += self.game.infomation.shield["cost"][str(self.game.infomation.shield["curr_lvl"])]["value"]
    
    def images(self, image, x, y):
        blit = pygame.Surface(
            (
                image.get_height() * ((self.game.infomation.WINDOW_WIDTH/30)/image.get_height()) + 10, 
                image.get_height() * ((self.game.infomation.WINDOW_WIDTH/30)/image.get_height()) + 10
            ), pygame.SRCALPHA
        )
        blit.fill((0, 0, 0, 0))
        blit.blit(
            pygame.transform.scale(
                image, 
                (
                    image.get_width() * ((self.game.infomation.WINDOW_WIDTH/30)/image.get_height()), 
                    image.get_height() * ((self.game.infomation.WINDOW_WIDTH/30)/image.get_height())
                )
            ), 
            (((image.get_height() * ((self.game.infomation.WINDOW_WIDTH/30)/image.get_height()) + 10) - (image.get_width() * ((self.game.infomation.WINDOW_WIDTH/30)/image.get_height())))//2, 5)
        )
        pygame.draw.rect(blit, 'red', blit.get_rect(), self.border_width)
        self.display_surf.blit(blit, (x, y))

    def upgrade(self, x, y, lvl, dt):
        border_width = 2
        original_surf = pygame.Surface((20, 40), pygame.SRCALPHA)
        
        for i in range(15):
            x+=30
            if i < lvl["curr_lvl"]:
                original_surf.fill((0, 0, 0, 0)) 
                pygame.draw.rect(original_surf, 'red', original_surf.get_rect(), border_width)
                inner_size_width = 20 - 4 * border_width
                inner_size_height = 40 - 4 * border_width
                inner_rect = pygame.Rect(border_width+2, border_width+2, inner_size_width, inner_size_height)
                pygame.draw.rect(original_surf, 'red', inner_rect)
                self.display_surf.blit(original_surf, (x, y))
            else:
                original_surf.fill((0, 0, 0, 0)) 
                pygame.draw.rect(original_surf, 'red', original_surf.get_rect(), border_width)
                self.display_surf.blit(original_surf, (x, y))


    def update(self, dt):
        self.display_surf = pygame.display.get_surface()
        self.display_surf.fill("#1f1f1f")
        self.breach_button.draw(self.display_surf, dt)
        self.upgrade_button.draw(self.display_surf, dt)

        text = self.font3.render(str(self.game.infomation.TOTAL_BITS), False, (255, 75, 80))
        self.bit = pygame.Surface((self.game.infomation.WINDOW_WIDTH//5, text.get_height()+10), pygame.SRCALPHA)
        
        # self.rect = self.image_bit.get_frect(center = (100, 100))
        self.bit.fill((0, 0, 0, 0)) 
        
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
                self.game.infomation.WINDOW_WIDTH//5 - text.get_width() - 12,
                (text.get_height()+10 - text.get_height())//2
            )
        )
        pygame.draw.rect(self.bit, 'red', self.bit.get_rect(), self.border_width)
        self.display_surf.blit(self.bit, ((self.game.infomation.WINDOW_WIDTH - self.game.infomation.WINDOW_WIDTH//50 - self.game.infomation.WINDOW_WIDTH//5), self.game.infomation.WINDOW_HEIGHT//50))

        #upgrade
        self.images(self.image_atk, self.game.infomation.WINDOW_WIDTH//50, self.game.infomation.WINDOW_HEIGHT/9)
        self.upgrade(self.game.infomation.WINDOW_WIDTH//50 + (self.game.infomation.WINDOW_WIDTH/30), self.game.infomation.WINDOW_HEIGHT//9 + self.game.infomation.WINDOW_WIDTH//30-40, self.game.infomation.damage, dt)
        if self.game.infomation.TOTAL_BITS < self.game.infomation.damage["cost"][str(self.game.infomation.damage["curr_lvl"]+1)]["cost"]:
            self.damage_button = Button(
                self.game.infomation.WINDOW_WIDTH//50 + (self.game.infomation.WINDOW_WIDTH/30) + 30 * 16, 
                self.game.infomation.WINDOW_HEIGHT//9 + self.game.infomation.WINDOW_WIDTH//30-40, 
                self.game.infomation.WINDOW_WIDTH/30*3, 
                self.game.infomation.WINDOW_WIDTH/30, 
                self.game.infomation.damage["cost"][str(self.game.infomation.damage["curr_lvl"] + 1)]["cost"], 
                self.font, 
                (31, 31, 31), 
                (255, 255, 255)
            )
            self.damage_button.draw(self.display_surf, dt)
        else:
            self.damage_button = Button(
                self.game.infomation.WINDOW_WIDTH//50 + (self.game.infomation.WINDOW_WIDTH/30) + 30 * 16, 
                self.game.infomation.WINDOW_HEIGHT//9 + self.game.infomation.WINDOW_WIDTH//30-40, 
                self.game.infomation.WINDOW_WIDTH/30*3, 
                self.game.infomation.WINDOW_WIDTH/30, 
                self.game.infomation.damage["cost"][str(self.game.infomation.damage["curr_lvl"] + 1)]["cost"], 
                self.font, 
                (255, 75, 80), 
                (255, 255, 255)
            )
            self.damage_button.draw(self.display_surf, dt)

        self.images(self.image_def, self.game.infomation.WINDOW_WIDTH//50, (self.game.infomation.WINDOW_HEIGHT/9) + (self.game.infomation.WINDOW_HEIGHT/9))
        self.upgrade(self.game.infomation.WINDOW_WIDTH//50 + (self.game.infomation.WINDOW_WIDTH/30), self.game.infomation.WINDOW_HEIGHT//9 + self.game.infomation.WINDOW_WIDTH//30-40 +  (self.game.infomation.WINDOW_HEIGHT/9), self.game.infomation.shield, dt)
        if self.game.infomation.TOTAL_BITS < self.game.infomation.shield["cost"][str(self.game.infomation.shield["curr_lvl"]+1)]["cost"]:
            self.shield_button = Button(
                self.game.infomation.WINDOW_WIDTH//50 + (self.game.infomation.WINDOW_WIDTH/30) + 30 * 16, 
                self.game.infomation.WINDOW_HEIGHT//9 + self.game.infomation.WINDOW_WIDTH//30-40 +  (self.game.infomation.WINDOW_HEIGHT/9), 
                self.game.infomation.WINDOW_WIDTH/30*3, 
                self.game.infomation.WINDOW_WIDTH/30, 
                self.game.infomation.shield["cost"][str(self.game.infomation.shield["curr_lvl"] + 1)]["cost"], 
                self.font, 
                (31, 31, 31), 
                (255, 255, 255)
            )
            self.shield_button.draw(self.display_surf, dt)
        else:
            self.shield_button = Button(
                self.game.infomation.WINDOW_WIDTH//50 + (self.game.infomation.WINDOW_WIDTH/30) + 30 * 16, 
                self.game.infomation.WINDOW_HEIGHT//9 + self.game.infomation.WINDOW_WIDTH//30-40 +  (self.game.infomation.WINDOW_HEIGHT/9), 
                self.game.infomation.WINDOW_WIDTH/30*3, 
                self.game.infomation.WINDOW_WIDTH/30, 
                self.game.infomation.shield["cost"][str(self.game.infomation.shield["curr_lvl"] + 1)]["cost"], 
                self.font, 
                (255, 75, 80), 
                (255, 255, 255)
            )
            self.shield_button.draw(self.display_surf, dt)
        
            


        self.images(self.image_health, self.game.infomation.WINDOW_WIDTH//50, (self.game.infomation.WINDOW_HEIGHT/9) + (self.game.infomation.WINDOW_HEIGHT/9)*2)
        self.upgrade(self.game.infomation.WINDOW_WIDTH//50 + (self.game.infomation.WINDOW_WIDTH/30), self.game.infomation.WINDOW_HEIGHT//9 + self.game.infomation.WINDOW_WIDTH//30-40 + (self.game.infomation.WINDOW_HEIGHT/9)*2, self.game.infomation.hp, dt)
        if self.game.infomation.TOTAL_BITS < self.game.infomation.shield["cost"][str(self.game.infomation.shield["curr_lvl"]+1)]["cost"]:
            self.hp_button = Button(
                self.game.infomation.WINDOW_WIDTH//50 + (self.game.infomation.WINDOW_WIDTH/30) + 30 * 16, 
                self.game.infomation.WINDOW_HEIGHT//9 + self.game.infomation.WINDOW_WIDTH//30-40 + (self.game.infomation.WINDOW_HEIGHT/9)*2, 
                self.game.infomation.WINDOW_WIDTH/30*3, 
                self.game.infomation.WINDOW_WIDTH/30, 
                self.game.infomation.hp["cost"][str(self.game.infomation.hp["curr_lvl"] + 1)]["cost"], 
                self.font, 
                (31, 31, 31), 
                (255, 255, 255)
            )
            self.hp_button.draw(self.display_surf, dt)
        else:
            self.hp_button = Button(
                self.game.infomation.WINDOW_WIDTH//50 + (self.game.infomation.WINDOW_WIDTH/30) + 30 * 16, 
                self.game.infomation.WINDOW_HEIGHT//9 + self.game.infomation.WINDOW_WIDTH//30-40 + (self.game.infomation.WINDOW_HEIGHT/9)*2, 
                self.game.infomation.WINDOW_WIDTH/30*3, 
                self.game.infomation.WINDOW_WIDTH/30, 
                self.game.infomation.hp["cost"][str(self.game.infomation.hp["curr_lvl"] + 1)]["cost"], 
                self.font, 
                (255, 75, 80), 
                (255, 255, 255)
            )
            self.hp_button.draw(self.display_surf, dt)
            

from settings import *
from random import *
import pygame
from os.path import join

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, collision_sprites, exp_collision, game, info):
        super().__init__(groups)
        self.infomation = info
        self.original_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.image = self.original_surf.copy()
        self.rect = self.image.get_frect(center=pygame.mouse.get_pos())
        self.collision_sprites = collision_sprites
        self.exp_sprite = exp_collision
        self.game = game


        self.hit_loot_surf = pygame.Surface((self.original_surf.get_width() - 20, self.original_surf.get_width() - 20))  # Ensure this is a Surface
        self.rect_hit_loot = self.hit_loot_surf.get_frect(center = self.rect.center)
        # print(self.image.get_width())
        self.scale_point = 1.0 
        self.max_scale = 1.5 
        self.min_scale = 1.0
        self.scale_speed = 0.5
        self.cooldown = 1000  
        self.time_shoot = 0   
        self.bounce = False 
        self.min = False
        
        self.can_shoot = False

    def collision(self):
        for sprite in self.exp_sprite:
            if sprite.rect.colliderect(self.rect_hit_loot):
                sprite.start = True 
                sprite.pick = True

    def shoot(self, dt):
        self.scale_point = self.max_scale
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                # print('overlap')
                sprite.hp -= self.infomation.infomation.PLAYER_ATK
                sprite.get_hit = True
                sprite.update_image()
                sprite.scale_point = sprite.max_scale
        self.bounce = True

    def shoot_time(self, dt):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.time_shoot > self.cooldown:
                self.can_shoot = True
        else:
            self.shoot(dt)
            self.time_shoot = pygame.time.get_ticks() 
            self.can_shoot = False

    def scale_effect(self, dt):
        if self.scale_point <= 0.8:
            self.scale_speed = abs(self.scale_speed)
            self.min = True
        elif self.scale_point >= self.max_scale:
            self.scale_speed = -abs(self.scale_speed)
                
        self.scale_point += self.scale_speed * dt
        if self.scale_point >= self.min_scale and self.min:
            self.scale_point = self.min_scale
            self.bounce = False
            self.min = False

        new_width = int(self.original_surf.get_width() * self.scale_point)
        new_height = int(self.original_surf.get_height() * self.scale_point)
        self.image = pygame.transform.scale(self.original_surf, (new_width, new_height))
        self.rect = self.image.get_rect(center=self.rect.center)



    def update(self, dt, game):
        self.rect.center = pygame.mouse.get_pos()
        self.rect_hit_loot.center = self.rect.center
        self.shoot_time(dt)
        self.infomation.infomation.PLAYER_HEALTH -= self.infomation.infomation.HP_LOST_PER_SEC * dt
        if self.infomation.infomation.PLAYER_HEALTH <= 0:
            self.infomation.infomation.IS_TERMINATED = True
        game.update_image()
        print(self.infomation.infomation.PLAYER_HEALTH)
        if self.bounce:
            self.scale_effect(dt)
        self.collision()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, all_sprite, exp_sprite, game):
        super().__init__(groups)
        self.size = 0
        self.init_size()
        self.game = game

        self.original_surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.image = self.original_surf

        self.pos = pygame.Vector2()
        self.init_pos()
        self.rect = self.image.get_frect(center = self.pos)

        self.direction = pygame.Vector2()
        self.init_diretion()
        self.speed = 5
        self.rotation = 0
        self.rotation_direct = randint(-80, 80)
        self.get_hit = False
        self.scale_point = 1.0 
        self.max_scale = 3.0
        self.min_scale = 1.0
        self.scale_speed = 2
        # print(self.pos)
        self.update_image()
        #info

        #exp
        self.all_sprite = all_sprite
        self.exp_sprite = exp_sprite

    def collision(self):
        pass

    def init_size(self):
        if randint(1, 100) < 95:
            self.size = 30
            self.hp_full = 5
            self.hp = 5
            self.exp = 10
        else:
            self.size = 70
            self.hp_full = 12
            self.hp = 12
            self.exp = 10

    def init_pos(self):
        if randint(0, 1):
            self.pos.x = randint(0, self.game.infomation.WINDOW_WIDTH)
            self.pos.y = randint(-(self.size-10), 0) if randint(0, 1) == 0 else randint(self.game.infomation.WINDOW_HEIGHT, self.game.infomation.WINDOW_HEIGHT + (self.size-10))
        else:
            self.pos.y = randint(0, self.game.infomation.WINDOW_WIDTH)
            self.pos.x = randint(-(self.size-10), 0) if randint(0, 1) == 0 else randint(self.game.infomation.WINDOW_WIDTH, self.game.infomation.WINDOW_WIDTH + (self.size-10))

    def init_diretion(self):
        if self.pos[0] < 0:
            self.direction.x = uniform(0.5, 1)
            if self.pos[1] < 0:
                self.direction.y = uniform(0.5, 1)
            if self.pos[1] > 0:
                self.direction.y = uniform(-1, -0.5)
        if self.pos[0] > 0:
            self.direction.x = uniform(-1, -0.5)
            if self.pos[1] < 0:
                self.direction.y = uniform(0.5, 1)
            if self.pos[1] > 0:
                self.direction.y = uniform(-1, -0.5)
        # print(self.direction)

    def update_image(self):
        self.original_surf.fill((0, 0, 0, 0)) 
        
        border_width = 2
        pygame.draw.rect(self.original_surf, 'red', self.original_surf.get_rect(), border_width)

        inner_size = self.size - 2 * border_width
        inner_rect = pygame.Rect(border_width, border_width, inner_size, inner_size * ((self.hp/self.hp_full)))
        pygame.draw.rect(self.original_surf, 'red', inner_rect)

        self.image = pygame.transform.rotate(self.original_surf, self.rotation)

    def movement(self, dt):
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.x += dt*self.direction.x*self.speed
        self.rect.y += dt*self.direction.y*self.speed
        
    def update(self, dt):
        self.movement(dt)
        if self.rect.x > self.game.infomation.WINDOW_WIDTH + self.size or self.rect.x < -self.size or self.rect.y > self.game.infomation.WINDOW_HEIGHT +  self.size or self.rect.y < - self.size or self.hp < 0:
            if self.hp < 0:
                for i in range(0, self.exp):
                    exp(self.rect, self.size, (self.all_sprite, self.exp_sprite), self.game)
            self.kill()
        if self.get_hit:
            self.scale_point -= self.scale_speed * dt
            if self.scale_point <= self.min_scale:
                self.scale_point = self.min_scale
                self.get_hit = False
        
        self.rotation += self.rotation_direct * dt * 0.1
        self.image = pygame.transform.rotate(self.original_surf, self.rotation)
        self.rect = self.image.get_frect(center=self.rect.center)


class exp(pygame.sprite.Sprite):
    def __init__(self, pos, size ,groups, infomation):
        super().__init__(groups)
        self.infomation = infomation.infomation
        self.image = pygame.image.load(join('images', 'exp.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (pos.x + randint(size//4, size), pos.y + randint(size//4, size)))
        self.get_pos = pos
        self.bits = 0
        
        self.colected = False
        self.goal_point = pygame.Vector2(100, 100)
        self.direction = pygame.Vector2()
        if self.rect.centerx > self.get_pos.x:
            self.direction.x = -1
            self.direction.y = -0.2
        else:
            self.direction.x = 1
            self.direction.y = -0.2
        self.start = False
        self.goal = False
        self.speed = 20
        self.pick = False
    def collision(self, dt):
        if self.start:
            self.rect.centerx += self.direction.x*dt*self.speed
            self.rect.centery += self.direction.y*dt*self.speed
            if self.rect.centerx - self.get_pos.x > 100 or self.rect.centerx - self.get_pos.x < -100:
                self.direction.x = (self.goal_point.x - self.rect.centerx)/abs(self.goal_point.x - self.rect.centerx)
                self.direction.y = (self.goal_point.y - self.rect.centery)/abs(self.goal_point.x - self.rect.centerx)
                self.start = False
                self.goal = True
        if self.goal:
            self.rect.centerx += self.direction.x*dt*self.speed
            self.rect.centery += self.direction.y*dt*self.speed
            if self.rect.x < self.goal_point.x + 30 and self.rect.x > self.goal_point.x - 30:
                self.goal = False
                self.pick = False
                self.kill()
                self.infomation.BITS +=1
                # print(self.infomation.BITS)

    def update(self, dt):
        if self.pick:
            self.collision(dt)
        # print(self.get_pos.x)

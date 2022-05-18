import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):

    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (SC_WIDTH/2, SC_HEIGHT/2)
        self.speed = vec(0, 0)
        self.acc = vec(0, 0)
        self.pos = vec(SC_WIDTH/2, SC_HEIGHT/2)
        

    def update(self):
        
        self.acc = vec(0, GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        if keys[pg.K_SPACE]:
            self.jump()
            
        self.acc.x += self.speed.x * PLAYER_FRICTION
        self.speed += self.acc
        self.pos += self.speed + 0.5 * self.acc
        self.rect.midbottom = self.pos

        if self.pos.x < 0:
            self.pos.x = SC_WIDTH
            
        elif self.pos.x > SC_WIDTH:
            self.pos.x = 0

    def jump(self):
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.platform_sprites, False)
        self.rect.y -= 1
        if hits:
            self.is_jump = True
            self.speed.y = PLAYER_JUMP_SPEED

class Platform(pg.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y








        

    

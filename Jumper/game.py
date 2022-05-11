import pygame as pg
import random
from settings import *
from sprites import *


class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SC_WIDTH, SC_HEIGHT))
        self.running = True
        self.clock = pg.time.Clock()

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.platform_sprites = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        
        for plat in PLATFORM_LIST:
            p1 = Platform(*plat)
            self.all_sprites.add(p1)
            self.platform_sprites.add(p1)
            
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()
        if self.player.speed.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platform_sprites,False)
            if hits:
                self.player.is_jump = False
                self.player.speed.y = 0
                self.player.pos.y = hits[0].rect.y
            

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass











    
    


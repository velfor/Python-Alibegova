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
        self.font_name = pg.font.match_font(FONT_NAME)

    def new(self):
        self.score = 0
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
        #игрок запрыгнул выше 1/4 высоты экрана
        if self.player.rect.top <= SC_HEIGHT // 4:
            #игрок опускается вниз
            self.player.pos.y += abs(self.player.speed.y)
            #все платформы опускаются вниз
            for plat in self.platform_sprites:
                plat.rect.y += abs(self.player.speed.y)
                #если платформа опустилась ниже нижнего края экрана - убираем её
                if plat.rect.top > SC_HEIGHT:
                    plat.kill()
                    self.score += 10
        #делаем новые платформы
        while len(self.platform_sprites) < PLATFORMS_QTY:
            width = random.randint(80, 160)
            p = Platform(random.randint(0, SC_WIDTH - width),
                         random.randint(-100, -20), width, 20)
            self.all_sprites.add(p)
            self.platform_sprites.add(p)
        #смерть игрока
        if self.player.rect.top > SC_HEIGHT:
            self.player.kill()
            self.playing = False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, WHITE, SC_WIDTH / 2, 15)
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)









    
    


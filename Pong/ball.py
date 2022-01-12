import pygame as pg
from const import *

class Ball:
    def __init__(self):
        self.x = SC_WIDTH // 2
        self.y = SC_HEIGHT // 2
        self.radius = 10
        self.speedx = 3
        self.speedy = 3
        self.score1 = 0
        self.score2 = 0

    def update(self):
        #движение мяча
        self.x += self.speedx
        self.y += self.speedy
        # отражение шара от левой границы, +1 очко 2-му игроку
        if self.x - self.radius <= 0:
            self.score2 += 1
            self.speedx = -self.speedx
        # отражение шара от правой границы, +1 очко 1-му игроку  
        if self.x + self.radius >= SC_WIDTH:
            self.score1 += 1
            self.speedx = -self.speedx
        #отражение от верхней или нижней границы
        if self.y - self.radius <= 0 or self.y + self.radius >= SC_HEIGHT:
            self.speedy = -self.speedy

    def draw(self,screen):
        pg.draw.circle(screen,YELLOW,(self.x,self.y),self.radius)

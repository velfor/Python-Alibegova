from const import *
import pygame

class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.speedy = 2
        self.speedx = 3
        self.r = 10
    
    def update(self):
        self.x += self.speedx
        self.y += self.speedy

        # отталкивание правой границы, очко получает левая (первая) ракетка
        if self.x + self.r > SCREEN_WIDTH:
            score1 += 1
            self.speedx = -self.speedx
        # отталкивание левой границы, очко получает правая (вторая) ракетка
        if self.x - self.r < 0:
            score2 += 1
            self.speed_x = -self.speedx
        # отталкивание от нижней и верхней границ
        if self.y + self.r > SCREEN_HEIGHT or self.y - self.r < 0:
            self.speedy = -self.speedy
    
    def draw(self,screen):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.r)
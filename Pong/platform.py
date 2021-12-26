from const import *
import pygame

class Platform:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speedy = 10
        self.width = 10
        self.height = 80
        

    def update(self,down,up):
        keys = pygame.key.get_pressed()
        #если нажата стрелка вниз
        if keys[down]:
        #увеличиваем координату у прямоугольника
            self.y += self.speedy
        if keys[up]:
            self.y -= self.speedy
        if self.y < 0:
            self.y = 0
        if self.y + self.height > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.height

    def draw(self,screen):
        pygame.draw.rect(screen,WHITE,(self.x, self.y, self.width , self.height))
    

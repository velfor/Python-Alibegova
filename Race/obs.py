import pygame
from const import *
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,starty):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("obs.png").convert_alpha()
        self.image = pygame.transform.scale(img, (100,30))
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(0, SC_WIDTH - self.rect.width)
        self.rect.bottom = starty
        self.speedy = 3
        self.score = 0

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top >= SC_HEIGHT:
            self.rect.left = random.randint(0, SC_WIDTH - self.rect.width)
            self.rect.bottom = 0
            self.score += 1
            if self.score % 10 == 0:
                self.speedy += 1






                
        

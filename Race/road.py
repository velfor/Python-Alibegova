import pygame
from const import *

class Road(pygame.sprite.Sprite):
    def __init__(self,starty):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("road1.jpg").convert()
        self.image = pygame.transform.scale(img,(SC_WIDTH,SC_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.top = starty
        self.rect.left = 0
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top >= SC_HEIGHT:
            self.rect.bottom = 0 

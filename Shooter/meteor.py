import pygame
from const import *
import random

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(IMG_DIR + "meteorBrown_big1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.random_spawn()

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left <= 0 or self.rect.right >= SC_WIDTH:
            self.random_spawn()
        if self.rect.top >= SC_HEIGHT:
            self.random_spawn()
            
    def random_spawn(self):
        self.rect.left = random.randint(0, SC_WIDTH - self.rect.width)
        self.rect.bottom = random.randint(-SC_HEIGHT, 0)
        self.speedx = random.randint(-1, 1)
        self.speedy = random.randint(3, 6)





                
        

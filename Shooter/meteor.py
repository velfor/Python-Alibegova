import pygame
from const import *
import random

class Meteor(pygame.sprite.Sprite):
    file_name_list = ["meteorBrown_big1.png", "meteorBrown_big2.png",
                        "meteorBrown_med1.png", "meteorBrown_med2.png",
                        "meteorBrown_small1.png", "meteorBrown_small2.png",
                        "meteorBrown_tiny1.png", "meteorBrown_tiny2.png"]   

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        number = random.randint(0,7)
        file_name = IMG_DIR + Meteor.file_name_list[number]
        self.image = pygame.image.load(file_name).convert_alpha()
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





                
        

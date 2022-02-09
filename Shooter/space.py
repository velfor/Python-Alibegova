import pygame
from const import *

class Space(pygame.sprite.Sprite):
    def __init__(self, x , y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(IMG_DIR + SPACE_IMG_FILE_NAME).convert()
        self.image = pygame.transform.scale(img, (SC_WIDTH, SC_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top >= SC_HEIGHT:
            self.rect.bottom = 0

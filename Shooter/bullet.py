import pygame
from const import *

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(IMG_DIR + BULLET_IMG_FILE_NAME)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = BULLET_SPEED

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom <= 0:
            self.kill()
        

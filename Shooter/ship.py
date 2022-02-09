import pygame
from const import *

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(IMG_DIR + PLAYER_IMG_FILE_NAME).convert()
        #self.image = pygame.transform.scale(img, (SC_WIDTH, SC_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.centerx = SC_WIDTH // 2
        self.rect.bottom = SC_HEIGHT - 20
        self.speedx = 5

    def update(self):
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.speedx = -5
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SC_WIDTH:
            self.rect.right = SC_WIDTH
        

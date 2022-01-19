import pygame
from const import *

class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("car.png").convert_alpha()
        self.image = pygame.transform.scale(img,(40,80))
        self.rect = self.image.get_rect()
        self.rect.bottom = SC_HEIGHT - 10
        self.rect.centerx = SC_WIDTH // 2
        self.speed = 10

    def update(self):
        keys = pygame.key.get_pressed()
        #движение по клавишам
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        # проверка на выход за границы окна
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SC_WIDTH:
            self.rect.right = SC_WIDTH









            
        
        

import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self):
        self.image = pg.image.load("Base pack/Player/p3_stand.png")
        self.rect = self.image.get_rect()
        self.rect.center = (250, 250)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

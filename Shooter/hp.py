import pygame
from const import *

class HpBar:

    def __init__(self, screen):
        self.screen = screen
        self.height = HP_BAR_HEIGHT
        self.x = HP_BAR_X
        self.y = HP_BAR_Y
        

    def update(self, hp):
        size = 0
        if hp > 0:
            size = hp
        self.width = HP_BAR_WIDTH * size / PLAYER_HP;
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.circuit_rect = pygame.Rect(self.x, self.y,HP_BAR_WIDTH,self.height)
        

    def draw(self):
        pygame.draw.rect(self.screen, GREEN, self.rect)
        pygame.draw.rect(self.screen, WHITE, self.circuit_rect, 2)




        

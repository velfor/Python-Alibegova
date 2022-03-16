import pygame

class Explosion(pygame.sprite.Sprite):

    def __init__(self, center, explosion_anim, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.explosion_anim = explosion_anim
        self.image = self.explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.frame_delay = 50
        self.last_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_delay:
            self.last_update = now
            self.frame += 1
            if self.frame < 9:
                old_center = self.rect.center
                self.image = self.explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = old_center
            else:
                self.kill()






                
        

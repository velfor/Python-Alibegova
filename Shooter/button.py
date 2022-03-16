import pygame

class Button:
    def __init__(self, width, height, inactive_color, active_color):
        self.width = width
        self.height= height
        self.inactive_color = inactive_color
        self.active_color = active_color

    def draw(x,y, message, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(screen, self.active_color, (x,y, self.width, self.height))
            #звук если мышка нажата на кнопке
            if click[0] == 1 and action is not None:
                #pygame.mixer.sound.play(button_sound)
                #pygame.time.delay(button_delay)
                action()
            
        else:
            pygame.draw.rect(screen, self.inactive_color, (x,y, self.width, self.height))

import pygame
import sys
from const import *
from car import Car

#создаем окно приложения
screen = pygame.display.set_mode((SC_WIDTH,SC_HEIGHT))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

car = Car()
all_sprites.add(car)
#0 секция - создание игровых объектов


# бесконечный игровой цикл
while True:
    # 1 секция - обработка ввода пользователя
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 2 секция - обновление игровых объектов, update
    all_sprites.update()
    # 3 секция - перерисовка экрана
    #3.1 залить экран цветом фона (или вывести картинку фона)
    screen.fill(WHITE)
    #3.2 нарисовать объекты
    all_sprites.draw(screen)
    #3.3 обновление экрана
    pygame.display.flip()

    # задержка для постоянной скорости игры на разных компах
    clock.tick(FPS)

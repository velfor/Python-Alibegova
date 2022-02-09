import pygame
import sys
from const import *
from space import Space
from ship import Ship
from meteor import Meteor

#создаем окно приложения
screen = pygame.display.set_mode((SC_WIDTH,SC_HEIGHT))
clock = pygame.time.Clock()
#0 секция - создание игровых объектов
space1 = Space(0, 0)
space2 = Space(0, -SC_HEIGHT)
player = Ship()
meteors = []
for i in range(10):
    m = Meteor()
    meteors.append(m)
# группы
all_sprites = pygame.sprite.Group()
# добавление объектов в группы
all_sprites.add(space1)
all_sprites.add(space2)
all_sprites.add(player)
for m in meteors:
    all_sprites.add(m)
# игровой цикл
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
    screen.fill(BLACK)
    #3.2 нарисовать объекты
    all_sprites.draw(screen)
    #3.3 обновление экрана
    pygame.display.flip()

    # задержка для постоянной скорости игры на разных компах
    clock.tick(FPS)

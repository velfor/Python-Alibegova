import pygame as pg
import sys
from player import Player

#создаем окно приложения
screen = pg.display.set_mode((500,500))
clock = pg.time.Clock()
#0 секция - создание игровых объектов
player = Player()
# бесконечный игровой цикл
while True:
    # 1 секция - обработка ввода пользователя
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    # 2 секция - обновление игровых объектов, update
    player.update()
    # 3 секция - перерисовка экрана
    #3.1 залить экран цветом фона (или вывести картинку фона)
    screen.fill((0,0,0))
    #3.2 нарисовать объекты
    player.draw(screen)
    #3.3 обновление экрана
    pg.display.flip()

    # задержка для постоянной скорости игры на разных компах
    clock.tick(60)

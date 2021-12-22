import pygame as pg
import sys
from const import *



#создаем окно приложения
screen = pg.display.set_mode((SC_WIDTH,SC_HEIGHT))

#0 секция - создание игровых объектов

clock = pg.time.Clock()
c_x = SC_WIDTH // 2
c_y = SC_HEIGHT // 2
radius = 10
c_speedx = 2
c_speedy = 3
# для прямоугольника 4 переменные:
# первые 2 - координаты верхнего левого угла
# вторые 2 - длина и ширина
r_width = 20
r_height = 80
r1_x = r_width
r1_y = SC_HEIGHT//2 - r_height//2
r2_x = SC_WIDTH - 2*r_width
r2_y = SC_HEIGHT//2 - r_height//2
r_speedy = 5


# бесконечный игровой цикл
while True:
    # 1 секция - обработка ввода пользователя
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    # 2 секция - обновление игровых объектов, update
    #движение круга
    c_x += c_speedx
    c_y += c_speedy
    # отражение шара от левой или правой границы
    if c_x - radius <= 0 or c_x + radius >= SC_WIDTH:
        c_speedx = -c_speedx
    #отражение от верхней или нижней границы
    if c_y - radius <= 0 or c_y + radius >= SC_HEIGHT:
        c_speedy = -c_speedy

    
    keys = pg.key.get_pressed()
    #движение правой ракетки по клавишам-стрелкам
    if keys[pg.K_UP]:
        r2_y -= r_speedy
    elif keys[pg.K_DOWN]:
        r2_y += r_speedy
    #не даём выйти правой ракетке за границы экрана
    if r2_y <= 0:
        r2_y = 0
    if r2_y >= SC_HEIGHT - r_height:
        r2_y = SC_HEIGHT - r_height
    #движение левой ракетки по клавишам-стрелкам
    if keys[pg.K_w]:
        r1_y -= r_speedy
    elif keys[pg.K_s]:
        r1_y += r_speedy    
    #не даём выйти левой ракетке за границы экрана
    if r1_y <= 0:
        r1_y = 0
    if r1_y >= SC_HEIGHT - r_height:
        r1_y = SC_HEIGHT - r_height
    
    # 3 секция - перерисовка экрана
    #3.1 залить экран цветом фона (или вывести картинку фона)
    screen.fill(BLACK)
    #3.2 нарисовать объекты
    pg.draw.rect(screen,WHITE, (r1_x,r1_y,r_width,r_height))
    pg.draw.rect(screen,WHITE, (r2_x,r2_y,r_width,r_height))
    pg.draw.circle(screen,YELLOW,(c_x,c_y),radius)
    #3.3 обновление экрана
    pg.display.flip()

    # задержка для постоянной скорости игры на разных компах
    clock.tick(FPS)

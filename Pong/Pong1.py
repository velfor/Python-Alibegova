import pygame as pg
import sys
from const import *
from ball import Ball

#создаем окно приложения
screen = pg.display.set_mode((SC_WIDTH,SC_HEIGHT))
pg.display.set_caption("My little Pong")
#0 секция - создание игровых объектов
# часы для контроля скорости игры
clock = pg.time.Clock()
#создаем мяч
ball = Ball()
# создаем шрифт
pg.font.init()
font = pg.font.SysFont('arial',28)
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
score1 = 0
score2 = 0

# бесконечный игровой цикл
while True:
    # 1 секция - обработка ввода пользователя
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    # 2 секция - обновление игровых объектов, update
    ball.update()
    
    # надписи для счетов
    score1_text = font.render(str(ball.score1),True,WHITE)
    score2_text = font.render(str(ball.score2),True,WHITE)
    
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

    #мяч попал в левую ракетку (только передняя поверхность)
    if (ball.y >= r1_y and ball.y <= r1_y + r_height) and (
        ball.x - ball.radius <= r1_x + r_width):
        ball.speedx = -ball.speedx
    #мяч попал в правую ракетку
    if (ball.y >= r2_y and ball.y <= r2_y + r_height) and (
        ball.x + ball.radius >= r2_x):
        ball.speedx = -ball.speedx
        
    # 3 секция - перерисовка экрана
    #3.1 залить экран цветом фона (или вывести картинку фона)
    screen.fill(BLACK)
    #3.2 нарисовать объекты
    pg.draw.rect(screen,WHITE, (r1_x,r1_y,r_width,r_height))
    pg.draw.rect(screen,WHITE, (r2_x,r2_y,r_width,r_height))
    #pg.draw.circle(screen,YELLOW,(c_x,c_y),radius)
    ball.draw(screen)
    screen.blit(score1_text,(100,10))
    screen.blit(score2_text,(SC_WIDTH-120,10))
    #3.3 обновление экрана
    pg.display.flip()

    # задержка для постоянной скорости игры на разных компах
    clock.tick(FPS)

import pygame
import sys
from const import *
from platform import Platform
from ball import Ball

# создание окна программы
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#создаем таймер для управления скоростью игры
clock = pygame.time.Clock()

# создаем игровые объекты
# переменные для сторон
a = 10
b = 80
left_paddle = Platform(20,SCREEN_HEIGHT // 2 - b//2)
right_paddle = Platform(SCREEN_WIDTH - 20 - a, SCREEN_HEIGHT // 2 - b//2)
ball = Ball()
# переменные для счета
score1 = 0
score2 = 0
#инициализация подмодуля font
pygame.font.init()
# создаем системный шрифт (имя шрифта, размер)
font = pygame.font.SysFont('Arial',36)

# основной игровой цикл
while True:
    #№ 1 - обработка игровых событий (ввод пользователя)
    for event in pygame.event.get():
        #если тип события - ВЫХОД
        if event.type == pygame.QUIT:
            #остановить модули библиотеки
            pygame.quit()
            #закрыть окно программы
            sys.exit()
        # если тип события - КЛАВИША НАЖАТА
##        if event.type == pygame.KEYDOWN:
##            #если нажата стрелка вниз
##            if event.key == pygame.K_DOWN:
##                #увеличиваем координату у прямоугольника
##                r_y += r_speedy
##            if event.key == pygame.K_UP:
##                r_y -= r_speedy
   
    #№ 2 - изменение состояния игровых объектов
    # =====КРУГ=====
    ball.update()
    #управление с клавиатуры левой ракеткой
    left_paddle.update(pygame.K_DOWN,pygame.K_UP)
    #управление с клавиатуры правой ракеткой
    right_paddle.update(pygame.K_s,pygame.K_w)

    #=====Отражение мяча от левой ракетки=====
    if (ball.x - ball.r <= left_paddle.x + a) and (ball.y + ball.r >= left_paddle.y) and
    (ball.y - ball.r <= left_paddle.y + b):
        ball.speedx = -ball.speedx
    #=====Отражение мяча от правой ракетки=====    
    if (ball.x + ball.r >= right_paddle.x) and (ball.y + r >= right_paddle.y) and 
    (ball.y - ball.r <= right_paddle.y + b):
        ball.speedx = -ball.speedx
    # текст для счета левой ракетки
    score1_text = font.render(str(score1),True,WHITE)
    # текст для счета правой ракетки
    score2_text = font.render(str(score2),True,WHITE)
    # № 3 - перерисовка экрана
    screen.fill(BLACK)
    ball.draw(screen)
    left_paddle.draw(screen)
    right_paddle.draw(screen)
    screen.blit(score1_text, (100,50))
    screen.blit(score2_text, (SCREEN_WIDTH - 100,50))
    pygame.display.flip()
    
        
    # задержка, чтобы скорость игры была постоянной на любых компах
    clock.tick(FPS)

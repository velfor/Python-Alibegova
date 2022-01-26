import pygame
import sys
from const import *
from car import Car
from obs import Obstacle
from road import Road

pygame.init()

#функция для отображения текста
def draw_text(screen, string, size, x, y, color):
    font = pygame.font.Font('miratrix.otf', size)
    text_surf = font.render(string, True, color)
    text_rect = text_surf.get_rect()
    text_rect.x = x
    text_rect.y = y
    screen.blit(text_surf, text_rect)
    
#создаем окно приложения
screen = pygame.display.set_mode((SC_WIDTH,SC_HEIGHT))
pygame.display.set_caption("CODEWARTS RACE")
clock = pygame.time.Clock()
#0 секция - создание игровых объектов
car = Car()
obs1 = Obstacle(0)
obs2 = Obstacle(-SC_HEIGHT//2)
road = Road(0)
road1 = Road(-SC_HEIGHT)
#0-1 группы
all_sprites = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group()
#0-2 добавление в группы
all_sprites.add(road)
all_sprites.add(road1)
all_sprites.add(car)
all_sprites.add(obs1)
all_sprites.add(obs2)
obstacles_group.add(obs1)
obstacles_group.add(obs2)
# бесконечный игровой цикл
while True:
    # 1 секция - обработка ввода пользователя
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 2 секция - обновление игровых объектов, update
    all_sprites.update()
    # 2-1 проверка столкновений
    hits = pygame.sprite.spritecollide(car, obstacles_group, False)
    if hits:
        pygame.quit()
        sys.exit()
    # 3 секция - перерисовка экрана
    #3.1 залить экран цветом фона (или вывести картинку фона)
    screen.fill(WHITE)
    #3.2 нарисовать объекты
    all_sprites.draw(screen)
    draw_text(screen, "Score: "+str(obs1.score+obs2.score), 24, 10, 5, YELLOW)
    #3.3 обновление экрана
    pygame.display.flip()

    # задержка для постоянной скорости игры на разных компах
    clock.tick(FPS)

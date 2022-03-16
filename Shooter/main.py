import pygame
import sys
from const import *
from space import Space
from ship import Ship
from meteor import Meteor
from bullet import Bullet
from hp import HpBar
from text import TextObject
from explosion import Explosion

#создаем окно приложения
screen = pygame.display.set_mode((SC_WIDTH,SC_HEIGHT))
clock = pygame.time.Clock()
pygame.init()
#0 секция - создание игровых объектов
space1 = Space(0, 0)
space2 = Space(0, -SC_HEIGHT)
player = Ship()
meteors = []
for i in range(10):
    m = Meteor()
    meteors.append(m)
hp_bar = HpBar(screen)
score_text = TextObject(5,5,lambda:str(player.score), YELLOW, "Arial", 20)
shoot_sound = pygame.mixer.Sound("res/sfx_laser1.ogg")
explosion_images = {}
explosion_images["large"] = []
explosion_images["small"] = []
for i in range(9):
    file_name = "images/regularExplosion0" + str(i) + ".png"
    img = pygame.image.load(file_name).convert_alpha()
    big_img = pygame.transform.scale(img, (73,73))
    small_img = pygame.transform.scale(img, (23,23))
    explosion_images["large"].append(big_img)
    explosion_images["small"].append(small_img)
# группы
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
# добавление объектов в группы
all_sprites.add(space1)
all_sprites.add(space2)
all_sprites.add(player)
for m in meteors:
    all_sprites.add(m)
    meteor_sprites.add(m)
# игровой цикл
play = True
while play:
    # 1 секция - обработка ввода пользователя
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        # стрельба
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == MOUSE_LEFT_BUTTON:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullet_sprites.add(bullet)
                shoot_sound.play()
                
                
    # 2 секция - обновление игровых объектов, update
    all_sprites.update()
    hp_bar.update(player.hp)
    #проверка столкновений
    #игрок с метеорами
    hits = pygame.sprite.spritecollide(player, meteor_sprites, True)
    for m in hits:
        player.hp -= m.rect.width // 2
    if player.hp <=0:
        player.kill()
        play = False
    #пули с метеорами
    bullet_hits = pygame.sprite.groupcollide(bullet_sprites, meteor_sprites,
                                             True, True)
    for meteor in bullet_hits:
        new_explosion = Explosion(meteor.rect.center, explosion_images, "large")
        all_sprites.add(new_explosion)
        m = Meteor()
        all_sprites.add(m)
        meteor_sprites.add(m)
        player.score += meteor.rect.width // 3

    
    # 3 секция - перерисовка экрана
    #3.1 залить экран цветом фона (или вывести картинку фона)
    screen.fill(BLACK)
    #3.2 нарисовать объекты
    all_sprites.draw(screen)
    hp_bar.draw()
    score_text.draw(screen)
    #3.3 обновление экрана
    pygame.display.flip()

    # задержка для постоянной скорости игры на разных компах
    clock.tick(FPS)

pygame.quit()
sys.exit()







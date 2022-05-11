import pygame as pg
from game import Game


game = Game()
game.show_start_screen()
while game.running:
    game.new()

game.show_go_screen()
pg.quit()

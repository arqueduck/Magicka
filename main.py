import pygame as pg
import sys

from code.game import Game #Importa a classe Game do arquivo game.py


game = Game()
game.run()

pg.quit()
sys.exit()
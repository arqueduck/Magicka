import pygame as pg
import sys
from code.score_db import init_db

from code.game import Game #Importa a classe Game do arquivo game.py

init_db()

game = Game()
game.run()

pg.quit()
sys.exit()
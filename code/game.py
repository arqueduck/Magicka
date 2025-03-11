#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
from code.const import *
from code.menu import Menu

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))    # Screen size

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
            
            # Check for events
            # for event in pg.event.get():
            #     if event.type == pg.QUIT:
            #         pg.quit() # Close the window
            #         print("Main loop finished")
            #         quit()    # Close the program




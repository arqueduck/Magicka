#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pygame as pg
from code.level import Level
from code.const import *
from code.menu import Menu

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))    # Screen size

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                print("Starting game")
                level = Level(self.window, "Level 1", menu_return)
                level_return = level.run()
                if level_return == "Game Over":
                    continue
                
            elif menu_return == MENU_OPTION[2] or menu_return == "Quit":
                return
                
            else:
                pass
    
 

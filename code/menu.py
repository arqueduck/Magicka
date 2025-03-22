#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
from code.const import *

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load("./assets/MenuBg.png")
        self.rect = self.surf.get_rect(left=0, top=0)
        self.running = True
        

    def run(self):
        menu_option = 0
        pg.init()
        pg.mixer.init()
        pg.mixer_music.load("assets/menu_music.mp3")
        pg.mixer_music.play(-1)
        pg.mixer_music.set_volume(0.2)
        
        while self.running:
            ## Draw the background
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Magicka", (C_RED), ((WIN_WIDTH / 2), 200))
            ## Draw the menu options
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], (C_YELLOW), ((WIN_WIDTH / 2), 320 + i * 50))
                else:
                    self.menu_text(30, MENU_OPTION[i], (C_WHITE), ((WIN_WIDTH / 2), 320 + i * 50))
            pg.display.flip()
            
            ## Checks for events
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    return "Quit"
                    
                ## Check if a key is pressed
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP: ## Move up
                        menu_option = (menu_option - 1) % len(MENU_OPTION)
                    if event.key == pg.K_DOWN: ## Move down
                        menu_option = (menu_option + 1) % len(MENU_OPTION)
                    if event.key == pg.K_RETURN: ## Select option
                        return MENU_OPTION[menu_option] 
            

              
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos:tuple):
        font = pg.font.SysFont("Arial", text_size)
        text = font.render(text, True, text_color).convert_alpha()
        text_rect = text.get_rect(center=text_center_pos)
        self.window.blit(text, text_rect)

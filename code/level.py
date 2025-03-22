#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame as pg
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.const import *

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("Level1Bg", (0, 0)))
        self.timeout = 20000 # 20 seconds

    def run(self, ):
        pg.mixer_music.load(f"assets/gameplay_music.wav")
        pg.mixer_music.play(-1)
        pg.mixer_music.set_volume(0.2)
        clock = pg.time.Clock()
        
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()
                
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
            self.level_text(20, f"Level: {self.name} - Timeout: {self.timeout / 100:.1f}s", (C_WHITE), (WIN_WIDTH - 650, WIN_HEIGHT - 20))
            self.level_text(20, f"FPS: {clock.get_fps():.0f}", (C_WHITE), (WIN_WIDTH - 45, WIN_HEIGHT - 35))
            self.level_text(20, f"Entidades: {len(self.entity_list)}", (C_WHITE), (WIN_WIDTH - 70, WIN_HEIGHT - 20))
            pg.display.flip()
            pass
        
    def level_text(self, text_size: int, text: str, text_color: tuple, text_position:tuple):
        font = pg.font.SysFont("Arial", text_size)
        text = font.render(text, True, text_color).convert_alpha()
        text_rect = text.get_rect(center=text_position)
        self.window.blit(text, text_rect)
        pass

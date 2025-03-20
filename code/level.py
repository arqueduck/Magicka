#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from code.entity import Entity
from code.entityFactory import EntityFactory

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("Level1Bg", (0, 0)))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                ent.move()
                self.window.blit(ent.surf, ent.rect)
                ent.move()
            pg.display.flip()
            pass

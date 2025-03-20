#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, name: str, position: tuple,):
        self.name = name
        self.surf = pg.image.load(f"./assets/{name}.png")
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass

#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
from code.const import *
from code.entity import Entity


class Player(Entity):
    def __init__(self, name_prefix: str, position: tuple):
        # Don't load the image yet — we'll load all frames instead
        self.frames = [
            pg.transform.scale(
                pg.image.load(f"./assets/{name_prefix}_{i}.png"), (WIN_WIDTH // 3, WIN_HEIGHT // 4)
            )
            for i in range(10)
        ]
        self.frame_index = 0
        self.animation_speed = 100  # milliseconds per frame
        self.last_update = pg.time.get_ticks()
        self.movement_bounds = None
        
        # Use first frame for init
        self.surf = self.frames[0]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.name = name_prefix
        self.speed = ENTITY_SPEED["Player1"]

    def set_bounds(self, bounds: pg.Rect):
        self.movement_bounds = bounds

    def move(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rect.x += self.speed
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.rect.y += self.speed
            
        self.rect.x = max(0, min(self.rect.x, WIN_WIDTH - self.rect.width))    
        self.rect.y = max(0, min(self.rect.y, WIN_HEIGHT - self.rect.height))
        
        now = pg.time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.surf = self.frames[self.frame_index]
            self.last_update = now
            
        if self.movement_bounds:
            self.rect.clamp_ip(self.movement_bounds)
            

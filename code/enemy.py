#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
from code.const import *
from code.entity import Entity


class Enemy(Entity):
    shared_frames = None
    
    def __init__(self, sheet_path: str, frame_size: tuple, position: tuple):
        if Enemy.shared_frames is None:
            Enemy.shared_frames = []
            sheet = pg.image.load("assets/Bat_Sprite_Sheet.png").convert_alpha()
            frame_width, frame_height = frame_size
            
            for col in range(4):
                frame = sheet.subsurface((col * frame_width, 0, frame_width, frame_height))
                flipped = pg.transform.flip(frame, True, False)  # True = horizontal flip
                scaled = pg.transform.scale(flipped, (WIN_WIDTH // 10, WIN_HEIGHT // 10))
                Enemy.shared_frames.append(scaled)
            
        self.frames = Enemy.shared_frames
            
        self.frame_index = 0
        self.animation_speed = 80
        self.last_update = pg.time.get_ticks()

        self.surf = self.frames[0]
        self.rect = self.surf.get_rect(topleft=position)

        self.name = "Enemy"
        self.speed = ENTITY_SPEED["Enemy"]
        self.movement_bounds = None

    def set_bounds(self, bounds: pg.Rect):
        self.movement_bounds = bounds

    def move(self):
        self.rect.x -= self.speed  # Move left

        # Animate
        now = pg.time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.surf = self.frames[self.frame_index]
            self.last_update = now

        # Clamp inside bounds
        if self.movement_bounds:
            self.rect.clamp_ip(self.movement_bounds)
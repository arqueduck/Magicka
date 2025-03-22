#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame as pg
from code.const import *
from code.entity import Entity


class Player(Entity):
    def __init__(self, name_prefix: str, position: tuple):
        self.frames = [
            pg.transform.scale(
                pg.image.load(f"./assets/{name_prefix}_{i}.png"), (WIN_WIDTH // 3, WIN_HEIGHT // 4)
            )
            for i in range(10)
        ]
        
        self.attack_frames = [
            pg.transform.scale(
                pg.image.load(f"./assets/HeroKnight_Attack1_{i}.png"), (WIN_WIDTH // 3, WIN_HEIGHT // 4)
            )
            for i in range(6)
        ]
        
        # Run animation
        self.frame_index = 0
        self.animation_speed = 100  # milliseconds per frame
        self.last_update = pg.time.get_ticks()
        self.movement_bounds = None
        
        # Attack animation
        self.is_attacking = False
        self.attack_frame_index = 0
        self.attack_cooldown = 600
        self.last_attack_time = 0
        
        self.health = 3
        self.invulnerable = False
        self.invuln_duration = 1000  # 1 second
        self.last_hit_time = 0
        self.alive = True
        
        # Use first frame for init
        self.surf = self.frames[0]
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.name = name_prefix
        self.speed = ENTITY_SPEED["Player1"]

    def set_bounds(self, bounds: pg.Rect):
        self.movement_bounds = bounds

    def move(self):
        keys = pg.key.get_pressed()
        now = pg.time.get_ticks()  # <-- moved this to the top to fix the error

        if not self.is_attacking:
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                self.rect.x -= self.speed
            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.rect.x += self.speed
            if keys[pg.K_UP] or keys[pg.K_w]:
                self.rect.y -= self.speed
            if keys[pg.K_DOWN] or keys[pg.K_s]:
                self.rect.y += self.speed
            if keys[pg.K_SPACE] and now - self.last_attack_time > self.attack_cooldown:
                self.is_attacking = True
                self.attack_frame_index = 0
                self.last_attack_time = now

        if self.movement_bounds:
            self.rect.clamp_ip(self.movement_bounds)

        if self.invulnerable and pg.time.get_ticks() - self.last_hit_time > self.invuln_duration:
            self.invulnerable = False
        
        # Animate
        if self.is_attacking:
            if now - self.last_update > self.animation_speed:
                self.attack_frame_index += 1
                if self.attack_frame_index >= len(self.attack_frames):
                    self.is_attacking = False
                    self.attack_frame_index = 0
                else:
                    self.surf = self.attack_frames[self.attack_frame_index]
                    self.last_update = now
        else:
            if now - self.last_update > self.animation_speed:
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.surf = self.frames[self.frame_index]
                self.last_update = now

    def get_attack_rect(self):
        if not self.is_attacking:
            return None
        return pg.Rect(self.rect.right - 95, self.rect.top - 10, 90, self.rect.height +20)
    
    def take_damage(self):
        now = pg.time.get_ticks()
        if not self.invulnerable and self.alive:
            self.health -= 1
            self.last_hit_time = now
            self.invulnerable = True
            if self.health <= 0:
                self.alive = False

    def get_hurtbox(self):
        width = self.rect.width * 0.5
        height = self.rect.height * 0.78
        offset_x = self.rect.width * 0.15
        offset_y = self.rect.height * 0.22

        return pg.Rect(
            self.rect.left + offset_x,
            self.rect.top + offset_y,
            width,
            height
        )
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame as pg
import random
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.const import *
from code.player import Player

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("Level1Bg", (0, 0)))
        self.entity_list.extend(EntityFactory.get_entity("Player1", (0, 0)))
        self.player_bounds = pg.Rect(0, WIN_HEIGHT/3.2, WIN_WIDTH, WIN_HEIGHT)
        self.enemy_spawn_delay = ENEMY_SPAWN_DELAY
        self.last_enemy_spawn = pg.time.get_ticks()
        self.timeout = 20000 # 20 seconds
        
        for ent in self.entity_list:
            if isinstance(ent, Player):
                ent.set_bounds(self.player_bounds)
            if hasattr(ent, "set_bounds"):
                ent.set_bounds(self.player_bounds)

    def run(self, ):
        pg.mixer_music.load(f"assets/gameplay_music.wav")
        pg.mixer_music.play(-1)
        pg.mixer_music.set_volume(0.2)
        clock = pg.time.Clock()
            
        while True:
            clock.tick(60)
            
            now = pg.time.get_ticks()
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
            enemy_count = sum(1 for ent in self.entity_list if getattr(ent, "name", "") == "Enemy")

            if now - self.last_enemy_spawn >= self.enemy_spawn_delay:
                self.last_enemy_spawn = now
                for _ in range(2):  # spawn 2 enemies
                    for _ in range(2):  # Spawn 2 enemies per cycle
                        spawn_x = WIN_WIDTH + 50  # Always spawn at right edge of screen
                        spawn_y = random.randint(self.player_bounds.top, self.player_bounds.bottom - 50)
                        
                        new_enemy = EntityFactory.get_entity("Enemy", (spawn_x, spawn_y))[0]
                        new_enemy.set_bounds(self.player_bounds)
                        self.entity_list.append(new_enemy)
                
            self.window.blit(pg.Surface((WIN_WIDTH, WIN_HEIGHT)), (0, 0))  # Optional: clear screen
            for ent in self.entity_list[:]:
                ent.move()
                    
                if getattr(ent, "name", "") == "Enemy" and ent.rect.left <= self.player_bounds.left:
                    self.entity_list.remove(ent)
                    continue
                    
            self.level_text(20, f"Level: {self.name} - Timeout: {self.timeout / 100:.1f}s", (C_WHITE), (WIN_WIDTH - 650, WIN_HEIGHT - 20))
            self.level_text(20, f"FPS: {clock.get_fps():.0f}", (C_WHITE), (WIN_WIDTH - 45, WIN_HEIGHT - 35))
            self.level_text(20, f"Entidades: {len(self.entity_list)}", (C_WHITE), (WIN_WIDTH - 70, WIN_HEIGHT - 20))
            
            for ent in self.entity_list:
                if "Level1Bg" in getattr(ent, "name", ""):
                    self.window.blit(ent.surf, ent.rect)
                    
            for ent in self.entity_list[:]:
                if "Level1Bg" not in getattr(ent, "name", ""):
                    ent.move()

                    if getattr(ent, "name", "") == "Enemy" and ent.rect.left <= self.player_bounds.left:
                        self.entity_list.remove(ent)
                        continue

                    self.window.blit(ent.surf, ent.rect)
                    pg.display.flip()
                    pass
        
    def level_text(self, text_size: int, text: str, text_color: tuple, text_position:tuple):
        font = pg.font.SysFont("Arial", text_size)
        text = font.render(text, True, text_color).convert_alpha()
        text_rect = text.get_rect(center=text_position)
        self.window.blit(text, text_rect)
        pass

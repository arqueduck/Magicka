#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame as pg
import random
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.const import *
from code.player import Player
from code.score_db import save_score

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
        self.score = 0
        self.paused = False
        self.start_time = None
        self.total_paused_time = 0
        self.pause_start = None
        self.remaining_time = 20000 # 20 seconds
        self.was_paused = False
        self.previous_tick = None
        
        for ent in self.entity_list:
            if isinstance(ent, Player):
                ent.set_bounds(self.player_bounds)
            if hasattr(ent, "set_bounds"):
                ent.set_bounds(self.player_bounds)

    def run(self, ):
        now = pg.time.get_ticks()
        pg.mixer_music.load(f"assets/gameplay_music.wav")
        pg.mixer_music.play(-1)
        pg.mixer_music.set_volume(0.2)
        self.start_time = pg.time.get_ticks()
        clock = pg.time.Clock()
            
        while True:
            clock.tick(60)
            
            now = pg.time.get_ticks()
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.paused = not self.paused
                        if self.paused:
                            self.pause_start = pg.time.get_ticks()
                            pg.mixer_music.set_volume(0.05)
                        else:
                            paused_duration = pg.time.get_ticks() - self.pause_start
                            self.total_paused_time += paused_duration
                            self.pause_start = None
                            pg.mixer_music.set_volume(0.2)

                    if self.paused and event.key == pg.K_SPACE:
                        return "Game Over"
                    
            if not self.paused:
                
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
                
                for ent in self.entity_list:
                    if "Level1Bg" in getattr(ent, "name", ""):
                        self.window.blit(ent.surf, ent.rect)
                        
                for ent in self.entity_list[:]:
                    if "Level1Bg" not in getattr(ent, "name", ""):
                        ent.move()
                        
                        if getattr(ent, "name", "") == "Enemy" and ent.rect.left <= self.player_bounds.left:
                            self.entity_list.remove(ent)
                            self.score += 1 # Survived an enemy +1 score
                            continue

                        self.window.blit(ent.surf, ent.rect)
                        
                        if isinstance(ent, Player) and ent.is_attacking:
                            attack_rect = ent.get_attack_rect()
                            hit_enemies = []
                            
                            for e in self.entity_list[:]:
                                if e.name == "Enemy" and attack_rect.colliderect(e.rect):
                                    self.entity_list.remove(e)
                                    hit_enemies.append(e)
                                    
                            if len(hit_enemies) == 1:
                                self.score += 3
                            elif len(hit_enemies) >= 2:
                                self.score += 5 * len(hit_enemies)
                                
                if self.previous_tick is not None:
                    delta = now - self.previous_tick
                    self.remaining_time = max(0, self.remaining_time - delta)
                self.previous_tick = now
            else:
                self.previous_tick = now
                                    
            player = None
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    player = ent
                    break

            # Check collision with enemies
            if player and player.alive:
                hurtbox = player.get_hurtbox()
                for ent in self.entity_list:
                    if ent.name == "Enemy" and hurtbox.colliderect(ent.rect):
                        player.take_damage()
            
            # Check remaining time          
            if self.remaining_time <= 0:
                self.level_text(50, "GAME OVER", C_RED, (WIN_WIDTH // 2, WIN_HEIGHT // 2 - 60))
                self.level_text(25, f"Your Score: {self.score}", C_YELLOW, (WIN_WIDTH // 2, WIN_HEIGHT // 2 - 20))
                self.level_text(20, "Time's up! Press any key to return to menu", C_WHITE, (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 20))
                pg.display.flip()

                waiting = True
                while waiting:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            pg.quit()
                            sys.exit()
                        elif event.type == pg.KEYDOWN:
                            waiting = False
                            
                initials = self.get_player_initials(self.window, self.score)
                save_score(initials, self.score)
                    
                return "Game Over"
            
            self.level_text(20, f"Score: {self.score}", C_YELLOW, (70, 50))            
            self.level_text(20, f"Level: {self.name} - Timeout: {self.remaining_time / 1000:.1f}s", (C_WHITE), (WIN_WIDTH - 650, WIN_HEIGHT - 20))
            self.level_text(20, f"FPS: {clock.get_fps():.0f}", (C_WHITE), (WIN_WIDTH - 45, WIN_HEIGHT - 35))
            self.level_text(20, f"Entidades: {len(self.entity_list)}", (C_WHITE), (WIN_WIDTH - 70, WIN_HEIGHT - 20))
            
            if player:
                self.level_text(20, f"HP: {player.health}", C_RED, (60, 30))
                
            if player and not player.alive:
                self.level_text(50, "GAME OVER", C_RED, (WIN_WIDTH // 2, WIN_HEIGHT // 2 - 60))
                self.level_text(25, f"Your Score: {self.score}", C_YELLOW, (WIN_WIDTH // 2, WIN_HEIGHT // 2 - 20))
                self.level_text(20, "Press any key to return to menu", C_WHITE, (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 20))
                pg.display.flip()

                # Pause game loop and wait for any key press or quit
                waiting = True
                while waiting:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            pg.quit()
                            sys.exit()
                        elif event.type == pg.KEYDOWN:
                            waiting = False

                initials = self.get_player_initials(self.window, self.score)
                save_score(initials, self.score)
                
                return "Game Over"
            # The below code is for debugging purposes
            # for ent in self.entity_list:
            #     if isinstance(ent, Player):
            #         hurtbox = ent.get_hurtbox()
            #         pg.draw.rect(self.window, C_GREEN, hurtbox, 2)
                    
            #     if isinstance(ent, Player) and ent.is_attacking:
            #         attack_rect = ent.get_attack_rect()
            #         if attack_rect:
            #             pg.draw.rect(self.window, (255, 0, 0), attack_rect, 2)
            if self.paused:
                overlay = pg.Surface((WIN_WIDTH, WIN_HEIGHT))
                overlay.set_alpha(180)  # 0 = fully transparent, 255 = solid
                overlay.fill((0, 0, 0))
                self.window.blit(overlay, (0, 0))

                self.level_text(30, "Paused", C_WHITE, (WIN_WIDTH // 2, WIN_HEIGHT // 2 - 60))
                self.level_text(20, "Press ESC to resume", C_WHITE, (WIN_WIDTH // 2, WIN_HEIGHT // 2))
                self.level_text(20, "Press SPACE to exit game", C_WHITE, (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 40))
                        
            pg.display.flip()
                
            
    def get_player_initials(self, window, score):
        initials = ["A", "A", "A"]
        current_index = 0
        clock = pg.time.Clock()

        font = pg.font.SysFont("Arial", 40, bold=True)
        running = True

        while running:
            clock.tick(30)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        running = False
                    elif event.key == pg.K_LEFT and current_index > 0:
                        current_index -= 1
                    elif event.key == pg.K_RIGHT and current_index < 2:
                        current_index += 1
                    elif event.key == pg.K_UP:
                        initials[current_index] = chr(((ord(initials[current_index]) - 65 + 1) % 26) + 65)
                    elif event.key == pg.K_DOWN:
                        initials[current_index] = chr(((ord(initials[current_index]) - 65 - 1) % 26) + 65)

            self.window.fill((0, 0, 0))

            # Display instructions
            msg = f"Enter your initials - Score: {score}"
            instr_surface = font.render(msg, True, C_WHITE)
            instr_rect = instr_surface.get_rect(center=(WIN_WIDTH // 2, 100))
            window.blit(instr_surface, instr_rect)

            # Display initials
            for i, letter in enumerate(initials):
                color = C_YELLOW if i == current_index else C_WHITE
                letter_surface = font.render(letter, True, color)
                rect = letter_surface.get_rect(center=(WIN_WIDTH // 2 - 50 + i * 50, WIN_HEIGHT // 2))
                window.blit(letter_surface, rect)

            pg.display.flip()

        return "".join(initials)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        font = pg.font.SysFont("Arial", text_size, bold=True)
        
        # Render main text
        main_surface = font.render(text, True, text_color).convert_alpha()
        main_rect = main_surface.get_rect(center=text_position)

        # Render outline
        outline_surface = font.render(text, True, (0, 0, 0)).convert_alpha()
        
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # left, right, up, down
        for dx, dy in offsets:
            outline_rect = outline_surface.get_rect(center=(text_position[0] + dx, text_position[1] + dy))
            self.window.blit(outline_surface, outline_rect)
        
        # Blit final text on top
        self.window.blit(main_surface, main_rect)

#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import *
from code.player import Player
from code.enemy import Enemy

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position: tuple, **kwargs):
        match entity_name:
            # Creates all parallax background layers
            case "Level1Bg":
                list_bg = []
                for i in range(BG_LAYER_COUNT):
                    list_bg.append(Background(f"Level1Bg{i}", position = (0, 0)))
                    list_bg.append(Background(f"Level1Bg{i}", position = (WIN_WIDTH, 0)))
                return list_bg
            
            # Creates player
            case "Player1":
                list_player = [Player(PLAYER_SPRITE_PREFIX, position=(10, WIN_HEIGHT / 2))]
                return list_player
            
            # Creates enemy
            case "Enemy":
                enemy = Enemy("assets/enemy_spritesheet.png", frame_size=(16, 16), position=position)
                return [enemy]

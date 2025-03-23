import pygame as pg

# A
ATTACK_COOLDOWN = 600

#B
BG_LAYER_COUNT = 8

# C
C_RED = 255, 20, 0
C_WHITE = 255, 255, 255
C_YELLOW = 255, 255, 0
C_GREEN = 0, 255, 0

# D
DEFAULT_HEALTH = 3

# E
ENTITY_SPEED = {
    "Level1Bg0": 1,
    "Level1Bg1": 2,
    "Level1Bg2": 3,
    "Level1Bg3": 4,
    "Level1Bg4": 5,
    "Level1Bg5": 6,
    "Level1Bg6": 6,
    "Level1Bg7": 6,
    "Player1": 2,
    "Player2": 3,
    "Enemy": 4,
}

ENEMY_SPAWN_DELAY = 1000

#I
INVULNERABILITY_DURATION = 1200

# M
MENU_OPTION = ("Start Game", 
               "High Scores", 
               "Exit")

#P
PLAYER_SPRITE_PREFIX = "HeroKnight_Run"

# W
WIN_WIDTH = 800
WIN_HEIGHT = 600
import pygame as pg
import sys
from code.const import *
from code.score_db import get_top_scores

def high_scores_screen(window):
    pg.font.init()
    font_title = pg.font.SysFont("Arial", 40, bold=True)
    font_score = pg.font.SysFont("Arial", 28, bold=True)

    scores = get_top_scores(10)
    clock = pg.time.Clock()
    running = True

    while running:
        clock.tick(30)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key in [pg.K_ESCAPE, pg.K_RETURN]:
                    running = False

        window.fill((0, 0, 0))

        # Título
        title_surface = font_title.render("High Scores", True, C_YELLOW)
        title_rect = title_surface.get_rect(center=(WIN_WIDTH // 2, 80))
        window.blit(title_surface, title_rect)

        # Lista de scores
        for i, (name, score, timestamp) in enumerate(scores):
            text = f"{i+1}. {name} - {score} pts"
            score_surface = font_score.render(text, True, C_WHITE)
            rect = score_surface.get_rect(midleft=(150, 150 + i * 40))
            window.blit(score_surface, rect)

        # Rodapé
        footer = font_score.render("Press ESC or ENTER to return", True, C_WHITE)
        footer_rect = footer.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT - 50))
        window.blit(footer, footer_rect)

        pg.display.flip()
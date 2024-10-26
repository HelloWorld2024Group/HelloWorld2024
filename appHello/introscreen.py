import pygame
import sys
from app_settings import *


start_button = pygame.Rect((SCREEN_SIZE - 200) // 2 + 35, SCREEN_SIZE - 260, 140, 30)


def show_intro_screen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button.collidepoint(event.pos):
                    intro = False  # Exit the introduction screen

        screen.fill(light_blue)
        pygame.display.set_caption("Hello World '24")

        # write start button
        pygame.draw.rect(screen, gold, start_button)

        # Hello world text
        font = pygame.font.SysFont(None, 48)
        text = font.render("Hello World '24", True, white)

        start_text = font.render("Start", True, (0,0,0)) # color letters
        start_text_rect = start_text.get_rect(center=start_button.center)
        screen.blit(start_text,start_text_rect)

        text_rect = text.get_rect(center=(400, 400))
        screen.blit(text, text_rect)

        pygame.display.flip()

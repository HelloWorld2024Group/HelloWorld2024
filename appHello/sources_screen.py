import pygame
from app_settings import *
import sys
import math

import pygame
from app_settings import *
import sys


next_button = pygame.Rect(600, 700, 140, 30)
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

news_sources = ["Source 1", "Source 2", "Source 3", "Source 4", "Source 5",
                    "Source 6", "Source 7", "Source 8", "Source 9", "Source 10",
                    "Source 11", "Source 12", "Source 13", "Source 14"]


SQUARE_SIDE = 20
MARGIN = 50
start_x = 100
start_y = 180



def select_sources_screen():
    pygame.init()
    scroll_offset = 0

    sources = True
    while sources:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN: #and event.button == 1:
                if next_button.collidepoint(event.pos):
                    sources = False  # Exit the introduction screen
            elif event.type == pygame.MOUSEWHEEL:
                scroll_offset += event.y * 20
 
        #scrolling logic

        content_height = len(news_sources) * (SQUARE_SIDE + MARGIN)
        max_offset = content_height - (SCREEN_SIZE - start_y)
        scroll_offset = max(-max_offset, min(0, scroll_offset))

        screen.fill(light_blue)
        pygame.display.set_caption(app_title)

        #Screen Title
        font = pygame.font.SysFont(None, 50)
        text = font.render("Choose your sources:", True, gold)
        text_xy = (100, 100)
        screen.blit(text,text_xy)

        #boxes
        for index, source in enumerate(news_sources):
            square_y = start_y + index * (SQUARE_SIDE + MARGIN) + scroll_offset
            square_rect = pygame.Rect(start_x, square_y, SQUARE_SIDE, SQUARE_SIDE)

            #if -SQUARE_SIDE < square_y < SCREEN_SIZE:
            if 120 < square_y < SCREEN_SIZE:

                    # Draw each square
                    pygame.draw.rect(screen, gold, square_rect)

                    # Render text for each square
                    source_text = font.render(source, True, white)
                    source_text_rect = source_text.get_rect()
                    source_text_rect.topleft = (150, square_y)
                    screen.blit(source_text, source_text_rect)

        #pygame.draw.rect(screen, "goldenrod", square_rect)


        # next button
        pygame.draw.rect(screen, gold, next_button)

        next_font = pygame.font.SysFont(None, 30)
        next_text = next_font.render("Next", True, white) # color letters
        next_text_rect = next_text.get_rect(center=next_button.center)
        screen.blit(next_text,next_text_rect)




        pygame.display.flip()




        # only able to click on the button if selected 3 or 5 more news sources

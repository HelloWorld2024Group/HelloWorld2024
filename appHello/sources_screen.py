import pygame
from app_settings import *
from assign_images import *
import sys
import math


next_button = pygame.Rect(600, 700, 140, 30)
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))


SQUARE_SIDE = 20
MARGIN = 50
# start_x = 100
start_x_column_1 = 100
start_x_column_2 = 400
start_y = 180

# split data in two columns
mid_index = len(sources_list) // 2
column_1 = sources_list[mid_index:]
column_2 = sources_list[:mid_index]

# need to split images list


def select_sources_screen():
    pygame.init()
    scroll_offset = 0

    process_sources(file_path)

    sources = True
    while sources:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if next_button.collidepoint(event.pos):
                    sources = False
            elif event.type == pygame.MOUSEWHEEL:
                scroll_offset += event.y * 20

        # scrolling logic
        #content_height = len(sources_list) * (SQUARE_SIDE + MARGIN)
        max_height = max(len(column_1), len(column_2)) * (SQUARE_SIDE + MARGIN)
        max_offset = max_height - (SCREEN_SIZE - start_y)
        scroll_offset = max(-max_offset, min(0, scroll_offset))

        screen.fill(light_blue)
        pygame.display.set_caption(app_title)

        # Screen Title
        font = pygame.font.SysFont(None, 50)
        text = font.render("Choose your sources:", True, gold)
        text_xy = (100, 80)
        screen.blit(text, text_xy)

        # boxes
        """for index, source in enumerate(sources_list):
            square_y = start_y + index * (SQUARE_SIDE + MARGIN) + scroll_offset
            square_rect = pygame.Rect(start_x, square_y, SQUARE_SIDE, SQUARE_SIDE)

            if 140 < square_y < SCREEN_SIZE:

                # Draw each square
                pygame.draw.rect(screen, gold, square_rect)

                # Render text for each square
                source_font = pygame.font.SysFont(None, 30)
                source_text = source_font.render(source, True, white)
                source_text_rect = source_text.get_rect()
                source_text_rect.topleft = (150, square_y)
                screen.blit(source_text, source_text_rect)"""

        for index, source in enumerate (column_1):
            square_y = start_y + index * (SQUARE_SIDE + MARGIN) + scroll_offset
            square_rect = pygame.Rect(start_x_column_1 - 20, square_y, SQUARE_SIDE, SQUARE_SIDE)

            if 140 < square_y < SCREEN_SIZE:
                pygame.draw.rect(screen, gold, square_rect)

                source_font = pygame.font.SysFont(None, 30)
                source_text = source_font.render(source, True, white)
                source_text_rect = source_text.get_rect()
                source_text_rect.topleft = (start_x_column_1 + 10, square_y)
                screen.blit(source_text, source_text_rect)


        for index, source in enumerate (column_2):
            square_y = start_y + index * (SQUARE_SIDE + MARGIN) + scroll_offset
            square_rect = pygame.Rect(start_x_column_2 - 20, square_y, SQUARE_SIDE, SQUARE_SIDE)

            if 140 < square_y < SCREEN_SIZE:
                pygame.draw.rect(screen, gold, square_rect)

                source_font = pygame.font.SysFont(None, 30)
                source_text = source_font.render(source, True, white)
                source_text_rect = source_text.get_rect()
                source_text_rect.topleft = (start_x_column_2 + 10, square_y)
                screen.blit(source_text, source_text_rect)


        # next button
        pygame.draw.rect(screen, gold, next_button)

        next_font = pygame.font.SysFont(None, 30)
        next_text = next_font.render("Next", True, white)  # color letters
        next_text_rect = next_text.get_rect(center=next_button.center)
        screen.blit(next_text, next_text_rect)

        pygame.display.flip()

        # only able to click on the button if selected 3 or 5 more news sources

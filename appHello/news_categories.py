import pygame
from app_settings import *
from assign_images import *

import sys

categories_list = ["Politics", "Economy and Business", "Technology and Innovation",
                    "Health and Wellness"," Environment and Climate", "Sports", "Entertainment and Culture",
                    "Science and Space", "Crime and Legal Affairs", "Miscellaneous"]

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
next_button = pygame.Rect(600, 50, 140, 30)

SQUARE_SIDE = 20
MARGIN = 50
start_y = 180
start_x_column_1 = 100
start_x_column_2 = 450
scroll_offset = 0

# Split data into two columns
mid_index = len(categories_list) // 2
column_1 = categories_list[:mid_index]
column_2 = categories_list[mid_index:]

def categories():
    global scroll_offset

    categories = True
    while categories:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if next_button.collidepoint(event.pos):
                    categories = False
            elif event.type == pygame.MOUSEWHEEL:
                scroll_offset += event.y * 20

        # Scroll boundaries logic
        max_height = max(len(column_1), len(column_2)) * (SQUARE_SIDE + MARGIN)
        max_offset = max_height - (SCREEN_SIZE - start_y)
        scroll_offset = max(-max_offset, min(0, scroll_offset))

        screen.fill(light_blue)
        pygame.display.set_caption(app_title)

        # Screen texts
        font = pygame.font.SysFont(None, 50)
        text = font.render("Select a category:", True, gold)
        screen.blit(text, (100, 80))

        display_categories(column_1, start_x_column_1 + 30, scroll_offset)
        display_categories(column_2, start_x_column_2 + 30, scroll_offset)


        # Draw 'Next' button
        pygame.draw.rect(screen, gold, next_button)
        next_font = pygame.font.SysFont(None, 30)
        next_text = next_font.render("Next", True, white)
        next_text_rect = next_text.get_rect(center=next_button.center)
        screen.blit(next_text, next_text_rect)

        pygame.display.flip()

def display_categories(column, start_x, scroll_offset):
    for index, source in enumerate(column):
        square_y = start_y + index * (SQUARE_SIDE + MARGIN) + scroll_offset
        if 140 < square_y < SCREEN_SIZE:
            source_font = pygame.font.SysFont(None, 30)
            source_text = source_font.render(source, True, white)
            source_text_rect = source_text.get_rect()
            source_text_rect.topleft = (start_x + 10, square_y)
            screen.blit(source_text, source_text_rect)
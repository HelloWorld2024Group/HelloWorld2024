import pygame
from app_settings import *
from assign_images import *

import sys


next_button = pygame.Rect(580, 80, 140, 30)
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

# Load and scale images once at the beginning
icons = [
    pygame.transform.scale(pygame.image.load(filename), (60, 60))
    for filename in icon_names_list
]

SQUARE_SIDE = 20
MARGIN = 50
start_x_column_1 = 100
start_x_column_2 = 450
start_y = 180

scroll_offset = 0

# Split data and images into two columns
mid_index = len(sources_list) // 2
column_1 = sources_list[mid_index:]
column_2 = sources_list[:mid_index]

column_icons_1 = icons[mid_index:]
column_icons_2 = icons[:mid_index]


def select_sources_screen():
    global arrow_visible, arrow_position, scroll_offset

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

        # Scroll boundaries logic
        max_height = max(len(column_1), len(column_2)) * (SQUARE_SIDE + MARGIN)
        max_offset = max_height - (SCREEN_SIZE - start_y)
        scroll_offset = max(-max_offset, min(0, scroll_offset))

        screen.fill(light_blue)
        pygame.display.set_caption(app_title)

        # Screen Title
        font = pygame.font.SysFont(None, 50)
        text = font.render("Choose your sources:", True, gold)
        screen.blit(text, (80, 80))

        # Display source text in columns
        display_sources(column_1, start_x_column_1 + 30, scroll_offset)
        display_sources(column_2, start_x_column_2 + 30, scroll_offset)

        # Display images in two columns
        display_images(scroll_offset)

        # Draw 'Next' button
        pygame.draw.rect(screen, gold, next_button)
        next_font = pygame.font.SysFont(None, 30)
        next_text = next_font.render("Next", True, white)
        next_text_rect = next_text.get_rect(center=next_button.center)
        screen.blit(next_text, next_text_rect)

        pygame.display.flip()


def display_sources(column, start_x, scroll_offset):
    for index, source in enumerate(column):
        square_y = 20 + start_y + index * (SQUARE_SIDE + MARGIN) + scroll_offset
        if 140 < square_y < SCREEN_SIZE:
            source_font = pygame.font.SysFont(None, 30)
            source_text = source_font.render(source, True, white)
            source_text_rect = source_text.get_rect()
            source_text_rect.topleft = (start_x + 10, square_y)
            screen.blit(source_text, source_text_rect)


def display_images(scroll_offset):
    # Display images in the first column
    for index, image in enumerate(column_icons_1):
        image_y = start_y + index * (SQUARE_SIDE + MARGIN) + scroll_offset
        if 140 < image_y < SCREEN_SIZE:
            image_rect = image.get_rect(topleft=(start_x_column_1 - 30, image_y))
            screen.blit(image, (start_x_column_1 - 30, image_y))

    # Display images in the second column
    for index, image in enumerate(column_icons_2):
        image_y = start_y + index * (SQUARE_SIDE + MARGIN) + scroll_offset
        if 140 < image_y < SCREEN_SIZE:
            image_rect = image.get_rect(topleft=(start_x_column_2 - 30, image_y))
            screen.blit(image, (start_x_column_2 - 30, image_y))

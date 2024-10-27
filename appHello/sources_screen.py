import pygame
from app_settings import *
from assign_images import *
from news_categories import *

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
count = 0

scroll_offset = 0

# Split data and images into two columns
mid_index = len(sources_list) // 2
column_1 = sources_list[mid_index:]
column_2 = sources_list[:mid_index]

column_icons_1 = icons[mid_index:]
column_icons_2 = icons[:mid_index]


def select_sources_screen():
    global count, scroll_offset

    scroll_offset = 0

    process_sources(file_path)

    sources = True
    while sources:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_source_click(event, column_1, start_x_column_1, spacing - 25)
                handle_source_click(event, column_2, start_x_column_2 + 10, spacing - 2)
                if count >= 3:
                    if next_button.collidepoint(event.pos):
                        sources = False
            elif event.type == pygame.MOUSEWHEEL:
                scroll_offset += event.y * 20

        # Scroll boundaries logic
        max_height = max(len(column_1), len(column_2)) * (SQUARE_SIDE + MARGIN)
        max_offset = max_height - (SCREEN_SIZE - start_y)
        scroll_offset = max(-max_offset, min(0, scroll_offset))

        screen.fill("midnightblue")
        pygame.display.set_caption(app_title)

        # Screen Title
        font = pygame.font.SysFont(None, 50)
        text = font.render("Choose your sources:", True, "silver")
        screen.blit(text, (80, 80))

        # Display source text in columns
        display_sources(column_1, start_x_column_1 + 30, scroll_offset)
        display_sources(column_2, start_x_column_2 + 30, scroll_offset)

        # Display images in two columns
        display_images(scroll_offset)

        # Draw 'Next' button
        pygame.draw.rect(screen, "silver", next_button)
        next_font = pygame.font.SysFont(None, 30)
        next_text = next_font.render("Next", True, white)
        next_text_rect = next_text.get_rect(center=next_button.center)
        screen.blit(next_text, next_text_rect)

        spacing = (800 - start_y) // (len(column_1) - 1) if len(column_1) > 1 else 0





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


def handle_source_click(event, column, start_x, spacing):
    global count
    #woking here to see if can fix seletcing 3 or more news outlets
    for index, source in enumerate(column):
        square_y = start_y + index * spacing
        button_rect = pygame.Rect(start_x - 20, square_y, 250, 40)  # Same size as in display_categories
        if button_rect.collidepoint(event.pos):
            print(f"Clicked on: {source}")
            count += 1
            print(count)

            #if 3 different inputs, allow to move on


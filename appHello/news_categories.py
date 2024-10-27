import pygame
import sys
from app_settings import *
from assign_images import *
from example_dictionaries import *
from article import *
from readfile import *  # Ensure this module contains `read_and_display_json`

categories_list = ["Politics", "Economy and Business", "Technology and Innovation",
                   "Health and Wellness", "Environment and Climate", "Sports",
                   "Entertainment and Culture", "Science and Space", 
                   "Crime and Legal Affairs", "Miscellaneous"]

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
next_button = pygame.Rect(580, 80, 140, 30)

SQUARE_SIDE = 20
MARGIN = 50
start_y = 180
start_x_column_1 = 100
start_x_column_2 = 450

# Split data into two columns
mid_index = len(categories_list) // 2
column_1 = categories_list[:mid_index]
column_2 = categories_list[mid_index:]

def categories():
    screen.fill("midnightblue")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                running = handle_category_click(event, column_1, start_x_column_1, spacing, dictionaries_list, running)
                running = handle_category_click(event, column_2, start_x_column_2 + 10, spacing, dictionaries_list, running)

                if next_button.collidepoint(event.pos):
                    running = False

        # Scroll boundaries logic
        pygame.display.set_caption(app_title)

        # Screen texts
        font = pygame.font.SysFont(None, 50)
        text = font.render("Select a category:", True, "silver")
        screen.blit(text, (80, 80))

        # Calculate spacing based on the number of items in column_1
        spacing = (800 - start_y) // (len(column_1) - 1) if len(column_1) > 1 else 0

        display_categories(column_1, start_x_column_1, spacing)
        display_categories(column_2, start_x_column_2 + 10, spacing)

        # Draw 'Next' button
        pygame.draw.rect(screen, "silver", next_button)
        next_font = pygame.font.SysFont(None, 30)
        next_text = next_font.render("Next", True, white)
        next_text_rect = next_text.get_rect(center=next_button.center)
        screen.blit(next_text, next_text_rect)

        pygame.display.flip()

def display_categories(column, start_x, spacing):
    for index, source in enumerate(column):
        square_y = start_y + index * spacing
        if 140 < square_y < SCREEN_SIZE:
            button_rect = pygame.Rect(start_x - 20, square_y, 280, 80)  # Adjust size as needed
            pygame.draw.rect(screen, "silver", button_rect)

            source_font = pygame.font.SysFont(None, 30)
            source_text = source_font.render(source, True, white)
            source_text_rect = source_text.get_rect(center=button_rect.center)
            screen.blit(source_text, source_text_rect)

def handle_category_click(event, column, start_x, spacing, dictionaries_list, running):
    for index, source in enumerate(column):
        square_y = start_y + index * spacing
        button_rect = pygame.Rect(start_x - 20, square_y, 250, 40)
        if button_rect.collidepoint(event.pos):
            # If a button is clicked, load the corresponding JSON data
            read_and_display_json('data.json')  # Make sure 'data.json' exists
            return False
    return running

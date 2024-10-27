import pygame
import json
from app_settings import *

def read_and_display_json(file_path):
    # Initialize Pygame and set up the screen
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("News Summaries")
    screen.fill((255, 255, 255))  # Fill screen with white color

    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            news_data = json.load(json_file)
    except FileNotFoundError:
        print("File not found.")
        return

    headline_font = pygame.font.SysFont(None, 40)
    bullet_font = pygame.font.SysFont(None, 25)

    start_x = 50
    initial_start_y = 50
    line_spacing = 10

    scroll_offset = 0

    def render_text(text, font, color, start_x, start_y, max_width):
        words = text.split(' ')
        current_line = []
        current_line_surface = []
        current_width = 0
        line_height = font.get_height()

        for word in words:
            word_surface = font.render(word + ' ', True, color)
            word_width = word_surface.get_width()

            if current_width + word_width >= max_width:
                # Blit the current line onto the screen
                line_surface = font.render(' '.join(current_line), True, color)
                screen.blit(line_surface, (start_x, start_y))

                # Move to the next line
                current_line = [word]
                current_width = word_width
                start_y += line_height + line_spacing
            else:
                current_line.append(word)
                current_width += word_width

        # Blit the remaining text in the current line
        if current_line:
            line_surface = font.render(' '.join(current_line), True, color)
            screen.blit(line_surface, (start_x, start_y))

        return start_y + line_height  # Return the updated y-coordinate

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEWHEEL:
                scroll_offset += event.y * 20  # Adjust scroll speed as needed

        # Fill screen with white background and adjust scroll offset
        screen.fill((255, 255, 255))
        start_y = initial_start_y + scroll_offset

        # Render the headlines and bullet points
        for headline, content in news_data.items():
            # Render headline
            start_y = render_text(headline, headline_font, (0, 0, 0), start_x, start_y, SCREEN_SIZE - 2 * start_x)
            start_y += line_spacing  # Space after the headline

            # Render bullet points
            bullet_points = content.split('\n')
            for bullet in bullet_points:
                start_y = render_text(bullet, bullet_font, (50, 50, 50), start_x + 20, start_y, SCREEN_SIZE - 2 * start_x)
                start_y += line_spacing

            # Extra space between sections
            start_y += 20

        # Update the display
        pygame.display.flip()


# Example usage

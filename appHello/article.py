import pygame
import sys
from introscreen import *
from sources_screen import *
from news_categories import *
from example_dictionaries import *

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

def write_article(news_item):

    start_x = 50
    start_y = 50
    heading_color = ((255, 255, 255),)
    sentence_color = (200, 200, 200)
    screen.fill(white)

    heading_font = pygame.font.SysFont(None, 35)
    sentence_font = pygame.font.SysFont(None, 25)

    # Render heading
    heading_text = heading_font.render(news_item["Heading"], True, (0,0,0))
    screen.blit(heading_text, (start_x, start_y))

    # Render sentence, leaving some space after the heading
    sentence_y = start_y + heading_text.get_height() + 5
    sentence_text = sentence_font.render(news_item["Sentence"], True,(0,0,0))
    screen.blit(sentence_text, (start_x, sentence_y))

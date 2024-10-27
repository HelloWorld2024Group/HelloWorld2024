import pygame
import sys
from introscreen import *
from sources_screen import *
from news_categories import *


def main():
    pygame.init()

    show_intro_screen()

    select_sources_screen()

    categories()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

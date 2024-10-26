import pygame
import sys
from introscreen import *
from sources_screen import *


def main():
    pygame.init()

    show_intro_screen()

    select_sources_screen()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

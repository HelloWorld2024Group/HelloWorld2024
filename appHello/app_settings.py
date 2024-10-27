import pygame
import math

file_path = "message.txt"
arrow = "images/arrow.png"

app_title = "Hello World '24"

sources_list = []

SCREEN_SIZE = 800

black = (0,0,0)
white = (255, 255, 255)
gold = (249, 216, 73)
red = (255,0,255)

light_blue = (151, 204, 232)

screen = pygame.display.set_mode((800, 800))

icon_names_list = [
    "images/nytimes.png","images/cnn.png","images/bbc.png","images/fox.png","images/washingtonpost.png",
    "images/abcnews.png","images/nbcnews.png", "images/cbsnews.png","images/buzzfeed.png",
    "images/vice.png","images/slate.png","images/vox.png","images/salon.png", "images/theintercept.png",
    "images/theatlantic.png","images/thenewyorker.png","images/time.png","images/businessinsider.png",
    "images/fortune.png","images/cnbc.png","images/latimes.png","images/democracynow.png","images/commondreams.png",
    "images/aljazeera.png","images/propublica.png","images/novaramedia.png","images/guardian.png",
]

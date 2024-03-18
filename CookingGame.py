import pygame
import time
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SNAKE GAME')
BACKGROUND = pygame.image.load("images/cooking_game.png")

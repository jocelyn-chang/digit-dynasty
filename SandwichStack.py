# Import appropriate libraries
import pygame, sys, csv
from Button import Button
from GameMap import load_map

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SANDWICH STACK')
BACKGROUND = pygame.image.load("images/sandwich_stack_bg.png")

def start_game():
    while True:
        SCREEN.blit(BACKGROUND, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
start_game()
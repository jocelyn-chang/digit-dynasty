# Import appropriate libraries
import pygame, sys
from button import Button

# Initialize the Pygame library
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = pygame.image.load("images/Background.png")

# Main Menu screen
def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.blit(background, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        

# Go to screen with main map
def start_game():
    while True:
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("bl")

# Intructions screen
def instructions():

# Controls screen
def controls():



run = True
while run:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

pygame.quit()


    
# Import appropriate libraries
import pygame
import sys

# Initialize the Pygame library
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


run = True
while run:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

pygame.quit()
Class Button:
    def __init__(self, text, width, height, pos, elevation):
        # Define core attributes
        self.press = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        # Defining the top rectangle
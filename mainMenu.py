# Import appropriate libraries
import pygame, sys
from button import Button

# Initialize the Pygame library
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# for bg
# background = pygame.image.load("assets/Background.png")

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
        self.top_rec = pygame.Rect(pos, (width, height))
        self.top_colour = '#475F77'
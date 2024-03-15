import pygame
import time
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = pygame.image.load("images/snakegamebg.png")
pygame.display.set_caption('SNAKE GAME')

# Main Colours
gold1 = (230, 224, 174)
gold2 = (223, 188, 94)
red1 = (238, 97, 70)
red2 = (215, 60, 55)
red3 = (181, 31, 9)

# Secondary Colours
green1 = (116, 217, 219)
green2 = (153, 216, 196)
green3 = (113, 182, 135)
green4 = (88, 133, 120)
green5 = (117, 132, 133)

snake_block = 10
snake_speed = 15


run = True
while run:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  
      # Draw the background image onto the screen
  screen.blit(BACKGROUND, (0, 0))

  # Update the display
  pygame.display.flip()

pygame.quit()
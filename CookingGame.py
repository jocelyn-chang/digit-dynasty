import pygame
import time
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('COOKING GAME')

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

BACKGROUND = pygame.image.load("images/cooking_game.png")


while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Drawing code should go here
    
    # First, clear the screen to white or any other color. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill((255, 255, 255))

    # Now let's blit the image onto the screen at position (0, 0)
    screen.blit(BACKGROUND, (0, 0))

    # --- Update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

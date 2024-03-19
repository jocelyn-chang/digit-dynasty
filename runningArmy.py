import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DIGIT DYNASTY')

# Load the tall image
image = pygame.image.load("images/running_army_bg.png")
panda = pygame.transform.scale(pygame.image.load("images/panda1.png"), (50, 50))
gate = pygame.transform.scale(pygame.image.load("images/gates.png"), (400, 125))
qbox = pygame.transform.scale(pygame.image.load("images/questionscreen.png"), (400, 125))
arrow = pygame.transform.scale(pygame.image.load("images/parrow.png"), (50, 50))

image_height = image.get_height()
image_width = image.get_width()

# movement for panda/arrow
arrow_rect = arrow.get_rect()
panda_rect = panda.get_rect()
x = (SCREEN_WIDTH) // 2
speed = 5

# Calculate the new height of the image to maintain the aspect ratio
scaled_height = int(image_height * (SCREEN_WIDTH / image_width))

# Scale the image to fill the width of the screen while maintaining the aspect ratio
scaled_image = pygame.transform.scale(image, (SCREEN_WIDTH, scaled_height))

# Scrolling variables
scroll_y = 0
scroll_speed = 2

# Main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed

    # Scroll the image
    scroll_y += scroll_speed
    if scroll_y >= scaled_height:
        scroll_y = 0

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the scaled image twice to create the looping effect and gates
    screen.blit(scaled_image, (0, scroll_y - scaled_height))
    screen.blit(scaled_image, (0, scroll_y))
    screen.blit(gate, (200, scroll_y-125))

    # Draw the panda and arrow
    screen.blit(panda, panda_rect)
    screen.blit(arrow, (x, scroll_y-125))

    panda_rect.topleft = (x, 400)
    arrow_rect.topleft = (x, scroll_y)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DUMPLING_SIZE = 100  

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('COOKING GAME')

done = False
clock = pygame.time.Clock()

BACKGROUND = pygame.image.load("images/cooking_game.png")
DUMPLING = pygame.image.load("images/dumpling.png")  # Replace with your image file path
DUMPLING = pygame.transform.scale(DUMPLING, (DUMPLING_SIZE, DUMPLING_SIZE))

# Define a smaller central area rectangle (x, y, width, height)
# For example, we'll make it 1/3 of the screen size for width and height and place it in the center
CENTRAL_AREA_WIDTH = SCREEN_WIDTH // 3
CENTRAL_AREA_HEIGHT = SCREEN_HEIGHT // 3
CENTRAL_AREA = pygame.Rect(
    (SCREEN_WIDTH - CENTRAL_AREA_WIDTH) // 2, 
    (SCREEN_HEIGHT - CENTRAL_AREA_HEIGHT) // 2, 
    CENTRAL_AREA_WIDTH, 
    CENTRAL_AREA_HEIGHT
)

# List to keep track of dumpling positions within the central area
dumpling_positions = []

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Add a new dumpling within the central area
                new_x = random.randint(CENTRAL_AREA.left, CENTRAL_AREA.right - DUMPLING_SIZE)
                new_y = random.randint(CENTRAL_AREA.top, CENTRAL_AREA.bottom - DUMPLING_SIZE)
                dumpling_positions.append((new_x, new_y))
            elif event.key == pygame.K_LEFT and dumpling_positions:
                # Remove the last dumpling added
                dumpling_positions.pop()

    screen.fill((255, 255, 255))  # Clear the screen
    screen.blit(BACKGROUND, (0, 0))  # Draw the background

    # Draw all the dumplings in their positions
    for pos in dumpling_positions:
        screen.blit(DUMPLING, pos)

    pygame.display.flip()  # Update the screen with what we've drawn
    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()

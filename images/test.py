import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Scrolling List")

# Create a list of items
items = [f"Item {i}" for i in range(1, 21)]
font = pygame.font.Font(None, 30)

# Scroll variables
scroll = 0
item_height = 30

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                scroll = max(scroll - item_height, 0)
            elif event.key == pygame.K_DOWN:
                scroll = min(scroll + item_height, len(items) * item_height - screen_height)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the visible portion of the list
    for i, item in enumerate(items):
        y = i * item_height - scroll
        if 0 <= y < screen_height:
            text = font.render(item, True, (0, 0, 0))
            screen.blit(text, (10, y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

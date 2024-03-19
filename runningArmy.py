import pygame, sys
from Button import Button

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DIGIT DYNASTY')

# Load the tall image
INSTRUCTIONS = pygame.image.load("images/Multiplication_instruction.png")
BACK = pygame.image.load("images/back_button.png")
RESIZED_BACK = pygame.image.load("images/resized_back.png")
start_screen = pygame.image.load("images/Running Army Start Screen.png")
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
scroll = 0
scroll_speed = 2

# Intructions screen
def instructions():
    while True:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(INSTRUCTIONS, (0, 0))
        
        INSTRUCTIONS_BACK = Button(image = "images/back_button.png", pos = (70, 55), text_input = "", font = get_font(15), base_colour = "White", hovering_colour = "#b51f09")
        if (40<MOUSE_X<75 and 40<MOUSE_Y<70):
            screen.blit(RESIZED_BACK, (-90,-96))
        
        INSTRUCTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkInput(GAME_MOUSE_POS):
                    running_army()

        pygame.display.update()


def start_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed

    # Scroll the image
    scroll += scroll_speed
    if scroll >= scaled_height:
        scroll = 0

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the scaled image twice to create the looping effect and gates
    screen.blit(scaled_image, (0, scroll - scaled_height))
    screen.blit(scaled_image, (0, scroll))
    screen.blit(gate, (200, scroll-125))

    # Draw the panda and arrow
    screen.blit(panda, panda_rect)
    screen.blit(arrow, (x, scroll-450))

    panda_rect.topleft = (x, 400)
    arrow_rect.topleft = (x, scroll)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

def running_army():
    # Main game loop
    run = True
    while run:
        MOUSE_POS = pygame.mouse.get_pos()

        START_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 75), text_input = "NEW GAME", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")
        INSTRUCTION_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 417), text_input = "INSTRUCTIONS", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if START_BUTTON.checkInput(MOUSE_POS):
                        start_game()
                    if INSTRUCTION_BUTTON.checkInput(MOUSE_POS):
                        instructions()
        # display start screen
        screen.blit(start_screen, (0,0))

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

running_army()
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SNAKE GAME')

# Load background image
BACKGROUND = pygame.image.load("images/snakegamebg.png")

# # Load fruit image
# FRUIT_A = pygame.image.load("images/orangea.png").convert_alpha()
fruit_size = (50, 50)

# # Scale the fruit image to the new size
# FRUIT_A = pygame.transform.scale(FRUIT_A, fruit_size)

# Clock for controlling game speed
clock = pygame.time.Clock()

# Colors
gold1 = (230, 224, 174)
gold2 = (223, 188, 94)
red1 = (238, 97, 70)
red2 = (215, 60, 55)
red3 = (181, 31, 9)
green1 = (116, 217, 219)
green2 = (153, 216, 196)
green3 = (113, 182, 135)
green4 = (88, 133, 120)
green5 = (117, 132, 133)
black = (0, 0, 0)
white = (255, 255, 255)

# Snake block size and speed
snake_block = 20
snake_speed = 10

# Font for displaying score
font_style = pygame.font.Font("fonts/Shojumaru-Regular.ttf", 25)

# Function to display current score
def current_score(score):
    # Shadow text
    shadow = font_style.render("Score: " + str(score), True, green4)
    screen.blit(shadow, [652, 12])
    
    # Main text
    main = font_style.render("Score: " + str(score), True, white)
    screen.blit(main, [650, 10])

# Function to draw the snake
def snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(screen, green2, [i[0], i[1], snake_block, snake_block])

# Main game function
def game():
    run = True 
    end = False

    # Snake starting coordinates
    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    # Initialize change in coordinates
    x1_change = 0
    y1_change = 0

    # List of snake body parts coordinates
    snake_list = []
    snake_len = 1

    # Load fruit image
    FRUIT_A = pygame.image.load("images/orangea.png").convert_alpha()
    # Scale the fruit image to the new size
    FRUIT_A = pygame.transform.scale(FRUIT_A, fruit_size)

    # Randomize position of fruit
    foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0

    while run:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Control snake movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x1_change = -snake_block
            y1_change = 0
        elif keys[pygame.K_RIGHT]:
            x1_change = snake_block
            y1_change = 0
        elif keys[pygame.K_UP]:
            y1_change = -snake_block
            x1_change = 0
        elif keys[pygame.K_DOWN]:
            y1_change = snake_block
            x1_change = 0

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        print("x1: " + str(x1))
        print("y1: " + str(y1))

        snake_list.append([x1, y1])

        # If snake length exceeds current length, remove the tail
        if len(snake_list) > snake_len:
            del snake_list[0]

        # Draw elements on screen
        screen.blit(BACKGROUND, (0, 0))
        snake(snake_block, snake_list)
        screen.blit(FRUIT_A, (foodx, foody))
        current_score(snake_len - 1)
        print("poo")
        print("foodx: " + str(foodx))
        print("foody: " + str(foody))

        # Check if snake has eaten the fruit
        # if x1 == foodx and y1 == foody:
        if x1 >= (foodx-20) and x1 <= (foodx+30) and y1 >= (foody-20) and y1 <= (foody+40):
            # if y1 >= (foody-20) and y1 <= (foody+20):
            #     print("foody: " + str(foody))
            #     print("foodx: " + str(foodx))
            #     run = False
            
                
            foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0
            snake_len += 1
            # # Load fruit image
            # FRUIT_A = pygame.image.load("images/orangea.png").convert_alpha()
            # # fruit_size = (100, 100)

            # # Scale the fruit image to the new size
            # FRUIT_A = pygame.transform.scale(FRUIT_A, fruit_size)
            # screen.blit(FRUIT_A, (foodx, foody))
        pygame.display.flip()

        clock.tick(snake_speed)

    pygame.quit()

# Run the game
game()
import pygame
import random
from question import Question
from Player import Player

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Dumpling and Photo Settings
DUMPLING_SIZE = 100
PHOTO_SIZE = (200, 250)
PHOTO_INTERVAL_MS = 5000
PHOTO_SPACING = 150

# Colors
WHITE = (255, 255, 255)

# Load images
BACKGROUND = pygame.image.load("images/cooking_game.png")
DUMPLING = pygame.image.load("images/dumpling.png")
DUMPLING = pygame.transform.scale(DUMPLING, (DUMPLING_SIZE, DUMPLING_SIZE))
NEW_PHOTO = pygame.image.load("images/order.png")
NEW_PHOTO = pygame.transform.scale(NEW_PHOTO, PHOTO_SIZE)

# Initialize the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('COOKING GAME')

# Clock for controlling game speed
clock = pygame.time.Clock()

font = pygame.font.Font("fonts/Shojumaru-Regular.ttf", 36)

number_of_dumplings = 0

def handle_events(dumpling_positions, central_area):
    global number_of_dumplings
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                add_dumpling(dumpling_positions, central_area)
                number_of_dumplings += 1
                print(number_of_dumplings)
            elif event.key == pygame.K_LEFT and dumpling_positions:
                dumpling_positions.pop()
                number_of_dumplings -= 1
                print(number_of_dumplings)
    return True

def add_dumpling(dumpling_positions, central_area):
    new_x = random.randint(central_area.left, central_area.right - DUMPLING_SIZE)
    new_y = random.randint(central_area.top, central_area.bottom - DUMPLING_SIZE)
    dumpling_positions.append((new_x, new_y))

def update_photos(photo_positions, last_photo_time, current_time):
    if current_time - last_photo_time > PHOTO_INTERVAL_MS:
        last_photo_x, last_photo_y = photo_positions[-1]
        new_photo_x = last_photo_x + PHOTO_SPACING
        if new_photo_x + PHOTO_SIZE[0] <= SCREEN_WIDTH:
            photo_positions.append((new_photo_x, 0))
            return current_time  # Update the time a photo was last added
    return last_photo_time

def draw_screen(dumpling_positions, photo_positions):
    screen.fill(WHITE)
    screen.blit(BACKGROUND, (0, 0))
    for pos in dumpling_positions:
        screen.blit(DUMPLING, pos)
    for pos in photo_positions:
        screen.blit(NEW_PHOTO, pos)
    pygame.display.flip()

def CookingGame():
    done = False
    dumpling_positions = []
    photo_positions = [(0, 0)]  # Start with one photo at the top left
    last_photo_time = pygame.time.get_ticks()
    
    # Define a smaller central area for dumplings to appear
    central_area = pygame.Rect(
        (SCREEN_WIDTH - SCREEN_WIDTH // 3) // 2, 
        (SCREEN_HEIGHT - SCREEN_HEIGHT // 3) // 2, 
        SCREEN_WIDTH // 3, 
        SCREEN_HEIGHT // 3
    )
    # temporary player
    player = Player(name="John", password="CookingForLife", best_game="Cooking Game", best_score=20, add_score=1, mul_score=1, div_score=1, sub_score=1)
    
    current_question = Question(player.name, player.password, player.best_game,
                                player.best_score, player.add_score, player.mul_score,
                                player.div_score, player.sub_score)
    show_question = current_question.generate_question('-')
    print(show_question)

    while not done:
        current_time = pygame.time.get_ticks()
        done = not handle_events(dumpling_positions, central_area)
        last_photo_time = update_photos(photo_positions, last_photo_time, current_time)
        draw_screen(dumpling_positions, photo_positions)
        clock.tick(60)  # Limit to 60 frames per second

    pygame.quit()

CookingGame()

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
PHOTO_INTERVAL_MS = 4000
PHOTO_SPACING = 150

# Colors
WHITE = (255, 255, 255)

# Load images
BACKGROUND = pygame.image.load("images/cooking_game.png")
DUMPLING = pygame.image.load("images/dumpling.png")
DUMPLING = pygame.transform.scale(DUMPLING, (DUMPLING_SIZE, DUMPLING_SIZE))
ORDER = pygame.image.load("images/order.png")
ORDER = pygame.transform.scale(ORDER, PHOTO_SIZE)

# Initialize the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('COOKING GAME')

# Clock for controlling game speed
clock = pygame.time.Clock()

font = pygame.font.Font("fonts/Shojumaru-Regular.ttf", 20)

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
            elif event.key == pygame.K_LEFT and dumpling_positions:
                dumpling_positions.pop()
                number_of_dumplings -= 1
    return True

def add_dumpling(dumpling_positions, central_area):
    new_x = random.randint(central_area.left, central_area.right - DUMPLING_SIZE)
    new_y = random.randint(central_area.top, central_area.bottom - DUMPLING_SIZE)
    dumpling_positions.append((new_x, new_y))


def update_photos(photo_positions, last_photo_time, current_time):
    photo_added = False  # Track if a new photo is added
    if current_time - last_photo_time > PHOTO_INTERVAL_MS:
        last_photo_x, last_photo_y = photo_positions[-1]
        new_photo_x = last_photo_x + PHOTO_SPACING
        if new_photo_x + PHOTO_SIZE[0] <= SCREEN_WIDTH:
            photo_positions.append((new_photo_x, 0))
            last_photo_time = current_time
            photo_added = True  # A new photo was added
    return last_photo_time, photo_added

def draw_screen(dumpling_positions, photo_positions, questions):
    screen.fill(WHITE)
    screen.blit(BACKGROUND, (0, 0))
    for pos in dumpling_positions:
        screen.blit(DUMPLING, pos)
    for i, pos in enumerate(photo_positions):
        screen.blit(ORDER, pos)
        if i < len(questions):
            question_text = questions[i]
            # Adjust text_surface creation to consider the size of the photo
            text_surface = font.render(question_text, True, (0, 0, 0))  # Black text
            # Calculate text position to center it on the photo
            text_x_adjustment = 30  # Adjust as needed for leftward movement
            text_y_adjustment = 50  # Adjust as needed for upward movement

            text_x = pos[0] + (PHOTO_SIZE[0] - text_surface.get_width()) // 2 - text_x_adjustment
            text_y = pos[1] + (PHOTO_SIZE[1] - text_surface.get_height()) // 2 - text_y_adjustment
            screen.blit(text_surface, (text_x, text_y))

    pygame.display.flip()

def CookingGame():
    done = False
    dumpling_positions = []
    photo_positions = [(0, 0)]  # Start with one photo at the top left
    questions = []  # Initialize an empty list to store questions
    last_photo_time = pygame.time.get_ticks() #- PHOTO_INTERVAL_MS  # Adjust to trigger immediate photo
    
    central_area = pygame.Rect(
        (SCREEN_WIDTH - SCREEN_WIDTH // 3) // 2, 
        (SCREEN_HEIGHT - SCREEN_HEIGHT // 3) // 2, 
        SCREEN_WIDTH // 3, 
        SCREEN_HEIGHT // 3
    )
    
    player = Player(name="John", password="CookingForLife", best_game="Cooking Game", best_score=20, add_score=1, mul_score=1, div_score=1, sub_score=20)
    
    current_question = Question(player.name, player.password, player.best_game, player.best_score, player.add_score, player.mul_score, player.div_score, player.sub_score)
    
    # Immediately generate a question for the initial photo
    question_text = current_question.generate_question('-')
    questions.append(question_text[0])
    print(question_text[0])
    print(question_text[1])

    while not done:
        current_time = pygame.time.get_ticks()
        done = not handle_events(dumpling_positions, central_area)
        last_photo_time, photo_added = update_photos(photo_positions, last_photo_time, current_time)
        if photo_added:
            # Generate a new question for each new photo and append it to the questions list
            question_text = current_question.generate_question('-')
            questions.append(question_text[0])
            print(question_text[0])
            print(question_text[1])
        draw_screen(dumpling_positions, photo_positions, questions)
        clock.tick(60)  # Limit to 60 frames per second

    pygame.quit()

CookingGame()

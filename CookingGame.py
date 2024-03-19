import pygame
import random
from question import Question  # Make sure this import matches your file structure

class CookingGame:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.dumpling_size = 100
        self.photo_size = (200, 250)
        self.photo_interval_ms = 5000
        self.photo_spacing = 150
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('COOKING GAME')
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("images/cooking_game.png")
        self.dumpling = pygame.image.load("images/dumpling.png")
        self.dumpling = pygame.transform.scale(self.dumpling, (self.dumpling_size, self.dumpling_size))
        self.new_photo = pygame.image.load("images/order.png")
        self.new_photo = pygame.transform.scale(self.new_photo, self.photo_size)
        self.last_photo_time = pygame.time.get_ticks()
        self.photo_positions = [(0, 0)]  # Initial photo position
        self.dumpling_positions = []
        self.questions = []  # Store questions for each photo
        
        
        
        
        self.player = Question("PlayerName", "PlayerPassword", "CookingGame", 100, 10, 10, 10, 5, ["CookingGame"])
        
        
        
        

    def run(self):
        done = False
        while not done:
            current_time = pygame.time.get_ticks()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.add_dumpling()
                    elif event.key == pygame.K_LEFT and self.dumpling_positions:
                        self.dumpling_positions.pop()

            self.handle_photos_and_questions(current_time)
            self.draw()

        pygame.quit()

    def add_dumpling(self):
        new_x = random.randint(0, self.screen_width - self.dumpling_size)
        new_y = random.randint(0, self.screen_height - self.dumpling_size)
        self.dumpling_positions.append((new_x, new_y))

    def handle_photos_and_questions(self, current_time):
        if current_time - self.last_photo_time > self.photo_interval_ms:
            last_photo_x, last_photo_y = self.photo_positions[-1]
            new_photo_x = last_photo_x + self.photo_spacing
            if new_photo_x + self.photo_size[0] <= self.screen_width:
                self.photo_positions.append((new_photo_x, 0))
                self.last_photo_time = current_time
                question = self.player.generate_question('-')[0]  # Assume we only want the question string
                self.questions.append(question)

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))
        for pos in self.dumpling_positions:
            self.screen.blit(self.dumpling, pos)
        font = pygame.font.SysFont(None, 24)
        for i, pos in enumerate(self.photo_positions):
            self.screen.blit(self.new_photo, pos)
            if i < len(self.questions):
                question_surf = font.render(self.questions[i], True, (0, 0, 0))
                self.screen.blit(question_surf, (pos[0], pos[1] + self.photo_size[1] + 10))
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == "__main__":
    game = CookingGame()
    game.run()




"""
#without question being added

import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DUMPLING_SIZE = 100
PHOTO_SIZE = (200, 250)  # Size of the new photo
PHOTO_INTERVAL_MS = 5000  # 5 seconds in milliseconds (updated as per your last code)
PHOTO_SPACING = 150  # Adjust this to control spacing between photos

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('COOKING GAME')

done = False
clock = pygame.time.Clock()

BACKGROUND = pygame.image.load("images/cooking_game.png")
DUMPLING = pygame.image.load("images/dumpling.png")  # Replace with your image file path
DUMPLING = pygame.transform.scale(DUMPLING, (DUMPLING_SIZE, DUMPLING_SIZE))
NEW_PHOTO = pygame.image.load("images/order.png")  # Load the new photo here
NEW_PHOTO = pygame.transform.scale(NEW_PHOTO, PHOTO_SIZE)  # Resize the new photo

# Initialize the timer for photo appearances
last_photo_time = pygame.time.get_ticks()  
# Start with one photo at the top left
photo_positions = [(0, 0)]  

# Define a smaller central area rectangle (x, y, width, height)
CENTRAL_AREA_WIDTH = SCREEN_WIDTH // 3
CENTRAL_AREA_HEIGHT = SCREEN_HEIGHT // 3
CENTRAL_AREA = pygame.Rect(
    (SCREEN_WIDTH - CENTRAL_AREA_WIDTH) // 2, 
    (SCREEN_HEIGHT - CENTRAL_AREA_HEIGHT) // 2, 
    CENTRAL_AREA_WIDTH, 
    CENTRAL_AREA_HEIGHT
)

dumpling_positions = []

while not done:
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                new_x = random.randint(CENTRAL_AREA.left, CENTRAL_AREA.right - DUMPLING_SIZE)
                new_y = random.randint(CENTRAL_AREA.top, CENTRAL_AREA.bottom - DUMPLING_SIZE)
                dumpling_positions.append((new_x, new_y))
            elif event.key == pygame.K_LEFT and dumpling_positions:
                dumpling_positions.pop()

    if current_time - last_photo_time > PHOTO_INTERVAL_MS:
        last_photo_x, last_photo_y = photo_positions[-1]
        new_photo_x = last_photo_x + PHOTO_SPACING  # Adjusted for closer spacing
        # Ensure new photo positions do not exceed the screen width
        if new_photo_x + PHOTO_SIZE[0] > SCREEN_WIDTH:
            # Adjust logic as needed if photos reach the end of the screen width
            pass
        else:
            photo_positions.append((new_photo_x, 0))
            last_photo_time = current_time

    screen.fill((255, 255, 255))  # Clear the screen
    screen.blit(BACKGROUND, (0, 0))  # Draw the background

    for pos in dumpling_positions:
        screen.blit(DUMPLING, pos)

    for pos in photo_positions:
        screen.blit(NEW_PHOTO, pos)

    pygame.display.flip()  # Update the screen with what we've drawn
    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()

"""
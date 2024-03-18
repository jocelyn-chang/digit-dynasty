# Import appropriate libraries
import pygame, sys

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize Pygame
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = pygame.image.load("images/background.png")

# Button class for image-based buttons
class Button():
    def __init__(self, image = None, pos = (0,0)):
        self.image = image
        self.x_pos, self.y_pos = pos
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)

    def checkInput(self, position):
        return self.rect.collidepoint(position)


# Go to login screen
def start_game():
    while True:
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        LOGIN = pygame.image.load("images/login_screen.png")

        input_username = pygame.Rect(300, 200, 140, 32)
        input_password = pygame.Rect(300, 250, 140, 32)
        inactive_colour = pygame.Color('lightskyblue3')
        active_colour = pygame.Color('dodgerblue2')
        active = False  # track is input box active

        username = ''
        password = ''

        '''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN: # if user clicks on input box, toggle active variable
                    if input_username.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    colour = active_colour if active else inactive_colour
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
        '''


                            

# Go to load screen 
def load_game():
    while True:
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SIGN_UP = pygame.image.load("images/sign_up_screen.png")

# Go to the high score table
def high_score():
    while True:
        GAME_MOUSE_POS = pygame.get_pos()

        SCREEN.fill("black")
        HIGH_SCORE = pygame.image.load("images/high_score_screen.png")

# Intructions screen
def instructions():
    while True:
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        INSTRUCTIONS = pygame.image.load("images/instruction_screen.png")

# Main Menu screen
def main_menu():

    while True:
        SCREEN.blit(BACKGROUND, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        START_BUTTON = Button(image = pygame.image.load("images/new_game.png"), pos = (395, 95))
        LOAD_BUTTON = Button(image = pygame.image.load("images/load_game.png"), pos = (395, 195))
        HIGH_SCORE_BUTTON = Button(image = pygame.image.load("images/high_score.png"), pos = (395, 295))
        INSTRUCTIONS_BUTTON = Button(image = pygame.image.load("images/instructions.png"), pos = (395, 395))
        EXIT_BUTTON = Button(image = pygame.image.load("images/exit.png"), pos = (395, 495))

        for button in [START_BUTTON, LOAD_BUTTON, HIGH_SCORE_BUTTON, INSTRUCTIONS_BUTTON, EXIT_BUTTON]:
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.checkInput(MENU_MOUSE_POS):
                    start_game()
                if LOAD_BUTTON.checkInput(MENU_MOUSE_POS):
                    load_game()
                if HIGH_SCORE_BUTTON.checkInput(MENU_MOUSE_POS):
                    high_score()
                if INSTRUCTIONS_BUTTON.checkInput(MENU_MOUSE_POS):
                    instructions()
                if EXIT_BUTTON.checkInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

main_menu()
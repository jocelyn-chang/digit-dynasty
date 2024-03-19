# Import appropriate libraries
import pygame, sys

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize Pygame
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = pygame.image.load("images/background.png")
LOGIN = pygame.image.load("images/login_screen.png")
HIGH_SCORE = pygame.image.load("images/leaderboard_screen.png")

def get_font(size):
    return pygame.font.Font("fonts/Shojumaru-Regular.ttf", size)

# Button class for image-based buttons
class Button():
    def __init__(self, image = None, pos = (0,0), text_input = "", font = 0, base_colour = "Black", hovering_colour = "White"):
        if isinstance(image, str):
            self.image = pygame.image.load(image)
        else:
            self.image = image
        self.x_pos, self.y_pos = pos
        self.font = font
        self.base_colour, self.hovering_colour = base_colour, hovering_colour
        self.text_input = text_input
        if self.font:
            self.text = self.font.render(self.text_input, True, pygame.Color(self.base_colour))
        else:
            self.text = None
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        if self.text:
            text_rect = self.text.get_rect(center = self.rect.center)
            screen.blit(self.text, text_rect)

            # Shadow offset
            shadow_offset = 2

            # Draw shadow first
            shadow_color = (135, 135, 135)  # Black shadow
            shadow_text = self.font.render(self.text_input, True, shadow_color)
            shadow_rect = shadow_text.get_rect(center=(self.rect.centerx + shadow_offset, self.rect.centery + shadow_offset))
            screen.blit(shadow_text, shadow_rect)

            # Draw the actual text
            screen.blit(self.text, text_rect)

    def checkInput(self, position):
        return self.rect.collidepoint(position)
    
    def changeColour(self, position):
        if self.rect.collidepoint(position):
            if self.font:
                self.text = self.font.render(self.text_input, True, pygame.Color(self.hovering_colour))
            else:
                if self.font:
                    self.text = self.font.render(self.text_input, True, pygame.Color(self.base_colour))


# Go to login screen
def start_game():
    while True:
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(LOGIN, (0, 0))
        START_BACK = Button(image = "images/back_button.png", pos = (70, 55), text_input = "", font = get_font(15), base_colour = "White", hovering_colour = "#b51f09")
        START_BACK.changeColour(GAME_MOUSE_POS)
        START_BACK.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BACK.checkInput(GAME_MOUSE_POS):
                    main_menu()

        pygame.display.update()             

# Go to load screen 
def load_game():
    while True:
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SIGN_UP = pygame.image.load("images/sign_up_screen.png")

# Go to the high score table
def high_score():
    while True:
        SCORE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(HIGH_SCORE, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

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

        START_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 75), text_input = "NEW GAME", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")
        LOAD_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 189), text_input = "LOAD GAME", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")
        HIGH_SCORE_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 303), text_input = "HIGH SCORES", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")
        INSTRUCTIONS_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 417), text_input = "INSTRUCTIONS", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")
        EXIT_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 531), text_input = "EXIT", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")

        for button in [START_BUTTON, LOAD_BUTTON, HIGH_SCORE_BUTTON, INSTRUCTIONS_BUTTON, EXIT_BUTTON]:
            button.changeColour(MENU_MOUSE_POS)
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
# Import appropriate libraries
import pygame, sys
from Button import Button

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize Pygame
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = pygame.image.load("images/background.png")
LOGIN = pygame.image.load("images/login_screen.png")
SIGNUP = pygame.image.load("images/sign_up_screen.png")
HIGH_SCORE = pygame.image.load("images/leaderboard_screen.png")
INSTRUCTIONS = pygame.image.load("images/instructions_screen.png")
BACK = pygame.image.load("images/back_button.png")
RESIZED_BACK = pygame.image.load("images/resized_back.png")

def get_font(font, size):
    if font == "Sawarabi":
        return pygame.font.Font("fonts/SawarabiMincho-Regular.ttf", size)
    elif font == "Shojumaru":
        return pygame.font.Font("fonts/Shojumaru-Regular.ttf", size)

# Create a function to create the input boxes
def input_box(screen, input_rect, text, font, active = False, is_password = False):
    colour_active = pygame.Color('lightskyblue3')
    colour_passive = pygame.Color('gray15')
    colour = colour_active if active else colour_passive

    box = pygame.Surface((input_rect.width, input_rect.height), pygame.SRCALPHA)
    box.fill((255, 255, 255, 100))
    SCREEN.blit(box, input_rect.topleft)

    if active:
        pygame.draw.rect(SCREEN, colour, input_rect, 2)

    display_text = ''.join('*' for _ in text) if is_password else text
    text_surface = font.render(display_text, True, pygame.Color('black'))
    SCREEN.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

# Go to login screen
def start_game():
    username = ''
    password = ''
    username_active = False
    password_active = False
    input_font = get_font("Sawarabi",35)

    username_rect = pygame.Rect(254, 237, 300, 50)
    password_rect = pygame.Rect(254, 378, 300, 50)

    while True:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(SIGNUP, (0, 0))
        
        START_BACK = Button(image = "images/back_button.png", pos = (70, 55), text_input = "", font = get_font("Shojumaru",22), base_colour = "White", hovering_colour = "#b51f09")
        if (40<MOUSE_X<75 and 40<MOUSE_Y<70):
            SCREEN.blit(RESIZED_BACK, (-90,-96))
        
        START_BACK.update(SCREEN)

        input_box(SCREEN, username_rect, username, input_font, active = username_active)
        input_box(SCREEN, password_rect, password, input_font, active = password_active, is_password = True)

        PLAY_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 531), text_input = "PLAY", font = get_font("Shojumaru",22), base_colour = "#b51f09", hovering_colour = "White")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BACK.checkInput(GAME_MOUSE_POS):
                    main_menu()
                elif username_rect.collidepoint(event.pos):
                    username_active = not username_active
                    password_active = False
                elif password_rect.collidepoint(event.pos):
                    password_active = not password_active
                    username_active = False
                else:
                    username_active = False
                    password_active = False
            if event.type== pygame.KEYDOWN:
                if username_active:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif password_active:
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode

        PLAY_BUTTON.update(SCREEN)
        pygame.display.flip()             

# Go to load screen 
def load_game():
    username = ''
    password = ''
    username_active = False
    password_active = False
    input_font = get_font("Sawarabi",35)

    username_rect = pygame.Rect(254, 237, 300, 50)
    password_rect = pygame.Rect(254, 378, 300, 50)

    while True:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(LOGIN, (0, 0))
        
        LOAD_BACK = Button(image = "images/back_button.png", pos = (70, 55), text_input = "", font = get_font("Shojumaru",22), base_colour = "White", hovering_colour = "#b51f09")
        if (40<MOUSE_X<75 and 40<MOUSE_Y<70):
            SCREEN.blit(RESIZED_BACK, (-90,-96))
        
        LOAD_BACK.update(SCREEN)

        PLAY_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 531), text_input = "PLAY", font = get_font("Shojumaru",22), base_colour = "#b51f09", hovering_colour = "White")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LOAD_BACK.checkInput(GAME_MOUSE_POS):
                    main_menu()
                elif username_rect.collidepoint(event.pos):
                    username_active = not username_active
                    password_active = False
                elif password_rect.collidepoint(event.pos):
                    password_active = not password_active
                    username_active = False
                else:
                    username_active = False
                    password_active = False
            if event.type== pygame.KEYDOWN:
                if username_active:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif password_active:
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode

        input_box(SCREEN, username_rect, username, input_font, active = username_active)
        input_box(SCREEN, password_rect, password, input_font, active = password_active, is_password = True)
        
        PLAY_BUTTON.update(SCREEN)
        pygame.display.flip()

# Go to the high score table
def high_score():
    while True:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(HIGH_SCORE, (0, 0))
        
        SCORE_BACK = Button(image = "images/back_button.png", pos = (70, 55), text_input = "", font = get_font("Shojumaru",15), base_colour = "White", hovering_colour = "#b51f09")
        if (40<MOUSE_X<75 and 40<MOUSE_Y<70):
            SCREEN.blit(RESIZED_BACK, (-90,-96))
        
        SCORE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SCORE_BACK.checkInput(GAME_MOUSE_POS):
                    main_menu()

        pygame.display.update()


# Intructions screen
def instructions():
    while True:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(INSTRUCTIONS, (0, 0))
        
        INSTRUCTIONS_BACK = Button(image = "images/back_button.png", pos = (70, 55), text_input = "", font = get_font("Shojumaru",15), base_colour = "White", hovering_colour = "#b51f09")
        if (40<MOUSE_X<75 and 40<MOUSE_Y<70):
            SCREEN.blit(RESIZED_BACK, (-90,-96))
        
        INSTRUCTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkInput(GAME_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# Main Menu screen
def main_menu():

    while True:
        SCREEN.blit(BACKGROUND, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        START_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 75), text_input = "NEW GAME", font = get_font("Shojumaru",22), base_colour = "#b51f09", hovering_colour = "White")
        LOAD_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 189), text_input = "LOAD GAME", font = get_font("Shojumaru",22), base_colour = "#b51f09", hovering_colour = "White")
        HIGH_SCORE_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 303), text_input = "HIGH SCORES", font = get_font("Shojumaru",22), base_colour = "#b51f09", hovering_colour = "White")
        INSTRUCTIONS_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 417), text_input = "INSTRUCTIONS", font = get_font("Shojumaru",22), base_colour = "#b51f09", hovering_colour = "White")
        EXIT_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 531), text_input = "EXIT", font = get_font("Shojumaru",22), base_colour = "#b51f09", hovering_colour = "White")

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
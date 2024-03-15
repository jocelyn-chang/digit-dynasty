# Import appropriate libraries
import pygame, sys
from button import Button

# Initialize the Pygame library
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = pygame.image.load("images/background.png")


        

# Go to screen with main map
def start_game():
    while True:
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

# Intructions screen
def instructions():

# Controls screen
def controls():

# Main Menu screen
def main_menu():

    while True:
        SCREEN.blit(BACKGROUND, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        START_BUTTON = Button(image = pygame.image.load("images/new_game.png"), pos = (640, 250))
        LOAD_BUTTON = Button(image = pygame.image.load("images/load_game.png"), pos = (640, 350))
        HIGH_SCORE_BUTTON = Button(image = pygame.image.load("image/high_score.png"), pos = (640, 450))
        INSTRUCTIONS_BUTTON = Button(image = pygame.image.load("image/instructions.png"), pos = (640, 550))
        EXIT_BUTTON = Button(image = pygame.image.load("images/exit.png"), pos = (640, 650))

        for event in [START_BUTTON, LOAD_BUTTON, HIGH_SCORE_BUTTON, INSTRUCTIONS_BUTTON, EXIT_BUTTON]:
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
                if INSTRUCTIONS.checkInput(MENU_MOUSE_POS):
                    instructions()
                if QUIT_BUTTON.checkInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.dsplay.update()

main_menu()
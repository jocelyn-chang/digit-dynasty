# Import appropriate libraries
import pygame, sys
from button import Button

# Initialize the Pygame library
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("images/Background.png")

# Return text in desired size
def get_font(size):

# Main Menu screen
def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.blit(background, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        

# Go to screen with main map
def start_game():

# Intructions screen
def instructions():

# Controls screen
def controls():



run = True
while run:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

pygame.quit()

class Button():
    def __init__(self, image, pos, base_colour, hovering_colour):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.base_colour, self.hovering_colour = base_colour, hovering_colour
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))

        def update(self, screen):
            if self.image is not None:
                screen.blit(elf.image, self.rect)
            screen.blit(self.text, self.text_rect)

        def checkInput(self, position):
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                return True
            return False

    
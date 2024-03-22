# Import appropriate libraries
import pygame, sys, csv
from Button import Button

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SANDWICH STACK')
BACKGROUND = pygame.image.load("images/sandwich_stack_bg.png")

PANDA = pygame.image.load("images/panda_tray.png")
CARROT = pygame.image.load("images/carrot.png")
BREAD = pygame.image.load("images/bread.png")
CUCUMBER = pygame.image.load("images/cucumber.png")
MEAT = pygame.image.load("images/meat.png")

def sandwich_stack():
    while True:
        SCREEN.blit(BACKGROUND, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

sandwich_stack()
import pygame
from Button import Button

pygame.init()

#Load Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Load Images
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DIGIT DYNASTY')
BACKGROUND = pygame.image.load("images/AE_background.png")
EMPERORMONKEY = pygame.image.load("images/emperor_monkey.png")
EMPERORPIG = pygame.image.load("images/emperor_pig.png")
EMPERORPHOENIX = pygame.image.load("images/emperor_phoenix.png")
EMPERORDRAGON = pygame.image.load("images/emperor_dragon.png")

#Set up Variables
emperorLevel = 0
pandaHealth = 100
emperorHealth = 100 #multiply these by emperor level once determined
addAttackPower = 10 #multiply these by strength once determined
emperorHealthDisplayFactor = 188/emperorHealth
pandaHealthDisplayFactor = 188/pandaHealth
subAttackPower = 10
mulAttackPower = 10
divAttackPower = 10

def get_font(font, size):
    if font == "Sawarabi":
        return pygame.font.Font("fonts/SawarabiMincho-Regular.ttf", size)
    elif font == "Shojumaru":
        return pygame.font.Font("fonts/Shojumaru-Regular.ttf", size)

def attack_emperor(attackType):
  global emperorHealth, emperorHealthDisplay
  emperorHealth = emperorHealth - attackType

def start_game():
  global emperorHealth, emperorHealthDisplayFactor, pandaHealthDisplayFactor
  while True:

    # Draw the background image onto the screen
    SCREEN.blit(BACKGROUND, (0, 0))
    SCREEN.blit(EMPERORMONKEY, (460, 40))
    pygame.draw.rect(SCREEN, (239, 39, 39), pygame.Rect(130, 102, emperorHealthDisplayFactor*emperorHealth, 20))
    pygame.draw.rect(SCREEN, (239, 39, 39), pygame.Rect(543, 430, 188, 20))

    #Get Mouse Pos
    MOUSE_POS = pygame.mouse.get_pos()  

    #Attack Buttons
    ADD_BUTTON = Button(image = None, pos = (500, 520), text_input = "Addition", font = get_font("Sawarabi",24), base_colour = "black", hovering_colour = "#d73c37")
    DIV_BUTTON = Button(image = None, pos = (500, 560), text_input = "Division", font = get_font("Sawarabi",24), base_colour = "black", hovering_colour = "#d73c37")
    SUB_BUTTON = Button(image = None, pos = (690, 520), text_input = "Subtraction", font = get_font("Sawarabi",24), base_colour = "black", hovering_colour = "#d73c37")
    MUL_BUTTON = Button(image = None, pos = (700, 560), text_input = "Multiplication", font = get_font("Sawarabi",24), base_colour = "black", hovering_colour = "#d73c37")

    for button in [ADD_BUTTON, DIV_BUTTON, SUB_BUTTON, MUL_BUTTON]:
      button.changeColour(MOUSE_POS)
      button.update(SCREEN)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if ADD_BUTTON.checkInput(MOUSE_POS):
            attack_emperor(addAttackPower)
        if DIV_BUTTON.checkInput(MOUSE_POS):
            attack_emperor(divAttackPower)
        if SUB_BUTTON.checkInput(MOUSE_POS):
            attack_emperor(subAttackPower)
        if MUL_BUTTON.checkInput(MOUSE_POS):
            attack_emperor(mulAttackPower)

    mouse_x, mouse_y = MOUSE_POS
    font = pygame.font.Font(None, 36)
    text = font.render(f"Mouse Position: ({mouse_x}, {mouse_y})", True, (0,0,0))
    SCREEN.blit(text,(10,10))

    # Update the display
    pygame.display.flip()

start_game()
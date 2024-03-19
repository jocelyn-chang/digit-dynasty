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

#Get Mouse Pos
MOUSE_POS = pygame.mouse.get_pos()

def get_font(font, size):
    if font == "Sawarabi":
        return pygame.font.Font("fonts/SawarabiMincho-Regular.ttf", size)
    elif font == "Shojumaru":
        return pygame.font.Font("fonts/Shojumaru-Regular.ttf", size)

ADD_BUTTON = Button(image = None, pos = (500, 520), text_input = "Addition", font = get_font("Sawarabi",24), base_colour = "black", hovering_colour = "#d73c37")
DIV_BUTTON = Button(image = None, pos = (500, 560), text_input = "Division", font = get_font("Sawarabi",24), base_colour = "black", hovering_colour = "#d73c37")
SUB_BUTTON = Button(image = None, pos = (690, 520), text_input = "Subtraction", font = get_font("Sawarabi",24), base_colour = "black", hovering_colour = "#d73c37")
MUL_BUTTON = Button(image = None, pos = (700, 560), text_input = "Multiplication", font = get_font("Sawarabi",24), base_colour = "black", hovering_colour = "#d73c37")

run = True
while run:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  
  # Draw the background image onto the screen
  SCREEN.blit(BACKGROUND, (0, 0))
  SCREEN.blit(EMPERORMONKEY, (460, 40))

  for button in [ADD_BUTTON, DIV_BUTTON, SUB_BUTTON, MUL_BUTTON]:
    button.changeColour(MOUSE_POS)
    button.update(SCREEN)

  # Update the display
  pygame.display.flip()

pygame.quit()
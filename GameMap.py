import pygame, sys
from Button import Button
from runningArmy import running_army

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DIGIT DYNASTY')
BACKGROUND = pygame.image.load("images/Map Screen.png")
LEFTTEMP = pygame.image.load("images/templeleft.png")
MULTTEMP = pygame.image.load("images/templeright.png")
TOPTEMP = pygame.image.load("images/templetop.png")
BOTTOMTEMP = pygame.image.load("images/templebottom.png")
MIDDLETEMP = pygame.image.load("images/templemiddle.png")
RESIZED_LEFTTEMP = pygame.transform.scale(LEFTTEMP, (110, 110))
RESIZED_MULTTEMP = pygame.transform.scale(MULTTEMP, (110, 110))
RESIZED_TOPTEMP = pygame.transform.scale(TOPTEMP, (103, 103))
RESIZED_BOTTOMTEMP = pygame.transform.scale(BOTTOMTEMP, (120, 120))
RESIZED_MIDDLETEMP = pygame.transform.scale(MIDDLETEMP, (150, 150))


# Main Colours
gold1 = (230, 224, 174)
gold2 = (223, 188, 94)
red1 = (238, 97, 70)
red2 = (215, 60, 55)
red3 = (181, 31, 9)

# Secondary Colours
green1 = (116, 217, 219)
green2 = (153, 216, 196)
green3 = (113, 182, 135)
green4 = (88, 133, 120)
green5 = (117, 132, 133)

# get the font
def get_font(size):
    return pygame.font.Font("fonts/Shojumaru-Regular.ttf", size)

def load_map():
  while True:

    MULTTEMP = Button(pygame.image.load("images/templeright.png"), pos = (600, 131), text_input = "", font = get_font(15), base_colour = "White", hovering_colour = "#b51f09")


    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        # Draw the background image onto the screen
    screen.blit(BACKGROUND, (0, 0))

    # Get the current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    MOUSE_POS = pygame.mouse.get_pos()

    # cooking game
    if (133<mouse_x<180 and 139<mouse_y<202):
      screen.blit(RESIZED_LEFTTEMP, (110, 92))

    # snake game
    if (372<mouse_x<419 and 32<mouse_y<95):
      screen.blit(RESIZED_TOPTEMP, (348, -2))
    
    # running army
    if (600<mouse_x<647 and 131<mouse_y<194):
      screen.blit(RESIZED_MULTTEMP, (582, 90))
      if event.type == pygame.MOUSEBUTTONDOWN:
        if MULTTEMP.checkInput(MOUSE_POS):
            running_army()
    
    # division game
    if (363<mouse_x<410 and 383<mouse_y<446):
      screen.blit(RESIZED_BOTTOMTEMP, (340, 352))
    
    # boss battle (arithmetic emperor)
    if (350<mouse_x<450 and 220<mouse_y<380):
      screen.blit(RESIZED_MIDDLETEMP, (326, 180))

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()
    mouse_x, mouse_y = mouse_pos

    # Display mouse position on the screen
    font = pygame.font.Font(None, 36)
    text = font.render(f"Mouse Position: ({mouse_x}, {mouse_y})", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    # Update the display
    pygame.display.flip()

  pygame.quit()

# load_map()
import pygame
import os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DIGIT DYNASTY')
BACKGROUND = pygame.image.load("images/Map Screen.png")
LEFTTEMP = pygame.image.load("images/templeleft.png")
RIGHTTEMP = pygame.image.load("images/templeright.png")
TOPTEMP = pygame.image.load("images/templetop.png")
BOTTOMTEMP = pygame.image.load("images/templebottom.png")
RESIZED_LEFTTEMP = pygame.transform.scale(LEFTTEMP, (110, 110))
RESIZED_RIGHTTEMP = pygame.transform.scale(RIGHTTEMP, (110, 110))
RESIZED_TOPTEMP = pygame.transform.scale(TOPTEMP, (103, 103))
RESIZED_BOTTOMTEMP = pygame.transform.scale(BOTTOMTEMP, (120, 120))


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

run = True
while run:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  
      # Draw the background image onto the screen
  screen.blit(BACKGROUND, (0, 0))

  # Get the current mouse position
  mouse_x, mouse_y = pygame.mouse.get_pos()

  if (133<mouse_x<180 and 139<mouse_y<202):
    screen.blit(RESIZED_LEFTTEMP, (110, 92))

  if (372<mouse_x<419 and 32<mouse_y<95):
    screen.blit(RESIZED_TOPTEMP, (348, -2))
  
  if (600<mouse_x<647 and 131<mouse_y<194):
    screen.blit(RESIZED_RIGHTTEMP, (582, 90))
  
  if (363<mouse_x<410 and 383<mouse_y<446):
    screen.blit(RESIZED_BOTTOMTEMP, (340, 352))


  # Update the display
  pygame.display.flip()

pygame.quit()
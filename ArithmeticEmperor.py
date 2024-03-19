import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DIGIT DYNASTY')
BACKGROUND = pygame.image.load("images/AE_background.png")
EMPERORMONKEY = pygame.image.load("images/emperor_monkey.png")
EMPERORPIG = pygame.image.load("images/emperor_pig.png")
EMPERORPHOENIX = pygame.image.load("images/emperor_phoenix.png")
EMPERORDRAGON = pygame.image.load("images/emperor_dragon.png")

run = True
while run:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  
  # Draw the background image onto the screen
  screen.blit(BACKGROUND, (0, 0))
  screen.blit(EMPERORMONKEY, (460, 40))

  # Update the display
  pygame.display.flip()

pygame.quit()
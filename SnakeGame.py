import pygame
import time
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SNAKE GAME')
BACKGROUND = pygame.image.load("images/snakegamebg.png")

clock = pygame.time.Clock()

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

# basic colours
black = (0, 0, 0)
white = (255, 255, 255)

snake_block = 15
snake_speed = 15

font_style = pygame.font.Font("fonts/Shojumaru-Regular.ttf", 25)

def current_score(score):
  # shadow text
  shadow = font_style.render("Score: " + str(score), True, green4)
  screen.blit(shadow, [652, 12])

  # main text
  main = font_style.render("Score: " + str(score), True, white)
  screen.blit(main, [650, 10])

def snake(snake_block, snake_list):
  for i in snake_list:
    pygame.draw.rect(screen, green2, [i[0], i[1], snake_block, snake_block])

def game():
  run = True 
  end = False

  x1 = SCREEN_WIDTH / 2
  y1 = SCREEN_HEIGHT /2

  x1_change = 0
  y1_change = 0

  snake_list = []
  snake_len = 1

  foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
  foody = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0

  while run:
    # when player loses
    while end == True:
      print("poop")

    screen.blit(BACKGROUND, (0, 0))

    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            if snake_block >= snake_block:
              x1_change = -snake_block
          elif event.key == pygame.K_RIGHT:
            if snake_block < SCREEN_WIDTH - snake_block:
              x1_change = snake_block
          elif event.key == pygame.K_UP:
            if y1_change >= snake_block:
              y1_change = -snake_block
          elif event.key == pygame.K_DOWN:
            if y1_change < SCREEN_HEIGHT - snake_block:
              y1_change = snake_block
    
    x1 += x1_change
    y1 += y1_change

    snake_list.append([x1, y1])

    # if len(snake_list) > snake_len:
    #   del snake_list

    snake(snake_block, snake_list)

    current_score(snake_len - 1)

    pygame.display.flip()

    if x1 == foodx and y1 == foody:
      foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
      foody = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
    
      snake_len += 1

    clock.tick(snake_speed)
  pygame.quit()

game()
# run = True
# while run:

#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       run = False
  
#   # Draw the background image onto the screen
#   screen.blit(BACKGROUND, (0, 0))
#   # testing
#   current_score(5)
#   snake(snake_block, [[300, 300], [315, 300]])
#   # Update the display
#   pygame.display.flip()

# pygame.quit()
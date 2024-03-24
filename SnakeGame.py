import pygame
import time
import random
from Player import Player

# Initialize Pygame
pygame.init()

# Initializing screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Creating screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SNAKE GAME')

# Create dark overlay for question screen
overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
overlay.set_alpha(128)  # Set transparency (0-255)
overlay.fill((0, 0, 0))  # Fill with black

# Load images
BACKGROUND = pygame.image.load("images/snakegamebg.png")
QBOX = pygame.image.load("images/snakegameqbox.png")

# Load fruit images and scale to the right size
fruit_size = (50, 50)
FRUIT_A = pygame.transform.scale(pygame.image.load("images/orangea.png").convert_alpha(), fruit_size)
FRUIT_B = pygame.transform.scale(pygame.image.load("images/orangeb.png").convert_alpha(), fruit_size)
FRUIT_C = pygame.transform.scale(pygame.image.load("images/orangec.png").convert_alpha(), fruit_size)
FRUIT_D = pygame.transform.scale(pygame.image.load("images/oranged.png").convert_alpha(), fruit_size)

# Clock for controlling game speed
clock = pygame.time.Clock()

# Colors
gold1 = (230, 224, 174)
gold2 = (223, 188, 94)
gold3 = (179, 152, 96)

red1 = (238, 97, 70)
red2 = (215, 60, 55)
red3 = (181, 31, 9)

green1 = (116, 217, 219)
green2 = (153, 216, 196)
green3 = (113, 182, 135)
green4 = (88, 133, 120)
green5 = (117, 132, 133)

black = (0, 0, 0)
white = (255, 255, 255)

# Snake block size and speed
snake_block = 20
snake_speed = 10

# Access the font style with changeable size
def get_font(size):
  return pygame.font.Font("fonts/Shojumaru-Regular.ttf", size)

# Function to display current score
def current_score(score):
  # Shadow text
  shadow = get_font(25).render("Score: " + str(score), True, green4)
  screen.blit(shadow, [652, 12]) # Displays text
    
  # Main text
  main = get_font(25).render("Score: " + str(score), True, white)
  screen.blit(main, [650, 10]) # Displays text

# Function to draw the snake
def snake(snake_block, snake_list):
  for i in snake_list:
    pygame.draw.rect(screen, green2, [i[0], i[1], snake_block, snake_block]) # Draws each rectangle of the snake at the right coordinates

# Shows the time left for the question
def timeLeft(time):
  # Shadow text
  shadow = get_font(25).render("Time Left: " + str(time), True, green4)
  screen.blit(shadow, [282, 62])
    
  # Main text
  main = get_font(25).render("Time Left: " + str(time), True, white)
  screen.blit(main, [280, 60])

# NEED TO CHANGE LATER TO USE THE QUESTION CLASS INSTEAD
# Generates the question and answer
def question(level):
  if level < 5: # For single digit addition
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
  else: # For double digit addition
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)

  ans = num1 + num2
  q = str(num1) + " + " + str(num2) + " = ?"
  return [q, ans]

# Generates the options for the question
def options(correctAns):
  opt1 = correctAns + random.randint(1, 5) # altered by adding a random number
  opt2 = correctAns - random.randint(1, correctAns-1) # altered by subtracting a random number below the answer
  opt3 = int(float(correctAns) * (10+random.randint(1, 5))//10) # altered by multiplying by a percentage of the answer

  if opt3 == opt2 or opt3 == opt1 or opt3 == correctAns: # changing opt3 if it rounds to a repeat number
    opt3 += 1

  optList = [opt1, opt2, opt3, correctAns] # list of options

  # Picks out and assigns a random option from the list
  optA = random.choice(optList)
  optList.remove(optA)
  if optA == correctAns:
    rightChoice = "optA"
  optB = random.choice(optList)
  optList.remove(optB)
  if optB == correctAns:
    rightChoice = "optB"
  optC = random.choice(optList)
  optList.remove(optC)
  if optC == correctAns:
    rightChoice = "optC"
  optD = random.choice(optList)
  if optD == correctAns:
    rightChoice = "optD"

  # Turn each option into text
  a = get_font(25).render(str(optA), True, black)
  b = get_font(25).render(str(optB), True, black)
  c = get_font(25).render(str(optC), True, black)
  d = get_font(25).render(str(optD), True, black)

  return [a, b, c, d, rightChoice]

# Create list of coordinates for the food
def foodCoordinates(x1, y1):
  # Randomize position of fruits
  foodCoord = [[x1, y1]]
  i = 0
  while i < 4:
    num1 = round(random.randrange(0, SCREEN_WIDTH -(snake_block + 40)) / 10.0) * 10.0
    num2 = round(random.randrange(0, SCREEN_HEIGHT - (snake_block + 40)) / 10.0) * 10.0
    while foodCoord.__contains__((num1, num2)):
      num1 = round(random.randrange(0, SCREEN_WIDTH - (snake_block + 40)) / 10.0) * 10.0
      num2 = round(random.randrange(0, SCREEN_HEIGHT - (snake_block + 40)) / 10.0) * 10.0
    foodCoord.append([num1, num2])
    i += 1
  return foodCoord

# Check if food's been eaten
def foodEaten(foodCoord, correctAns):
  snakex = foodCoord[0][0]
  snakey = foodCoord[0][1]
  if correctAns == "optA":
    answer = 1
  if correctAns == "optB":
    answer = 2
  if correctAns == "optC":
    answer = 3
  if correctAns == "optD":
    answer = 4
  i = 1
  while i < 5:
    if snakex >= (foodCoord[i][0]-20) and snakex <= (foodCoord[i][0]+30) and snakey >= (foodCoord[i][1]-20) and snakey <= (foodCoord[i][1]+40):
      if i != answer:
        return 1
      else:
        return 2
  return 0

# Main game function
def game(user):
  run = True 
  pause = True
  correct = False
  level = user.get_add()
  currQNA = question(level)
  currQ = currQNA[0]
  correctAns = currQNA[1]
  optionList = options(correctAns)

  # # Snake starting coordinates
  # x1 = SCREEN_WIDTH / 2
  # y1 = SCREEN_HEIGHT / 2

  # Initialize change in coordinates
  x1_change = 0
  y1_change = 0

  # List of snake body parts coordinates
  snake_list = []
  snake_len = 1


  # Randomize coordinates for each orange
  foodCoord = foodCoordinates(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

  # Delay the question screen
  elements_delay_counter = 20

  # Adjust counter according to level, 10 seconds for < 5 and 30 seconds otherwise
  if level < 5: 
    countdown = 600
    timerDown = 10
  else: 
    countdown = 1800
    timerDown = 30

  while run:
    # Event handling
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    # Control snake movement
    if not pause: 
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT]:
        x1_change = -snake_block
        y1_change = 0
      elif keys[pygame.K_RIGHT]:
        x1_change = snake_block
        y1_change = 0
      elif keys[pygame.K_UP]:
        y1_change = -snake_block
        x1_change = 0
      elif keys[pygame.K_DOWN]:
        y1_change = snake_block
        x1_change = 0

      # Update snake position
      foodCoord[0][0] += x1_change
      foodCoord[0][1] += y1_change
      # print("x1: " + str(x1))
      # print("y1: " + str(y1))

      snake_list.append([foodCoord[0][0], foodCoord[0][1]])

      # If snake length exceeds current length, remove the tail
      if len(snake_list) > snake_len:
        del snake_list[0]

    # Draw elements on screen
    screen.blit(BACKGROUND, (0, 0))
    
    # Blit overlay on top of everything
    if elements_delay_counter > 0:
      elements_delay_counter -= 1
      pause = True
    else:
      if countdown > 0 and pause == True and timerDown > 0:
        if countdown == 600:
          currQNA = question(level)
          currQ = currQNA[0]
          correctAns = currQNA[1]
          optionList = options(correctAns)
        print("hello")
        countdown -= 1
        screen.blit(overlay, (0, 0))
        screen.blit(QBOX, (141, 115))
        timeLeft(timerDown)
        # Shadow text
        shadow = get_font(65).render(currQ, True, gold3)
        # Main text
        main = get_font(65).render(currQ, True, white)
        if level < 5: 
          screen.blit(shadow, [242, 182])
          screen.blit(main, [240, 180])
        else:
          screen.blit(shadow, [202, 182])
          screen.blit(main, [200, 180])

        screen.blit(optionList[0], [315, 290])
        screen.blit(optionList[1], [315, 395])
        screen.blit(optionList[2], [505, 290])
        screen.blit(optionList[3], [505, 395])
        screen.blit(FRUIT_A, [245, 280])
        screen.blit(FRUIT_B, [245, 385])
        screen.blit(FRUIT_C, [438, 280])
        screen.blit(FRUIT_D, [438, 385])
        if countdown % 10 == 0 and timerDown > 0:
          timerDown -= 1

      else:
        pause = False

      if pause == False: 
        snake(snake_block, snake_list)
        current_score(snake_len - 1)
        screen.blit(FRUIT_A, (foodCoord[1][0], foodCoord[1][1]))
        screen.blit(FRUIT_B, (foodCoord[2][0], foodCoord[2][1]))
        screen.blit(FRUIT_C, (foodCoord[3][0], foodCoord[3][1]))
        screen.blit(FRUIT_D, (foodCoord[4][0], foodCoord[4][1]))
        pause == True
        
    if foodEaten(foodCoord, correctAns) == 2:
    # if foodCoord[0][0] >= (foodCoord[1][0]-20) and foodCoord[0][0] <= (foodCoord[1][0]+30) and foodCoord[0][1] >= (foodCoord[1][1]-20) and foodCoord[0][1] <= (foodCoord[1][1]+40):
      # foodx = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
      # foody = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0
      print("p")
      foodCoord = foodCoordinates(foodCoord[0][0], foodCoord[0][1])
      snake_len += 1
      pause == True
      elements_delay_counter = 20
      # change countdown to a minute later
      if level < 5:
        countdown = 600
        timerDown = 10
      else: 
        countdown = 1800
        timerDown = 30
  
    pygame.display.flip()

    clock.tick(snake_speed)

  pygame.quit()

# Run the game
person = Player("jocelyn", 12345678, 0, 0, 0, 0, 0, 0)
game(person)
# Import libraries and classes
import pygame, sys
import random
from Player import Player
from Button import Button
from Question import Question

# Initialize Pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(8)

# Initialize sounds for game
LOSS = pygame.mixer.Sound("sound/LossSound.mp3")
WIN = pygame.mixer.Sound("sound/LevelComplete.mp3")
CORRECT = pygame.mixer.Sound("sound/Correct.mp3")
INCORRECT = pygame.mixer.Sound("sound/Incorrect.mp3")

# Colors
GOLD3 = (179, 152, 96)

GREEN2 = (153, 216, 196)
GREEN4 = (88, 133, 120)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initializing screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Creating screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SNAKE GAME')

# Create dark overlay for question screen
overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
overlay.set_alpha(128)  # Set transparency (0-255)
overlay.fill(BLACK)  # Fill with black

# Load images
BACKGROUND = pygame.image.load("images/snakegamebg.png")
QBOX = pygame.image.load("images/snakegameqbox.png")
INSTRUCTION1 = pygame.image.load("images/additionInstructions.png")
INSTRUCTION2 = pygame.image.load("images/snakeSumsInstructions.png")
BACK = pygame.image.load("images/back_button.png")
RESIZED_BACK = pygame.image.load("images/resized_back.png")
RESIZED_NEXT = pygame.transform.rotate(pygame.image.load("images/resized_back.png"), 180)
START_SCREEN = pygame.image.load("images/snakesumsstart.png")
LOST_SCREEN = pygame.image.load("images/lostscreensnake.png")
WIN_SCREEN = pygame.image.load("images/winscreensnake.png")

# Load fruit images and scale to the right size
FRUIT_SIZE = (50, 50)
BORDER_SIZE = (60, 60)
FRUIT_A = pygame.transform.scale(pygame.image.load("images/orangea.png").convert_alpha(), FRUIT_SIZE)
FRUIT_B = pygame.transform.scale(pygame.image.load("images/orangeb.png").convert_alpha(), FRUIT_SIZE)
FRUIT_C = pygame.transform.scale(pygame.image.load("images/orangec.png").convert_alpha(), FRUIT_SIZE)
FRUIT_D = pygame.transform.scale(pygame.image.load("images/oranged.png").convert_alpha(), FRUIT_SIZE)
FRUIT_BORDER = pygame.transform.scale(pygame.image.load("images/orangeborder.png").convert_alpha(), BORDER_SIZE)

# Clock for controlling game speed
clock = pygame.time.Clock()

# Snake block size and speed
snake_block = 20
snake_speed = 8

# Access the font style with changeable size
def get_font(size):
  return pygame.font.Font("fonts/Shojumaru-Regular.ttf", size)

# Function to display current score
def current_score(score):
  # Shadow text
  shadow = get_font(25).render("Score: " + str(score), True, GREEN4)
  SCREEN.blit(shadow, [652, 12]) 
    
  # Main text
  main = get_font(25).render("Score: " + str(score), True, WHITE)
  SCREEN.blit(main, [650, 10]) 

# Function to display current level
def current_level(level):
  # Shadow text
  shadow = get_font(25).render("Level: " + str(level), True, GREEN4)
  SCREEN.blit(shadow, [502, 12])
    
  # Main text
  main = get_font(25).render("Level: " + str(level), True, WHITE)
  SCREEN.blit(main, [500, 10]) 

# Function to draw the snake
def snake(snake_block, snake_list):
  for i in snake_list:
    pygame.draw.rect(SCREEN, GREEN2, [i[0], i[1], snake_block, snake_block]) # Draws each rectangle of the snake at the right coordinates

# Shows the time left for the question
def time_left(time):
  # Shadow text
  shadow = get_font(25).render("Time Left: " + str(time), True, GREEN4)
  SCREEN.blit(shadow, [282, 62])
    
  # Main text
  main = get_font(25).render("Time Left: " + str(time), True, WHITE)
  SCREEN.blit(main, [280, 60])

# Generates the options for the question
def options(correct_ans):
  opt1 = correct_ans + random.randint(1, 5) # Altered by adding a random number
  opt2 = correct_ans - random.randint(1, correct_ans-1) # Altered by subtracting a random number below the answer
  opt3 = int(float(correct_ans) * (10+random.randint(1, 5))//10) # Altered by multiplying by a percentage of the answer

  # FIX THIS IF YOU CAN
  if opt3 == opt2 or opt3 == opt1 or opt3 == correct_ans: # Changing opt3 if it rounds to a repeat number
    opt3 += 1

  opt_list = [opt1, opt2, opt3, correct_ans] # List of options

  # Picks out and assigns a random option from the list
  optA = random.choice(opt_list)
  opt_list.remove(optA)
  if optA == correct_ans:
    right_opt = "optA"
  optB = random.choice(opt_list)
  opt_list.remove(optB)
  if optB == correct_ans:
    right_opt = "optB"
  optC = random.choice(opt_list)
  opt_list.remove(optC)
  if optC == correct_ans:
    right_opt = "optC"
  optD = random.choice(opt_list)
  if optD == correct_ans:
    right_opt = "optD"

  # Turn each option into text
  a = get_font(25).render(str(optA), True, BLACK)
  b = get_font(25).render(str(optB), True, BLACK)
  c = get_font(25).render(str(optC), True, BLACK)
  d = get_font(25).render(str(optD), True, BLACK)

  return [a, b, c, d, right_opt]

# First instruction screen
def instruction1():
  run = True
  while run:
    MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
    GAME_MOUSE_POS = pygame.mouse.get_pos()

    # Display instruction screen
    SCREEN.blit(INSTRUCTION1, (0, 0))
    
    # Create buttons
    INSTRUCTIONS_BACK = Button(pygame.image.load("images/back_button.png"), pos = (70, 55), text_input = "", font = get_font(15), base_colour = "White", hovering_colour = "#b51f09")
    INSTRUCTIONS_NEXT = Button(pygame.transform.rotate(pygame.image.load("images/back_button.png"), 180), pos = (680, 475), text_input = "", font = get_font(15), base_colour = "White", hovering_colour = "#b51f09")
    
    # Hovering effect
    if (40<MOUSE_X<75 and 40<MOUSE_Y<70):
      SCREEN.blit(RESIZED_BACK, (-90,-96))
    elif (690<MOUSE_X<705 and 465<MOUSE_Y<490):
      SCREEN.blit(RESIZED_NEXT, (540, 324))

    INSTRUCTIONS_BACK.update(SCREEN)
    INSTRUCTIONS_NEXT.update(SCREEN)

    # Event handling
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if INSTRUCTIONS_BACK.checkInput(GAME_MOUSE_POS):
          return
        elif INSTRUCTIONS_NEXT.checkInput(GAME_MOUSE_POS):
          instruction2()
    pygame.display.update()

# Second instruction screen
def instruction2():
    run = True
    while run:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(INSTRUCTION2, (0, 0))
        
        INSTRUCTIONS_BACK = Button(pygame.image.load("images/back_button.png"), pos = (70, 55), text_input = "", font = get_font(15), base_colour = "White", hovering_colour = "#b51f09")
        
        if (40<MOUSE_X<75 and 40<MOUSE_Y<70):
            SCREEN.blit(RESIZED_BACK, (-90,-96))

        INSTRUCTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkInput(GAME_MOUSE_POS):
                  return

        pygame.display.update()

# Randomize position of fruits
def fruit_coordinates(x1, y1):
  # Initialize variables
  coord_list = [[x1, y1]]
  i = 0
  min_distance = 100

  while i < 4:
    while True:
      # Generate random coordinates
      num1 = round(random.randrange(50, SCREEN_WIDTH - (snake_block + 50)) / 10.0) * 10.0
      num2 = round(random.randrange(50, SCREEN_HEIGHT - (snake_block + 50)) / 10.0) * 10.0
      too_close = False
      for coord in coord_list:
        distance = ((num1 - coord[0]) ** 2 + (num2 - coord[1]) ** 2) ** 0.5
        # Checking if coordinates are too close
        if distance < min_distance:
          too_close = True
          break
      if not too_close:
        break
    coord_list.append([num1, num2])
    i += 1
  return coord_list

# Check if food's been eaten
def fruit_eaten(coord_list, correct_ans):
  # Snake head coordinates
  snakex = coord_list[0][0]
  snakey = coord_list[0][1]

  if correct_ans == "optA":
    answer = 1
  if correct_ans == "optB":
    answer = 2
  if correct_ans == "optC":
    answer = 3
  if correct_ans == "optD":
    answer = 4

  i = 1
  while i < 5:
    # Checking if a fruit has been eaten
    if snakex >= (coord_list[i][0]-25) and snakex <= (coord_list[i][0]+35) and snakey >= (coord_list[i][1]-25) and snakey <= (coord_list[i][1]+45):
      # Checking if the right fruit has been eaten
      if i != answer:
        return 1
      else:
        return 2
    i += 1
  # Checking if the snake has hit the walls
  if snakex == 0 or snakex == 800 or snakey == 0 or snakey == 600:
     return 3
  return 0

# Display ending screen
def end_screen(result):
  while True:
    MOUSE_POS = pygame.mouse.get_pos()

    if result == True:
      pygame.mixer.music.stop()
      WIN.play()
      SCREEN.blit(WIN_SCREEN, (0, 0))
    else:
      pygame.mixer.music.stop()
      LOSS.play()
      SCREEN.blit(LOST_SCREEN, (0, 0))

    RETURN = Button(image = pygame.image.load("images/scroll_button.png"), pos = (400, 500), text_input = "RETURN", font = get_font(18), base_colour = "#b51f09", hovering_colour = "White")
    RETURN.changeColour(MOUSE_POS)
    RETURN.update(SCREEN)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if RETURN.checkInput(MOUSE_POS):
          play_music("sound/SandwichStackMusic.mp3")
          return

    pygame.display.update()

def response(correct, question, answer):
  SCREEN.blit(overlay, (0, 0))
  SCREEN.blit(QBOX, (141, 115))
  # Shadow text
  shadow = get_font(25).render("Press Space To Continue", True, GREEN4)
  # Main text
  main = get_font(25).render("Press Space To Continue", True, WHITE)
        
  SCREEN.blit(shadow, [199, 525])
  SCREEN.blit(main, [197, 523])
  # Shadow text
  if correct == False:
    INCORRECT.play()
    shadow = get_font(50).render("Nice Try!", True, GREEN4)
    # Main text
    main = get_font(50).render("Nice Try!", True, WHITE)
    SCREEN.blit(shadow, [256, 212])
    SCREEN.blit(main, [256, 210])
    q = get_font(25).render(question, True, BLACK)
    # Main text
    ans = get_font(25).render("Correct Answer: " + str(answer), True, BLACK)
    SCREEN.blit(q, [328, 308])
    SCREEN.blit(ans, [245, 387])
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
      end_screen(False)
      return True
  else:
    CORRECT.play()
    shadow = get_font(50).render("Good Job!", True, GREEN4)
    # Main text
    main = get_font(50).render("Good Job!", True, WHITE)
    SCREEN.blit(shadow, [245, 212])
    SCREEN.blit(main, [243, 210])
    q = get_font(25).render(question, True, BLACK)
    # Main text
    ans = get_font(25).render("Correct Answer: " + str(answer), True, BLACK)
    SCREEN.blit(q, [328, 308])
    SCREEN.blit(ans, [245, 387])
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
      end_screen(True)
      return True

def correct(question, answer):
  good = get_font(50).render("Good Job!", True, GREEN4)
  good1 = get_font(50).render("Good Job!", True, WHITE)
  SCREEN.blit(good, [245, 212])
  SCREEN.blit(good1, [243, 210])
  q = get_font(25).render(question, True, BLACK)
  ans = get_font(25).render("Correct Answer: " + str(answer), True, BLACK)
  SCREEN.blit(q, [328, 308])
  SCREEN.blit(ans, [245, 387])

def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

# Main game function
def game(user):
  dontrun = 1
  doneYet = 0
  result = False
  fruit_delay = 4
  run = True 
  pause = True
  snake_pause = True
  level = int(user.get_add()) # get addition level from the user
  select = 0

  # Initialize questions, options, and answer
  currQNA = Question(user).generate_question("+") # gets question and the answer
  currQ = currQNA[0] 
  correct_ans = currQNA[1]
  optionList = options(correct_ans) # creates list of answer options

  # Initialize change in coordinates
  x1_change = 0
  y1_change = 0

  # List of snake body parts coordinates
  snake_list = []
  snake_len = 1

  # Randomize and create coordinates for each orange
  coord_list = fruit_coordinates(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

  # Delay the question screen
  elements_delay_counter = 5

  # Adjust counter according to level, 10 seconds for < 5 and 30 seconds otherwise
  if level < 5: 
    countdown = 600
    timerDown = 10
  else: 
    countdown = 1800
    timerDown = 30

  while run:
    MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
    MOUSE_POS = pygame.mouse.get_pos()
    # Event handling, stop run if quit
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        if BACK.checkInput(MOUSE_POS):
          return
        if event.type == pygame.MOUSEBUTTONDOWN:
            if FRUIT_AB.checkInput(MOUSE_POS):
              select = 1
              pause = False
            elif FRUIT_BB.checkInput(MOUSE_POS):
              select = 2
              pause = False
            elif FRUIT_CB.checkInput(MOUSE_POS):
              select = 3
              pause = False
            elif FRUIT_DB.checkInput(MOUSE_POS):
              select = 4
              pause = False
            

            # Control snake movement when not paused
    if not pause:
      # Refresh the direction changes
      if snake_pause:
        x1_change = 0
        y1_change = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
          snake_pause = False
          x1_change = -snake_block
          y1_change = 0
        elif keys[pygame.K_RIGHT]:
          snake_pause = False
          x1_change = snake_block
          y1_change = 0
        elif keys[pygame.K_UP]:
          snake_pause = False
          y1_change = -snake_block
          x1_change = 0
        elif keys[pygame.K_DOWN]:
          snake_pause = False
          y1_change = snake_block
          x1_change = 0
      else:
        # Check for key presses
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
      if not snake_pause:
        coord_list[0][0] += x1_change
        coord_list[0][1] += y1_change

      snake_list.append([coord_list[0][0], coord_list[0][1]])

      # If snake length exceeds current length, remove the tail
      if len(snake_list) > snake_len:
        del snake_list[0]

    # Draw elements on screen
    SCREEN.blit(BACKGROUND, (0, 0))
    # Blit overlay on top of everything
    if elements_delay_counter > 0:
      elements_delay_counter -= 1
      pause = True
    elif dontrun == 1:
      if countdown > 0 and pause == True and timerDown > 0 and result is False:
        snake_pause = True
        if countdown == 600:
          currQNA = Question(user).generate_question("+")
          currQ = currQNA[0]
          correct_ans = currQNA[1]
          optionList = options(correct_ans)
        countdown -= 1
        SCREEN.blit(overlay, (0, 0))
        SCREEN.blit(QBOX, (141, 115))
        time_left(timerDown)
        # Shadow text
        shadow = get_font(65).render(currQ, True, GOLD3)
        # Main text
        main = get_font(65).render(currQ, True, WHITE)
        if level < 5: 
          SCREEN.blit(shadow, [242, 182])
          SCREEN.blit(main, [240, 180])
        else:
          SCREEN.blit(shadow, [202, 182])
          SCREEN.blit(main, [200, 180])
        # Shadow text
        shadow = get_font(25).render("Select Your Answer", True, GREEN4)
        # Main text
        main = get_font(25).render("Select Your Answer", True, WHITE)
        
        SCREEN.blit(shadow, [235, 525])
        SCREEN.blit(main, [233, 523])

        SCREEN.blit(optionList[0], [315, 290])
        SCREEN.blit(optionList[1], [315, 395])
        SCREEN.blit(optionList[2], [505, 290])
        SCREEN.blit(optionList[3], [505, 395])
        SCREEN.blit(FRUIT_A, [245, 280])
        SCREEN.blit(FRUIT_B, [245, 385])
        SCREEN.blit(FRUIT_C, [438, 280])
        SCREEN.blit(FRUIT_D, [438, 385])
        FRUIT_AB = Button(FRUIT_A, pos = (270, 305), text_input = "", font = get_font(22), base_colour = "White", hovering_colour = "#b51f09")
        FRUIT_AB.update(SCREEN)
        FRUIT_BB = Button(FRUIT_B, pos = (270, 410), text_input = "", font = get_font(22), base_colour = "White", hovering_colour = "#b51f09")
        FRUIT_BB.update(SCREEN)
        FRUIT_CB = Button(FRUIT_C, pos = (463, 305), text_input = "", font = get_font(22), base_colour = "White", hovering_colour = "#b51f09")
        FRUIT_CB.update(SCREEN)
        FRUIT_DB = Button(FRUIT_D, pos = (463, 410), text_input = "", font = get_font(22), base_colour = "White", hovering_colour = "#b51f09")
        FRUIT_DB.update(SCREEN)
        if (235<MOUSE_X<315 and 260<MOUSE_Y<350):
          SCREEN.blit(FRUIT_BORDER, [240, 275])
          SCREEN.blit(FRUIT_A, [245, 280])
        elif (235<MOUSE_X<315 and 375<MOUSE_Y<445):
          SCREEN.blit(FRUIT_BORDER, [240, 380])
          SCREEN.blit(FRUIT_B, [245, 385])
        elif (428<MOUSE_X<498 and 260<MOUSE_Y<350):
          SCREEN.blit(FRUIT_BORDER, [433, 275])
          SCREEN.blit(FRUIT_C, [438, 280])
        elif (428<MOUSE_X<498 and 375<MOUSE_Y<445):
          SCREEN.blit(FRUIT_BORDER, [433, 380])
          SCREEN.blit(FRUIT_D, [438, 385])
        if countdown % 10 == 0 and timerDown > 0:
          timerDown -= 1
        snake_pause = True
      elif result is True:
        SCREEN.blit(overlay, (0, 0))
        SCREEN.blit(QBOX, (141, 115))
        # Shadow text
        shadow = get_font(25).render("Press Space To Continue", True, GREEN4)
        # Main text
        main = get_font(25).render("Press Space To Continue", True, WHITE)
        
        SCREEN.blit(shadow, [199, 525])
        SCREEN.blit(main, [197, 523])
        correct(currQ, correct_ans)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
          result = False
          fruit_delay = 4
          countdown = 600
      else:
        pause = False
      
      if pause == False: 
        if fruit_delay > 0:
           fruit_delay -= 1
        else:
          snake(snake_block, snake_list)
          current_score(snake_len - 1)
          current_level(int(user.get_add()))
          if select == 1:
            SCREEN.blit(FRUIT_BORDER, ((coord_list[1][0]) - 5, (coord_list[1][1]) - 5))
          elif select == 2:
            SCREEN.blit(FRUIT_BORDER, ((coord_list[2][0]) - 5, (coord_list[2][1]) - 5))
          elif select == 3:
            SCREEN.blit(FRUIT_BORDER, ((coord_list[3][0]) - 5, (coord_list[3][1]) - 5))
          elif select == 4:
            SCREEN.blit(FRUIT_BORDER, ((coord_list[4][0]) - 5, (coord_list[4][1]) - 5))
          SCREEN.blit(FRUIT_A, (coord_list[1][0], coord_list[1][1]))
          SCREEN.blit(FRUIT_B, (coord_list[2][0], coord_list[2][1]))
          SCREEN.blit(FRUIT_C, (coord_list[3][0], coord_list[3][1]))
          SCREEN.blit(FRUIT_D, (coord_list[4][0], coord_list[4][1]))
    
    doneYet = fruit_eaten(coord_list, optionList[4])
    BACK = Button(image = "images/back_button.png", pos = (40, 25), text_input = "", font = get_font(22), base_colour = "White", hovering_colour = "#b51f09")
    BACK.update(SCREEN)

    if (10<MOUSE_X<45 and 10<MOUSE_Y<40):
      SCREEN.blit(RESIZED_BACK, (-120,-126))
    if doneYet == 2:
      if (snake_len - 1) == 4:
        result = False
        plss = response(True, currQ, correct_ans)
        elements_delay_counter = 1
        if plss == True:
          new_score = int(user.get_add()) + 1
          user.update_add(str(new_score))
          return
      elif level < 5 and dontrun == 1:
        coord_list = fruit_coordinates(coord_list[0][0], coord_list[0][1])
        snake_len += 1
        elements_delay_counter = 1
        fruit_delay = 4
        countdown = 600
        timerDown = 10
        select = 0
        result = True
      elif dontrun == 1: 
        coord_list = fruit_coordinates(coord_list[0][0], coord_list[0][1])
        snake_len += 1
        elements_delay_counter = 1
        fruit_delay = 4
        countdown = 1800
        timerDown = 30
        select = 0
        result = True
    if doneYet == 1:
      result = False
      dontrun = 0
      plss = response(False, currQ, correct_ans)
      elements_delay_counter = 1
      if plss == True:
        return
    if doneYet == 3:
       end_screen(False)
       return
  
    pygame.display.flip()

    clock.tick(snake_speed)

  pygame.quit()

def snakeSums(username, password):
    play_music("sound/SnakeSumsMusic.mp3")
    user = Player(name=username, password=password)
    user.load_player()
    # Main game loop
    run = True
    while run:
        # display start screen
        SCREEN.blit(START_SCREEN, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()

        START_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 250), text_input = "START GAME", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")
        INSTRUCTION_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 380), text_input = "INSTRUCTIONS", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")
        RETURN_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 510), text_input = "BACK TO MENU", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")

        for button in [START_BUTTON, INSTRUCTION_BUTTON, RETURN_BUTTON]:
            button.changeColour(MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if START_BUTTON.checkInput(MOUSE_POS):
                        game(user)
                        play_music("sound/SnakeSumsMusic.mp3")
                    if INSTRUCTION_BUTTON.checkInput(MOUSE_POS):
                        instruction1()
                        play_music("sound/SnakeSumsMusic.mp3")
                    if RETURN_BUTTON.checkInput(MOUSE_POS):
                        return

        # Update the display
        pygame.display.update()

    # Quit back to the game map
    pygame.mixer.music.stop()
    return
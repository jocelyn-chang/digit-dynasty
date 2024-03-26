import pygame
import glob
import random
from Button import Button

pygame.init()

#Load Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Load Regular Images
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DIGIT DYNASTY')
BACKGROUND = pygame.image.load("images/AE_background.png")
EMPERORMONKEY = pygame.image.load("images/emperor_monkey.png")
EMPERORPIG = pygame.image.load("images/emperor_pig.png")
EMPERORPHOENIX = pygame.image.load("images/emperor_phoenix.png")
EMPERORDRAGON = pygame.image.load("images/emperor_dragon.png")
DEADMONKEY = pygame.image.load("images/dead_monkey.png")
DEADPIG = pygame.image.load("images/dead_pig.png")
DEADPHOENIX = pygame.image.load("images/dead_phoenix.png")
DEADDRAGON = pygame.image.load("images/dead_dragon.png")
DEADPANDASCREEN = pygame.image.load("images/dead_background.png")
QUESTIONSCROLL = pygame.image.load("images/bigScroll.png")
BACKBUTTON = pygame.transform.rotate(pygame.image.load("images/back_button.png"), 180)
RESIZED_NEXT = pygame.transform.rotate(pygame.image.load("images/resized_back.png"), 180)
HAPPYPANDA = pygame.image.load("images/thumbsuppanda.png")

emperorImages = [[EMPERORMONKEY, (460, 40)], [EMPERORPIG, (460, 10)], [EMPERORPHOENIX, (460, 20)], [EMPERORDRAGON, (480, -5)]]
deadEmperorImages = [[DEADMONKEY, (420, 20)], [DEADPIG, (460, 30)], [DEADPHOENIX, (460, 40)], [DEADDRAGON, (410, -5)]]
emperorRotation = 3

#Load Attack Animation Frames
emperorFramePaths = sorted(glob.glob('images/AE_emperor_attack/*.png')) 
emperorAttackFrames = [pygame.transform.scale(pygame.image.load(path), (550, 325)) for path in emperorFramePaths]

addFramePaths = sorted(glob.glob('images/AE_add_attack/*.png')) 
addAttackFrames = [pygame.transform.scale(pygame.image.load(path), (500, 290)) for path in addFramePaths]

subFramePaths = sorted(glob.glob('images/AE_sub_attack/*.png')) 
subAttackFrames = [pygame.transform.scale(pygame.image.load(path), (589, 375)) for path in subFramePaths]

mulFramePaths = sorted(glob.glob('images/AE_mul_attack/*.png'))  
mulAttackFrames = [pygame.transform.scale(pygame.image.load(path), (589, 375)) for path in mulFramePaths]

divFramePaths = sorted(glob.glob('images/AE_div_attack/*.png'))  
divAttackFrames = [pygame.transform.scale(pygame.image.load(path), (589, 375)) for path in divFramePaths]

# Animation settings
frame_rate = 10
frame_index = 0

#Set up Variables
emperorLevel = 0    #get from player class
emperorAttackPower = 100 #change it so that it's based on emperorLevel
playerHealth = 100   #change depending on their level
emperorHealth = 100 #multiply these by emperor level once determined
addAttackPower = 100 #multiply these by strength once determined
subAttackPower = 10
mulAttackPower = 10
divAttackPower = 10

#the health bar is 188 pixels, so need to get num pixels per 1 health
emperorHealthDisplayFactor = 188/emperorHealth
playerHealthDisplayFactor = 188/playerHealth

actionTexts = ["Choose an attack...", "You used ", "You missed your attack", "The emperor uses Blazing Fury!", "The emperor missed its attack!"]
emperorNames = ["Emperor AddWukong", "Emperor DivPorkus", "Emperor SubPyrros", "Emperor MulSmaug"]
emperorTypes = ["Addition", "Subtraction", "Multiplication", "Division"]
playerName = "Player Name"
operandSymbols = ['+', '-', '*', '/']

# define colours
white = (255, 255, 255)
black = (0, 0, 0)

def get_font(font, size):
    if font == "Sawarabi":
        return pygame.font.Font("fonts/SawarabiMincho-Regular.ttf", size)
    elif font == "Shojumaru":
        return pygame.font.Font("fonts/Shojumaru-Regular.ttf", size)

def display_static_text(text, position, colour, max_width):
    font = get_font("Sawarabi", 20)
    rendered_lines = []
    words = text.split()
    line = ''
    
    for word in words:
        test_line = line + word + ' '
        if max_width and font.size(test_line)[0] > max_width:
            rendered_lines.append(line)
            line = word + ' '
        else:
            line = test_line
    
    if line:
        rendered_lines.append(line)
    
    y = position[1]
    for rendered_line in rendered_lines:
        text_surface = font.render(rendered_line, True, colour)
        SCREEN.blit(text_surface, (position[0], y))
        y += text_surface.get_height()  # Move to the next line
    
    return rendered_lines
   
def display_basic_screen(emperorImage, emperorPos, emperorName):
    #Draw the background image onto the screen
    SCREEN.blit(BACKGROUND, (0, 0))
    SCREEN.blit(emperorImage, emperorPos)

    # Render names as text and blit onto screen
    emperorNameText = get_font("Sawarabi", 20).render(emperorNames[emperorRotation], True, (0, 0, 0)) 
    playerNameText = get_font("Sawarabi", 20).render(playerName, True, (0, 0, 0)) 
    SCREEN.blit(emperorNameText, (50, 62))
    SCREEN.blit(playerNameText, (750 - playerNameText.get_width(), 385)) #position references top right corner of text box

    #Display health damge overlay
    pygame.draw.rect(SCREEN, (239, 39, 39), pygame.Rect(130, 102, emperorHealthDisplayFactor*emperorHealth, 20))
    pygame.draw.rect(SCREEN, (239, 39, 39), pygame.Rect(543, 430, playerHealthDisplayFactor*playerHealth, 20))

def attack_emperor(attackType, attackFrames, position, attacker, attackTypeText):
  global emperorHealth
  animate_attack(attackFrames, position, attacker, attackTypeText)
  emperorHealth = emperorHealth - attackType

def attack_player(attackFrames, position, attacker, attackTypeText, attackedEmperor):
  global playerHealth
  random_number = random.uniform(1, 2)

  #if player attached emperor, 50% change emperor will attack back
  if (attackedEmperor):
    random_number = random.uniform(1, 2)
    if random_number <= 1.5:
      animate_attack(attackFrames, position, attacker, attackTypeText)
      playerHealth = playerHealth - emperorAttackPower
    else:
      display_basic_screen(emperorImages[emperorRotation][0], emperorImages[emperorRotation][1], emperorNames[emperorRotation])
      display_static_text(actionTexts[4], (40, 510), white, 300)
      pygame.display.update()
      pygame.time.delay(3000)

  #If player didn't attack emperor, emperor will 100% attack player
  else:
    display_basic_screen(emperorImages[emperorRotation][0], emperorImages[emperorRotation][1], emperorNames[emperorRotation])
    display_static_text(actionTexts[2], (40, 510), white, 300)
    pygame.display.update()
    pygame.time.delay(3000)
    
    animate_attack(attackFrames, position, attacker, attackTypeText)
    playerHealth = playerHealth - emperorAttackPower

def check_answer(answer, correct_answer):
    # Display question screen
    SCREEN.blit(QUESTIONSCROLL, (25, 100))
    title = get_font("Shojumaru", 25).render("Answer the Following Question:", True, white)
    titleRect = title.get_rect()
    titleRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
    SCREEN.blit(title, titleRect)

    if int(answer) == int(correct_answer):
        # Display user's input text
        correct = get_font("Shojumaru", 20).render('CORRECT', True, white)
        inputRect = correct.get_rect()
        inputRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Adjust position as needed
        SCREEN.blit(correct, inputRect)
        correct = True

    else:
        # Display user's input text
        incorrect = get_font("Shojumaru", 20).render(f"Incorrect, Correct answer = {correct_answer}  your answer = {answer}", True, white)
        inputRect = incorrect.get_rect()
        inputRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Adjust position as needed
        SCREEN.blit(incorrect, inputRect)
        correct = False

    # Update the display
    pygame.display.update()
    pygame.time.delay(3000)
    
    return correct

def generate_question_answer():
   while True:
        num_operands = random.randint(2, 4)  # Random number of operands
        operands = random.choices(operandSymbols, k=num_operands)  # Randomly select operands
        numbers = [random.randint(1, 10) for _ in range(num_operands + 1)]  # Generate random numbers

        # Construct the expression string
        expression = ' '.join([f'{num} {op}' for num, op in zip(numbers[:-1], operands)]) + f' {numbers[-1]}'

        try:
            # Evaluate the expression
            result = eval(expression)

            # Check if the result is a whole number
            if isinstance(result, int) and result == round(result):
                return [expression, result]  # Return the expression and its result as a list
        except Exception:
            pass  # Ignore any errors during evaluation and continue generating a new question
        
def question():
    answer = ""
    questionAndAnswer = generate_question_answer()
    question_text = questionAndAnswer[0]
    correct_answer = questionAndAnswer[1]
    run = True

    while run:
    
        # Display question screen
        SCREEN.blit(QUESTIONSCROLL, (25, 100))
        title = get_font("Shojumaru", 20).render("Answer the Following Question:", True, white)
        titleRect = title.get_rect()
        titleRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
        SCREEN.blit(title, titleRect)

        title = get_font("Shojumaru", 40).render(question_text, True, white)
        titleRect = title.get_rect()
        titleRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(title, titleRect)

        # Display user's input text
        input_text = get_font("Shojumaru", 40).render(answer, True, white)
        inputRect = input_text.get_rect()
        inputRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)  # Adjust position as needed
        SCREEN.blit(input_text, inputRect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Check if Enter key is pressed to submit answer
                    if check_answer(answer, correct_answer):
                       return True
                    else:
                       return False
                elif event.key == pygame.K_BACKSPACE:  # Check if Backspace key is pressed to delete characters
                    answer = answer[:-1]
                else:
                    # Check if a printable character is pressed and append it to the answer
                    if event.unicode.isprintable():
                        answer += event.unicode

        # Update the display
        pygame.display.update()

def animate_attack(attackFrames, position, attacker, attackTypeText):
  global frame_index
   
  clock = pygame.time.Clock()
  frame_delay = 10

  for _ in range(len(attackFrames)):
    # Draw the background image onto the screen
    display_basic_screen(emperorImages[emperorRotation][0], emperorImages[emperorRotation][1], emperorNames[emperorRotation])
    display_static_text(actionTexts[attacker] + attackTypeText, (40, 510), white, 300)

    # Blit current frame onto the screen
    SCREEN.blit(attackFrames[frame_index], position)  # Adjust the position as needed

    # Increment frame index and loop back to the beginning if necessary
    frame_index = (frame_index + 1) % len(attackFrames)

    # Update the display
    pygame.display.update()

    # Delay for specified time
    clock.tick(frame_delay)

def end_game_screen(playerWon):
    run = True
    NEXT_BUTTON = Button(BACKBUTTON, pos = (650, 300), text_input = "", font = get_font("Sawarabi",24), base_colour = "White", hovering_colour = "#b51f09")

    if (playerWon):
       display_basic_screen(deadEmperorImages[emperorRotation][0], deadEmperorImages[emperorRotation][1], emperorNames[emperorRotation])
       display_static_text("Congratulations! The emperor has been defeated.", (40, 510), white, 300)
    else:
       SCREEN.blit(DEADPANDASCREEN, (-1, 301))
       display_static_text("You have been defeated by the emperor.", (40, 510), white, 300)

    pygame.display.update()
    pygame.time.delay(2000)

    while run:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()
        # Display question screen
        SCREEN.blit(QUESTIONSCROLL, (25, 100))

        if emperorHealth < 0:
            title_lines = ["Congratulations you imroved"]
        else:
            title_lines = ["Keep practicing!"]

        for i, line in enumerate(title_lines):
            title_text = get_font("Sawarabi",24).render(line, True, white)
            inputRect = title_text.get_rect()
            inputRect.center = (SCREEN_WIDTH // 2, 225 + i * get_font("Sawarabi",25).get_height())  # Adjust position for each line
            SCREEN.blit(title_text, inputRect)
        
        SCREEN.blit(HAPPYPANDA, (250, 330))

        if (660<MOUSE_X<685 and 390<MOUSE_Y<415):
            SCREEN.blit(RESIZED_NEXT, (510, 249))
        
        NEXT_BUTTON.update(SCREEN)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEXT_BUTTON.checkInput(GAME_MOUSE_POS):
                    run = False
        # Update the display
        pygame.display.update()

def start_game():
  global emperorHealth, emperorHealthDisplayFactor, playerHealthDisplayFactor, frame_index, attackedEmperor

  while True:
    #Get Mouse Pos
    MOUSE_POS = pygame.mouse.get_pos()  
  
    attackedEmperor = False 

    display_basic_screen(emperorImages[emperorRotation][0], emperorImages[emperorRotation][1], emperorNames[emperorRotation])
    display_static_text(actionTexts[0], (40, 510), white, 300)

    #if player died
    if (playerHealth <= 0):
        end_game_screen(False)
        return

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
            if question():
              attack_emperor(addAttackPower, addAttackFrames, (365, 25), 1, "Addition Anarchy!")
              attackedEmperor = True
              if (emperorHealth <= 0):
                end_game_screen(True)
                return
            attack_player(emperorAttackFrames, (-45, 170), 3, "", attackedEmperor)

        if SUB_BUTTON.checkInput(MOUSE_POS):
            if question():
              attack_emperor(subAttackPower, subAttackFrames, (320, -30), 1, "Subtraction Storm!")
              attackedEmperor = True
              if (emperorHealth <= 0):
                end_game_screen(True)
                return

            attack_player(emperorAttackFrames, (-45, 170), 3, "", attackedEmperor)

        if DIV_BUTTON.checkInput(MOUSE_POS):
            if question():
              attack_emperor(divAttackPower, divAttackFrames, (290, 25), 1, "Division Disaster!")
              attackedEmperor = True
              if (emperorHealth <= 0):
                end_game_screen(True)
                return

            attack_player(emperorAttackFrames, (-45, 170), 3, "", attackedEmperor)

        if MUL_BUTTON.checkInput(MOUSE_POS):
            if question():
              attack_emperor(mulAttackPower, mulAttackFrames, (295, -80), 1, "Multiplication Magnetism!")
              attackedEmperor = True
              if (emperorHealth <= 0):
                end_game_screen(True)
                return

            attack_player(emperorAttackFrames, (-45, 170), 3, "", attackedEmperor)
    
    mouse_x, mouse_y = MOUSE_POS
    font = pygame.font.Font(None, 36)
    text = font.render(f"Mouse Position: ({mouse_x}, {mouse_y})", True, (0,0,0))
    SCREEN.blit(text,(10,10))

    # Update the display
    pygame.display.flip()

start_game()
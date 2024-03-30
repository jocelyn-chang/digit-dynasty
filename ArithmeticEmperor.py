import pygame
import glob
import random
from Button import Button
from Player import Player
from question import Question

pygame.init()

pygame.display.set_caption('DIGIT DYNASTY')

#Load Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Load Regular Images
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = pygame.image.load("images/AE_background.png")
START_SCREEN = pygame.image.load("images/AE_title_screen.png")
BEDMAS_INSTRUCTIONS = pygame.image.load("images/bedmas_instruction.png")
AE_INSTRUCTIONS = pygame.image.load("images/AE_instructions.png")
BACK = pygame.image.load("images/back_button.png")
RESIZED_BACK = pygame.image.load("images/resized_back.png")
RESIZED_NEXT = pygame.transform.rotate(pygame.image.load("images/resized_back.png"), 180)
WIN_SCREEN = pygame.image.load("images/AE_win_background.png")
LOSE_SCREEN = pygame.image.load("images/AE_lose_background.png")
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

emperorImages = [[EMPERORMONKEY, (460, 40)], [EMPERORPHOENIX, (460, 20)], [EMPERORDRAGON, (480, -5)], [EMPERORPIG, (460, 10)]]
deadEmperorImages = [[DEADMONKEY, (420, 20)], [DEADPHOENIX, (460, 40)], [DEADDRAGON, (410, -5)], [DEADPIG, (460, 30)]]

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


actionTexts = ["Choose an attack...", "You used ", "You missed your attack", "The emperor uses Blazing Fury!", "The emperor missed its attack!"]
emperorNames = ["Emperor AddWukong", "Emperor SubPyrros", "Emperor MulSmaug", "Emperor DivPorkus"]
emperorTypes = ["Addition", "Subtraction", "Multiplication", "Division"]
operandSymbols = ['+', '-', '*', '/']

# define colours
white = (255, 255, 255)
black = (0, 0, 0)

# Intructions screen
def instruction1():
    """
    Display the first set of instructions for the game.

    This function displays the instructions related to the BEDMAS (Brackets, Exponents, Division, Multiplication, Addition, Subtraction) concept of the game.
    Users can navigate to the next set of instructions by clicking on the appropriate button.

    Args:
        None

    Returns:
        None
    """
    while True:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BEDMAS_INSTRUCTIONS, (0, 0))
        
        INSTRUCTIONS_BACK = Button(pygame.image.load("images/back_button.png"), pos = (70, 55), text_input = "", font = get_font("Shojumaru", 15), base_colour = "White", hovering_colour = "#b51f09")
        INSTRUCTIONS_NEXT = Button(pygame.transform.rotate(pygame.image.load("images/back_button.png"), 180), pos = (680, 475), text_input = "", font = get_font("Shojumaru", 15), base_colour = "White", hovering_colour = "#b51f09")
        INSTRUCTIONS_BACK.update(SCREEN)
        INSTRUCTIONS_NEXT.update(SCREEN)

        if (40<MOUSE_X<75 and 40<MOUSE_Y<70):
            SCREEN.blit(RESIZED_BACK, (-90,-96))
        if (690<MOUSE_X<705 and 465<MOUSE_Y<490):
            SCREEN.blit(RESIZED_NEXT, (540, 324))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkInput(GAME_MOUSE_POS):
                    return
                if INSTRUCTIONS_NEXT.checkInput(GAME_MOUSE_POS):
                    instruction2()

        pygame.display.update()

def instruction2():
    """
    Display the second set of instructions for the game.

    This function displays the instructions related to the Arithmetic Emperor (AE) game mechanics.
    Users can navigate back to the previous screen by clicking on the back button.

    Args:
        None

    Returns:
        None
    """
    while True:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(AE_INSTRUCTIONS, (0, 0))
        
        INSTRUCTIONS_BACK = Button(pygame.image.load("images/back_button.png"), pos = (70, 55), text_input = "", font = get_font("Shojumaru", 15), base_colour = "White", hovering_colour = "#b51f09")
        INSTRUCTIONS_BACK.update(SCREEN)

        if (40 < MOUSE_X < 75 and 40 < MOUSE_Y < 70):
            SCREEN.blit(RESIZED_BACK, (-90,-96))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkInput(GAME_MOUSE_POS):
                    return

        pygame.display.update()

def arithmetic_emperor(username, password):
    """
    Start the main menu game loop for the Arithmetic Emperor game.

    This function initializes the game and allows players to interact with the main menu to start the game, view instructions, or return to the map screen.

    Args:
        username (str): The username of the player.
        password (str): The password of the player.

    Returns:
        None
    """

    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(START_SCREEN, (0,0))

        START_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 250), text_input = "START GAME", font = get_font("Shojumaru", 22), base_colour = "#b51f09", hovering_colour = "White")
        INSTRUCTION_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 380), text_input = "INSTRUCTIONS", font = get_font("Shojumaru", 22), base_colour = "#b51f09", hovering_colour = "White")
        RETURN_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 510), text_input = "BACK TO MAP", font = get_font("Shojumaru", 22), base_colour = "#b51f09", hovering_colour = "White")

        for button in [START_BUTTON, INSTRUCTION_BUTTON, RETURN_BUTTON] :
            button.changeColour(MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.checkInput(MOUSE_POS):
                      start_game(username, password)
                if INSTRUCTION_BUTTON.checkInput(MOUSE_POS):
                     instruction1()
                if RETURN_BUTTON.checkInput(MOUSE_POS):
                     return

        # Update the display
        pygame.display.update()

def get_font(font, size):
    """
    Retrieve the font object based on the specified font name and size.

    This function returns the appropriate font object based on the specified font name and size.

    Args:
        font (str): The name of the font.
        size (int): The size of the font.

    Returns:
        pygame.font.Font: The font object.
    """
    if font == "Sawarabi":
        return pygame.font.Font("fonts/SawarabiMincho-Regular.ttf", size)
    elif font == "Shojumaru":
        return pygame.font.Font("fonts/Shojumaru-Regular.ttf", size)

def display_static_text(text, position, colour, max_width):
    """
    Display static text on the screen with word wrapping.

    This function renders and displays static text on the screen with word wrapping if the text exceeds the specified maximum width.

    Args:
        text (str): The text to be displayed.
        position (tuple): The position (x, y) where the text should be displayed.
        colour (tuple): The colour of the text in RGB format.
        max_width (int): The maximum width allowed for the text before word wrapping.

    Returns:
        list: A list of rendered lines of text.
    """
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
    """
    Display the basic game screen with emperor and player information.

    This function renders and displays the basic game screen with the emperor's image, position, and name, as well as the player's name and health bars.

    Args:
        emperorImage (pygame.Surface): The image of the emperor.
        emperorPos (tuple): The position (x, y) of the emperor.
        emperorName (str): The name of the emperor.

    Returns:
        None
    """

    global emperorHealthDisplayFactor, playerHealthDisplayFactor, emperorHealth, playerHealth, emperorRotation, playerName

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

def attack_emperor(playerAttack, attackFrames, position, attacker, attackTypeText):
    """
    Perform an attack on the emperor.

    This function calculates the damage inflicted on the emperor by the player's attack and updates the emperor's health accordingly.

    Args:
        playerAttack (int): The power of the player's attack.
        attackFrames (list): The frames of the attack animation.
        position (tuple): The position (x, y) where the attack animation should be displayed.
        attacker (int): The identifier of the attacker (player or emperor).
        attackTypeText (str): The text describing the type of attack.

    Returns:
        int: The updated health of the emperor.
    """

    global emperorHealth, playerHealth, attackType, emperorRotation

    #if player attack type is super effective against emperor type
    if (attackType == emperorRotation - 1 or attackType - 3 == emperorRotation ):
        animate_attack(attackFrames, position, attacker, attackTypeText + " It's super effective!")
        emperorHealth = emperorHealth - (1.5 * playerAttack)
        
    else:
        animate_attack(attackFrames, position, attacker, attackTypeText)
        emperorHealth = emperorHealth - playerAttack

    return emperorHealth

def attack_player(emperorAttackPower, attackFrames, position, attacker, attackTypeText, attackedEmperor):
    """
    Perform an attack on the player.

    This function calculates the damage inflicted on the player by the emperor's attack and updates the player's health accordingly.

    Args:
        emperorAttackPower (int): The power of the emperor's attack.
        attackFrames (list): The frames of the attack animation.
        position (tuple): The position (x, y) where the attack animation should be displayed.
        attacker (int): The identifier of the attacker (player or emperor).
        attackTypeText (str): The text describing the type of attack.
        attackedEmperor (bool): A flag indicating whether the emperor was attacked.

    Returns:
        int: The updated health of the player.
    """
    global emperorHealth, playerHealth, emperorRotation

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
        
    return playerHealth

def check_answer(answer, correct_answer):
    """
    Check the correctness of the player's answer to a question.

    This function compares the player's answer to the correct answer and displays feedback accordingly.

    Args:
        answer (str): The player's answer.
        correct_answer (str): The correct answer.

    Returns:
        bool: True if the answer is correct, False otherwise.
    """

    # Display question screen
    SCREEN.blit(QUESTIONSCROLL, (25, 100))
    title = get_font("Shojumaru", 25).render("Answer the Following Question:", True, white)
    titleRect = title.get_rect()
    titleRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
    SCREEN.blit(title, titleRect)

    correct = False

    if int(answer) == int(correct_answer):
        # Display user's input text
        correct = get_font("Shojumaru", 20).render('CORRECT', True, white)
        inputRect = correct.get_rect()
        inputRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Adjust position as needed
        SCREEN.blit(correct, inputRect)
        correct = True

    else:
        incorrect_lines = ["Incorrect", f"Correct Answer = {int(correct_answer)}", f"Your Answer = {answer}"]
        line_height = get_font("Shojumaru", 20).get_height()
        for i, line in enumerate(incorrect_lines):
            incorrect_text = get_font("Shojumaru", 20).render(line, True, white)
            inputRect = incorrect_text.get_rect()
            inputRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * line_height)  # Adjust position for each line
            SCREEN.blit(incorrect_text, inputRect)

    # Update the display
    pygame.display.update()
    pygame.time.delay(3000)
    
    return correct

def generate_question_answer():
    """
    Generate a random arithmetic question and its answer.

    This function generates a random arithmetic question involving addition, subtraction, multiplication, or division, along with its correct answer.

    Args:
        None

    Returns:
        list: A list containing the arithmetic question and its correct answer.
    """
    equationFound = False
    while True:
        num_operands = random.randint(2, 4)  # Random number of operands
        operands = random.choices(operandSymbols, k=num_operands)  # Randomly select operands
        numbers = [random.randint(1, 10) for _ in range(num_operands + 1)]  # Generate random numbers
        
        for i in range (len(operands)):
            if operands[i] == '/':
                if numbers[i]%numbers[i + 1] == 0:
                    equationFound = True
                else:
                    equationFound = False
                    break

        if equationFound:
            break

    expression = ' '.join([f'{num} {op}' for num, op in zip(numbers[:-1], operands)]) + f' {numbers[-1]}'
    result = eval(expression)
    return [expression, result]

def question():
    """
    Display a question and prompt the player for an answer.

    This function generates a random arithmetic question, displays it on the screen, and prompts the player to input an answer.

    Args:
        None

    Returns:
        bool: True if the player's answer is correct, False otherwise.
    """
     
    global player
    answer = ""
    current_question = Question(player)
    questionAndAnswer = current_question.generate_question("Bedmas")
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
                    if event.unicode.isdigit() or (event.unicode == '-' and len(answer) == 0):
                        answer += event.unicode

        # Update the display
        pygame.display.update()

def animate_attack(attackFrames, position, attacker, attackTypeText):
    """
    Animate an attack on the screen.

    This function animates an attack on the screen by displaying a sequence of frames from the attack animation.

    Args:
        attackFrames (list): The frames of the attack animation.
        position (tuple): The position (x, y) where the attack animation should be displayed.
        attacker (int): The identifier of the attacker (player or emperor).
        attackTypeText (str): The text describing the type of attack.

    Returns:
        None
    """

    global frame_index, emperorHealth, playerHealth, emperorRotation
    
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

def win_screen(score):
    """
    Display the win screen.

    This function displays the win screen with a congratulatory message and the player's new level.

    Args:
        score (int): The player's new level.

    Returns:
        None
    """
    global emperorHealth, playerHealth
    display_basic_screen(deadEmperorImages[emperorRotation][0], deadEmperorImages[emperorRotation][1], emperorNames[emperorRotation])
    display_static_text("Congratulations! The emperor has been defeated.", (40, 510), white, 300)
    pygame.display.update()
    pygame.time.delay(3000)

    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(WIN_SCREEN, (0, 0))
        score_font = get_font("Shojumaru", 20)
        score_surface = score_font.render(f"Your Player Level is Now: {score}", True, "White")
        SCREEN.blit(score_surface, (215, 420))
            
        RETURN = Button(image = pygame.image.load("images/scroll_button.png"), pos = (SCREEN_WIDTH / 2, 520), text_input = "TITLE SCREEN", font = get_font("Shojumaru", 18), base_colour = "#b51f09", hovering_colour = "White")
        RETURN.changeColour(MOUSE_POS)
        RETURN.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN.checkInput(MOUSE_POS):
                    return

        pygame.display.update()

def lose_screen(username, password):
    """
    Display the lose screen.

    This function displays the lose screen with a message indicating defeat and the player's current level.

    Args:
        username (str): The username of the player.
        password (str): The password of the player.

    Returns:
        None
    """
    global emperorHealth, playerHealth
    SCREEN.blit(DEADPANDASCREEN, (-1, 301))
    display_static_text("You have been defeated by the emperor.", (40, 510), white, 300)
    pygame.display.update()
    pygame.time.delay(3000)

    player = Player(username, password)
    player.load_player()
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(LOSE_SCREEN, (0, 0))
        level_font = get_font("Shojumaru", 20)
        level_surface = level_font.render(f"Current level: {player.get_bosses()}", True, "White")
        SCREEN.blit(level_surface, (130, 340))

        RETURN = Button(image = pygame.image.load("images/scroll_button.png"), pos = (SCREEN_WIDTH / 2, 440), text_input = "TITLE SCREEN", font = get_font("Shojumaru", 18), base_colour = "#b51f09", hovering_colour = "White")
        RETURN.changeColour(MOUSE_POS)
        RETURN.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN.checkInput(MOUSE_POS):
                    return

        pygame.display.update()

def start_game(username, password):
    """
    Start the main game loop.

    This function initializes the game and allows players to interact with the main game screen to perform attacks and answer questions.

    Args:
        username (str): The username of the player.
        password (str): The password of the player.

    Returns:
        None
    """
    global frame_index, emperorHealthDisplayFactor, playerHealthDisplayFactor, emperorHealth, playerHealth, emperorLevel, emperorRotation, playerName, attackType, player
    player = Player(username, password)
    player.load_player()

    #Set up Emperor Variables
    emperorLevel = int(player.get_bosses())
    emperorAttackPower = 20 + 2 * emperorLevel
    emperorHealth = 100 + 5 * emperorLevel
    emperorRotation = emperorLevel % 4
    
    #Set up Player Variables (each attack has base power of 20, and get stronger based on operand score)
    playerHealth = 100
    playerName = player.get_name()
    addAttackPower = 20 + int(player.get_add())
    subAttackPower = 20 + int(player.get_sub())
    mulAttackPower = 20 + int(player.get_mul())
    divAttackPower = 20 + int(player.get_div())

    #the health bar is 188 pixels, so need to get num pixels per 1 health
    emperorHealthDisplayFactor = 188/emperorHealth
    playerHealthDisplayFactor = 188/playerHealth

    attackType = 0
    
    while True:
        #Get Mouse Pos
        MOUSE_POS = pygame.mouse.get_pos() 
        MOUSE_X, MOUSE_Y = MOUSE_POS 
    
        attackedEmperor = False 

        display_basic_screen(emperorImages[emperorRotation][0], emperorImages[emperorRotation][1], emperorNames[emperorRotation])
        display_static_text(actionTexts[0], (40, 510), white, 300)

        if (10<MOUSE_X<45 and 10<MOUSE_Y<40):
            SCREEN.blit(RESIZED_BACK, (-120,-126))

        #if player died
        if (playerHealth <= 0):
            lose_screen(username, password)
            return

        #Attack Buttons
        ADD_BUTTON = Button(image = None, pos = (500, 520), text_input = "Addition", font = get_font("Sawarabi",24), base_colour = "black", hovering_colour = "#d73c37")
        DIV_BUTTON = Button(image = None, pos = (500, 560), text_input = "Division", font = get_font("Sawarabi",24), base_colour = "black", hovering_colour = "#d73c37")
        SUB_BUTTON = Button(image = None, pos = (690, 520), text_input = "Subtraction", font = get_font("Sawarabi",24), base_colour = "black", hovering_colour = "#d73c37")
        MUL_BUTTON = Button(image = None, pos = (700, 560), text_input = "Multiplication", font = get_font("Sawarabi",24), base_colour = "black", hovering_colour = "#d73c37")

        #Back Button
        BACK = Button(image = "images/back_button.png", pos = (40, 25), text_input = "", font = get_font("Shojumaru", 22), base_colour = "White", hovering_colour = "#b51f09")

        for button in [ADD_BUTTON, DIV_BUTTON, SUB_BUTTON, MUL_BUTTON, BACK]:
            button.changeColour(MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ADD_BUTTON.checkInput(MOUSE_POS):
                    if question():
                        attackType = 0
                        emperorHealth = attack_emperor(addAttackPower, addAttackFrames, (365, 25), 1, "Addition Anarchy!")
                        attackedEmperor = True
                    if (emperorHealth <= 0):
                        new_score = int(player.get_bosses()) + 1
                        player.update_bosses(str(new_score))
                        win_screen(new_score)
                        return
                    playerHealth = attack_player(emperorAttackPower, emperorAttackFrames, (-45, 170), 3, "", attackedEmperor)

                if SUB_BUTTON.checkInput(MOUSE_POS):
                    if question():
                        attackType = 1
                        emperorHealth = attack_emperor(subAttackPower, subAttackFrames, (320, -30), 1, "Subtraction Storm!")
                        attackedEmperor = True
                    if (emperorHealth <= 0):
                        new_score = int(player.get_bosses()) + 1
                        player.update_bosses(str(new_score))
                        win_screen(new_score)
                        return

                    playerHealth = attack_player( emperorAttackPower, emperorAttackFrames, (-45, 170), 3, "", attackedEmperor)
                
                if MUL_BUTTON.checkInput(MOUSE_POS):
                    if question():
                        attackType = 2
                        emperorHealth = attack_emperor(mulAttackPower, mulAttackFrames, (295, -80), 1, "Multiplication Magnetism!")
                        attackedEmperor = True
                    if (emperorHealth <= 0):
                        new_score = int(player.get_bosses()) + 1
                        player.update_bosses(str(new_score))
                        win_screen(new_score)
                        return

                    playerHealth = attack_player(emperorAttackPower, emperorAttackFrames, (-45, 170), 3, "", attackedEmperor)

                if DIV_BUTTON.checkInput(MOUSE_POS):
                    if question():
                        attackType = 3
                        emperorHealth = attack_emperor(divAttackPower, divAttackFrames, (290, 25), 1, "Division Disaster!")
                        attackedEmperor = True
                    if (emperorHealth <= 0):
                        new_score = int(player.get_bosses()) + 1
                        player.update_bosses(str(new_score))
                        win_screen(new_score)
                        return

                    playerHealth = attack_player(emperorAttackPower, emperorAttackFrames, (-45, 170), 3, "", attackedEmperor)
                
                if BACK.checkInput(MOUSE_POS):
                    return
                
        # Update the display
        pygame.display.flip()

#arithmetic_emperor("test", "test")
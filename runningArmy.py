import pygame, sys, random, math
from Button import Button
from question import Question
from Player import Player

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DIGIT DYNASTY')

# Load the tall image
INSTRUCTION1 = pygame.image.load("images/Multiplication_instruction.png")
INSTRUCTION2 = pygame.image.load("images/Instructions for running army.png")
BACK = pygame.image.load("images/back_button.png")
RESIZED_BACK = pygame.image.load("images/resized_back.png")
RESIZED_NEXT = pygame.transform.rotate(pygame.image.load("images/resized_back.png"), 180)
WIN_SCREEN = pygame.image.load("images/win_screen_mult.png")
LOSE_SCREEN = pygame.image.load("images/lose_screen_mult.png")
START_SCREEN = pygame.image.load("images/Running Army Start Screen.png")
IMAGE = pygame.image.load("images/running_army_bg.png")
PANDA = pygame.transform.scale(pygame.image.load("images/panda1.png"), (50, 50))
DEAD_PANDA = pygame.transform.scale(pygame.image.load("images/panda4.png"), (60, 60))
GATE = pygame.transform.scale(pygame.image.load("images/gates.png"), (400, 125))
ARROW = pygame.transform.scale(pygame.image.load("images/parrow.png"), (50, 50))
QUESTION_SCROLL = pygame.image.load("images/bigScroll.png")

# Load Sounds
LOSS = pygame.mixer.Sound("sound/LossSound.mp3")
WIN = pygame.mixer.Sound("sound/LevelComplete.mp3")
CORRECT = pygame.mixer.Sound("sound/Correct.mp3")
# INCORRECT = pygame.mixer.Sound("sound/Hover.mp3")

image_height = IMAGE.get_height()
image_width = IMAGE.get_width()

# define colours
white = (255, 255, 255)

# movement for panda/arrow
arrow_rect = ARROW.get_rect()
panda_rect = PANDA.get_rect()


# Calculate the new height of the image to maintain the aspect ratio
scaled_height = int(image_height * (SCREEN_WIDTH / image_width))
# Scale the image to fill the width of the screen while maintaining the aspect ratio
scaled_image = pygame.transform.scale(IMAGE, (SCREEN_WIDTH, scaled_height))

def get_font(size):
    """
    Returns a pygame font object with the specified size.

    Args:
        size (int): The size of the font.

    Returns:
        pygame.font.Font: A font object with the specified size.
    """
    return pygame.font.Font("fonts/Shojumaru-Regular.ttf", size)

def instruction1():
    """
    Displays the first instruction screen for how to use multiplication.
    Allows the user to navigate to the next instruction screen or go back.
    """
    run = True
    while run:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(INSTRUCTION1, (0, 0))
        
        INSTRUCTIONS_BACK = Button(pygame.image.load("images/back_button.png"), pos = (70, 55), text_input = "", font = get_font(15), base_colour = "White", hovering_colour = "#b51f09")
        INSTRUCTIONS_NEXT = Button(pygame.transform.rotate(pygame.image.load("images/back_button.png"), 180), pos = (680, 475), text_input = "", font = get_font(15), base_colour = "White", hovering_colour = "#b51f09")
        
        if (40<MOUSE_X<75 and 40<MOUSE_Y<70):
            screen.blit(RESIZED_BACK, (-90,-96))
        if (690<MOUSE_X<705 and 465<MOUSE_Y<490):
            screen.blit(RESIZED_NEXT, (540, 324))

        INSTRUCTIONS_BACK.update(screen)
        INSTRUCTIONS_NEXT.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkInput(GAME_MOUSE_POS):
                    run = False
                if INSTRUCTIONS_NEXT.checkInput(GAME_MOUSE_POS):
                    instruction2()
                    run = False

        pygame.display.update()

def instruction2():
    """
    Displays the second instruction screen for how to play the game.
    Allows the user to navigate back to the first instruction screen.
    """
    run = True
    while run:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(INSTRUCTION2, (0, 0))
        
        INSTRUCTIONS_BACK = Button(pygame.image.load("images/back_button.png"), pos = (70, 55), text_input = "", font = get_font(15), base_colour = "White", hovering_colour = "#b51f09")
        INSTRUCTIONS_BACK.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkInput(GAME_MOUSE_POS):
                    run = False

        pygame.display.update()

def check_answer(answer, correct_answer):
    """
    Checks if the user's answer is correct and displays the result on the screen.

    Args:
        answer (str): The user's answer to the question.
        correct_answer (str): The correct answer to the question.

    Returns:
        bool: True if the user's answer is correct, False otherwise.
    """
    screen.blit(QUESTION_SCROLL, (25, 100))
    title = get_font(25).render("Answer the Following Question:", True, white)
    titleRect = title.get_rect()
    titleRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
    screen.blit(title, titleRect)
    
    correct = False
    
    if int(answer) == int(correct_answer):
        #play sound
        CORRECT.play()

        # Display user's input text
        correct = get_font(20).render('CORRECT', True, white)
        inputRect = correct.get_rect()
        inputRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Adjust position as needed
        screen.blit(correct, inputRect)
        correct = True

    else:
        # Play sound
        # INCORRECT.play()

        incorrect_lines = ["Incorrect", f"Correct Answer = {correct_answer}", f"Your Answer = {answer}"]
        line_height = get_font(20).get_height()
        for i, line in enumerate(incorrect_lines):
            incorrect_text = get_font(20).render(line, True, white)
            inputRect = incorrect_text.get_rect()
            inputRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * line_height)  # Adjust position for each line
            screen.blit(incorrect_text, inputRect)


    # Update the display
    pygame.display.update()
    pygame.time.delay(3000)

    return correct


def question(numpandas, multiplier):
    """
    Displays a multiplication question and checks if the user's answer is correct.

    Args:
        numpandas (int): The number of pandas.
        multiplier (int): The multiplier for the question.

    Returns:
        bool: True if the user's answer is correct, False otherwise.
    """
    answer = ""
    correct_answer = numpandas*multiplier
    run = True

    while run:
        
        # Display question screen
        screen.blit(QUESTION_SCROLL, (25, 100))
        title = get_font(20).render("Answer the Following Question:", True, white)
        titleRect = title.get_rect()
        titleRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
        screen.blit(title, titleRect)

        title = get_font(40).render(f"{numpandas} X {multiplier}", True, white)
        titleRect = title.get_rect()
        titleRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        screen.blit(title, titleRect)

        # Display user's input text
        input_text = get_font(40).render(answer, True, white)
        inputRect = input_text.get_rect()
        inputRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)  # Adjust position as needed
        screen.blit(input_text, inputRect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Check if Enter key is pressed to submit answer
                    if check_answer(answer, correct_answer):
                       return True
                    else:
                       return False
                       run = False
                elif event.key == pygame.K_BACKSPACE:  # Check if Backspace key is pressed to delete characters
                    answer = answer[:-1]
                else:
                    # Check if a printable character is pressed and append it to the answer
                    if event.unicode.isprintable():
                        answer += event.unicode

        # Update the display
        pygame.display.update()

def lose_screen(x_pos):
    """
    Displays the lose screen when the player loses the game.

    Args:
        x_pos (int): The x position of the dead panda.
    """
    run = True    
    screen.blit(DEAD_PANDA, (x_pos-5, 385))
    pygame.display.update()
    pygame.time.delay(2000)
    # play sound once
    LOSS.play()
    while run:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()
        
        # Load buttons
        RETURN = Button(image = pygame.image.load("images/scroll_button.png"), pos = (400, 500), text_input = "TITLE SCREEN", font = get_font(18), base_colour = "#b51f09", hovering_colour = "White")
        
        screen.blit(LOSE_SCREEN, (0, 0))

        RETURN.changeColour(GAME_MOUSE_POS)
        RETURN.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN.checkInput(GAME_MOUSE_POS):
                    run = False

        if (660<MOUSE_X<685 and 390<MOUSE_Y<415):
            screen.blit(RESIZED_NEXT, (510, 249))
        
        # Update the display
        pygame.display.update()
    return 

def win_screen():
    """
    Displays the win screen when the player wins the game.
    """
    
    # play sound once
    WIN.play()

    run = True
    while run:
            MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
            GAME_MOUSE_POS = pygame.mouse.get_pos()

            # Load buttons
            RETURN = Button(image = pygame.image.load("images/scroll_button.png"), pos = (400, 500), text_input = "TITLE SCREEN", font = get_font(18), base_colour = "#b51f09", hovering_colour = "White")
            
            screen.blit(WIN_SCREEN, (0, 0))

            RETURN.changeColour(GAME_MOUSE_POS)
            RETURN.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if RETURN.checkInput(GAME_MOUSE_POS):
                        return

            if (660<MOUSE_X<685 and 390<MOUSE_Y<415):
                screen.blit(RESIZED_NEXT, (510, 249))
            
            # Update the display
            pygame.display.update()
    return 

def generate_arrows(incorrect_counter, num_pandas):
    """
    Generates the number of arrows based on the number of pandas and the incorrect counter.

    Args:
        incorrect_counter (int): The number of incorrect answers given by the player.
        num_pandas (int): The number of pandas.

    Returns:
        int: The number of arrows to be generated.
    """
    randomizer = random.randint(1, 100)
    if incorrect_counter == 0:
        if num_pandas < 4:
            num_arrows = 1
        elif num_pandas < 6:
            num_arrows = 2
        elif num_pandas < 8:
            num_arrows = 3
        elif num_pandas < 10:
            num_arrows = 4
        else:
            reducer = num_pandas-10
            num_arrows = random.randint(reducer, reducer +5) 
    elif incorrect_counter == 1:
        if randomizer < 100:
            num_arrows = num_pandas + random.randint(1,20)
        else:
            num_arrows = round(num_pandas/2)
    elif incorrect_counter == 2:
        if randomizer < 85:
            num_arrows = num_pandas + random.randint(1,20)
        else:
            num_arrows = round(num_pandas/2)
    else:
        num_arrows = num_pandas + random.randint(1,20)
    
    return num_arrows

def start_game(username, password):
    """
    Starts the main game loop.

    Args:
        username (str): The username of the player.
        password (str): The password of the player.
    """
    # Scrolling variables
    scroll = 0
    scroll_speed = 4
    x = (SCREEN_WIDTH) // 2
    speed = 5
    num_arrows = 1
    num_pandas = 1
    incorrect_counter = 0
    gates = 0

    # initialize player
    player = Player(name=username, password=password)
    player.load_player()
    current_question = Question(player)
    question_text = current_question.generate_question('*')
    
    run = True
    # Main game loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if x > 200:
                x -= speed
        if keys[pygame.K_RIGHT]:
            if x < 550:
                x += speed

        # Scroll the image
        scroll += scroll_speed
        if scroll >= scaled_height:
            scroll = 0

        # Check if arrow hits the panda
        if scroll == 0:
            if num_arrows >= num_pandas:
                lose_screen(x)
                run = False  # Exit the function if game ends
            else:
                num_pandas -= num_arrows
            
        num_arrows = generate_arrows(incorrect_counter, num_pandas)


        #checks what gate the panda enters
        if scroll == 400:
            if x > SCREEN_WIDTH // 2:

                if question(num_pandas, question_text[1]):
                    num_pandas *= question_text[1]
                    incorrect_counter = 0
                else:
                    incorrect_counter +=1
                    gates -= 1
            else:
                if question(num_pandas, question_text[0]):
                    num_pandas *= question_text[0]
                    incorrect_counter = 0
                else:
                    incorrect_counter += 1
                    gates -= 1
            question_text = current_question.generate_question('*')
            gates += 1
            if gates == 5:
                player.update_mul(str(int(player.get_mul()) + 1))
                win_screen()
                break

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the scaled image twice to create the looping effect and gates
        screen.blit(scaled_image, (0, scroll - scaled_height))
        screen.blit(scaled_image, (0, scroll))
        screen.blit(GATE, (200, scroll - 125))

        # draw current score and level
        score_text = get_font(20).render((f"Score: {gates}"), True, white)
        level_text = get_font(20).render((f"Level: {player.get_mul()}"), True, white)
        screen.blit(score_text, (25, 20))
        screen.blit(level_text, (25, 50))


        # Draw the panda and arrow
        amplitude = 10
        frequency = 10
        time = pygame.time.get_ticks() / 1000
        offset_y = amplitude * math.sin(frequency * time)
        # Update the rect position of panda
        panda_rect.y = 395 + offset_y
        panda_rect.x = x
        arrow_rect.y = scroll - 450
        arrow_rect.x = x

        screen.blit(PANDA, panda_rect)
        screen.blit(ARROW, (arrow_rect))

        # Display number of arrows and pandas
        arrow_text = get_font(20).render(str(num_arrows), True, white)
        screen.blit(arrow_text, (x+20, scroll - 475))

        panda_text = get_font(20).render(str(num_pandas), True, white)
        screen.blit(panda_text, (x + 15, 450))

        # gets numbers for the gates
        num1 = get_font(40).render(str(question_text[0]), True, white)
        num2 = get_font(40).render(str(question_text[1]), True, white)

        if scroll-85 < 315:
            screen.blit(num1, (285, scroll - 85))
            screen.blit(num2, (485, scroll - 85))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

    return

def play_music(file):
    """
    Starts the main game loop.

    Args:
        username (str): The username of the player.
        password (str): The password of the player.
    """
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

def running_army(username, password):
    """
    Initializes and runs the "Running Army" game.

    Args:
        username (str): The username of the player.
        password (str): The password of the player.
    """
    play_music("sound/RunningArmyMusic.mp3")
    run = True
    while run:
        # display start screen
        screen.blit(START_SCREEN, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()

        START_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 250), text_input = "START GAME", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")
        INSTRUCTION_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 380), text_input = "INSTRUCTIONS", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")
        RETURN_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 510), text_input = "BACK TO MENU", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")

        for button in [START_BUTTON, INSTRUCTION_BUTTON, RETURN_BUTTON] :
            button.changeColour(MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.checkInput(MOUSE_POS):
                    start_game(username, password)
                if INSTRUCTION_BUTTON.checkInput(MOUSE_POS):
                    instruction1()
                if RETURN_BUTTON.checkInput(MOUSE_POS):
                    run = False
                    break

        # Update the display
        pygame.display.update()

    # Quit back to the game map
    pygame.mixer.music.stop()
    return
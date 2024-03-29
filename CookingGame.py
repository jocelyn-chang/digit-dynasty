import pygame, sys
import random
from Button import Button
from question import Question
from Player import Player

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Dumpling and Photo Settings
DUMPLING_SIZE = 100
PHOTO_SIZE = (200, 250)
PHOTO_INTERVAL_MS = 100
PHOTO_SPACING = 150

# Colors
WHITE = (255, 255, 255)
GREEN = (88, 133, 120)

# Load images
BACKGROUND = pygame.image.load("images/cooking_game.png")
DUMPLING = pygame.image.load("images/dumpling.png")
DUMPLING = pygame.transform.scale(DUMPLING, (DUMPLING_SIZE, DUMPLING_SIZE))
ORDER = pygame.image.load("images/order.png")
ORDER = pygame.transform.scale(ORDER, PHOTO_SIZE)

#changing screens
INSTRUCTION = pygame.image.load("images/Subtraction.png")
TUTORIAL = pygame.image.load("images/Instructions for cooking game.png")
BACK = pygame.image.load("images/back_button.png")
RESIZED_BACK = pygame.image.load("images/resized_back.png")
RESIZED_NEXT = pygame.transform.rotate(pygame.image.load("images/resized_back.png"), 180)
start_screen = pygame.image.load("images/Cooking Game Start Screen.png")

LOSE_SCREEN = pygame.image.load("images/Cooking game lose game.png")
WIN_SCREEN = pygame.image.load("images/Cooking game winning.png")

BACK = pygame.image.load("images/back_button.png")
RESIZED_BACK = pygame.image.load("images/resized_back.png")

# Initialize the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('COOKING GAME')

# Clock for controlling game speed
clock = pygame.time.Clock()

number_of_dumplings = 0

def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

def get_font(size):
    """
    Returns the font used in the game of a specified size.

    :param size: The size of the font to be returned.
    :type size: int
    :return: A pygame font object of the specified size.
    :rtype: pygame.font.Font
    """
    return pygame.font.Font("fonts/Shojumaru-Regular.ttf", size)

def instruction():
    run = True
    while run:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(INSTRUCTION, (0, 0))
        
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
                    tutorial()
                    run = False

        pygame.display.update()

def tutorial():
    run = True
    while run:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(TUTORIAL, (0, 0))
        
        INSTRUCTIONS_BACK = Button(pygame.image.load("images/back_button.png"), pos = (70, 55), text_input = "", font = get_font(15), base_colour = "White", hovering_colour = "#b51f09")
        #INSTRUCTIONS_NEXT = Button(pygame.transform.rotate(pygame.image.load("images/back_button.png"), 180), pos = (680, 475), text_input = "", font = get_font(15), base_colour = "White", hovering_colour = "#b51f09")
        
        if (40<MOUSE_X<75 and 40<MOUSE_Y<70):
            screen.blit(RESIZED_BACK, (-90,-96))
        if (690<MOUSE_X<705 and 465<MOUSE_Y<490):
            screen.blit(RESIZED_NEXT, (540, 324))

        INSTRUCTIONS_BACK.update(screen)
        #INSTRUCTIONS_NEXT.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkInput(GAME_MOUSE_POS): #or INSTRUCTIONS_NEXT.checkInput(GAME_MOUSE_POS):
                    run = False

        pygame.display.update()


def handle_events(dumpling_positions, central_area, questions):
    global number_of_dumplings
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            MOUSE_POS = pygame.mouse.get_pos()
            MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
            BACK = Button(image="images/back_button.png", pos=(40, 25), text_input="", font=get_font(22), base_colour="White", hovering_colour="#b51f09")
            BACK.update(screen)
            
            if (10<MOUSE_X<45 and 10<MOUSE_Y<40):
                screen.blit(RESIZED_BACK, (-120,-126))
            
            if BACK.checkInput(MOUSE_POS):
                return 3  # Signal that we should go back
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                add_dumpling(dumpling_positions, central_area)
                number_of_dumplings += 1
            elif event.key == pygame.K_LEFT and dumpling_positions:
                dumpling_positions.pop()
                number_of_dumplings -= 1
            elif event.key == pygame.K_SPACE and questions:  # Check answer when space bar is pressed
                # Assume the question is directly asking for the number of dumplings
                if number_of_dumplings == questions[0][1]:  # Assuming the question is simply the expected number
                    # Clears the number of dumplings on the screen when the question is answered correctly
                    dumpling_positions.clear()
                    number_of_dumplings = 0
                    return 1
                else:
                    dumpling_positions.clear()
                    return 2
    return None 
    #return True

def add_dumpling(dumpling_positions, central_area):
    new_x = random.randint(central_area.left, central_area.right - DUMPLING_SIZE)
    new_y = random.randint(central_area.top, central_area.bottom - DUMPLING_SIZE)
    dumpling_positions.append((new_x, new_y))


def update_photos(photo_positions, last_photo_time, current_time, total_questions_generated):
    photo_added = False  # Track if a new photo is added
    if current_time - last_photo_time > PHOTO_INTERVAL_MS and total_questions_generated < 5:
        # Check if it's time to add a new photo and we haven't exceeded 5 questions
        last_photo_x, last_photo_y = photo_positions[-1] if photo_positions else (0, 0)
        new_photo_x = last_photo_x + PHOTO_SPACING if photo_positions else 0  # Adjust for the first photo
        if new_photo_x + PHOTO_SIZE[0] <= SCREEN_WIDTH:
            photo_positions.append((new_photo_x, 0))
            last_photo_time = current_time
            photo_added = True  # A new photo was added
    return last_photo_time, photo_added
    

def lose_screen(correct_order, question):
    
    run = True    
    pygame.display.update()
    pygame.time.delay(1000)

    while run:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()
        # Load buttons
        RETURN = Button(image = pygame.image.load("images/scroll_button.png"), pos = (400, 500), text_input = "TITLE SCREEN", font = get_font(18), base_colour = "#b51f09", hovering_colour = "White")
        
        screen.blit(LOSE_SCREEN, (0, 0))
    
        if correct_order == 5:
            title_lines = ["Congratulations you moved up one level!"]
        else:
            title_lines = ["Incorrect", f"Correct Answer = {question[1]}", f"Your Answer = {number_of_dumplings}"]
        
        line_height = get_font(25).get_height()

        for i, line in enumerate(title_lines):
            title_text = get_font(35).render(line, True, WHITE)
            inputRect = title_text.get_rect()
            inputRect.center = (SCREEN_WIDTH // 2, 300 + i * line_height)  # Adjust position for each line
            screen.blit(title_text, inputRect)

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

def draw_screen(dumpling_positions, photo_positions, questions, level):
    screen.fill(WHITE)
    screen.blit(BACKGROUND, (0, 0))
    for pos in dumpling_positions:
        screen.blit(DUMPLING, pos)
    for i, pos in enumerate(photo_positions):
        screen.blit(ORDER, pos)
        if i < len(questions):
            question_text = questions[i]
            # Adjust text_surface creation to consider the size of the photo
            text_surface = get_font(20).render(question_text[0], True, (0, 0, 0))  # Black text
            # Calculate text position to center it on the photo
            text_x_adjustment = 30  # Adjust as needed for leftward movement
            text_y_adjustment = 50  # Adjust as needed for upward movement

            text_x = pos[0] + (PHOTO_SIZE[0] - text_surface.get_width()) // 2 - text_x_adjustment
            text_y = pos[1] + (PHOTO_SIZE[1] - text_surface.get_height()) // 2 - text_y_adjustment
            screen.blit(text_surface, (text_x, text_y))
            
    num_dumplings_text = get_font(20).render(f"Dumplings: {len(dumpling_positions)}", True, (0, 0, 0))
    screen.blit(num_dumplings_text, (26, SCREEN_HEIGHT - 55))
    
    score_text = get_font(20).render(f"Score: {correct_answer}", True, (0, 0, 0))
    screen.blit(score_text, (26, SCREEN_HEIGHT - 95))
        
    level_text = get_font(20).render(f"Level: {level}", True, (0, 0, 0))
    screen.blit(level_text, (26, SCREEN_HEIGHT - 135))
    
    MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
    BACK = Button(image="images/back_button.png", pos=(40, 25), text_input="", font=get_font(22), base_colour="White", hovering_colour="#b51f09")
    BACK.update(screen)
            
    if (10<MOUSE_X<45 and 10<MOUSE_Y<40):
        screen.blit(RESIZED_BACK, (-120,-126))
    
    '''
    BACK = Button(image="images/back_button.png", pos=(40, 25), text_input="", font=get_font(22), base_colour="White", hovering_colour="#b51f09")
    BACK.update(screen)
    
    MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
    
    if (10<MOUSE_X<45 and 10<MOUSE_Y<40):
        screen.blit(RESIZED_BACK, (-120,-126))
    

    for event in pygame.event.get():
        MOUSE_POS = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if BACK.checkInput(MOUSE_POS):
                return True  # Signal that the BACK button was pressed
    '''
    pygame.display.flip()


def playGame(username, password):
    player = Player(username, password)
    player.load_player()
    
    global correct_answer, number_of_dumplings
    
    correct_answer = 0
    number_of_dumplings = 0
    
    done = False
    dumpling_positions = []
    photo_positions = []
    questions = []
    last_photo_time = pygame.time.get_ticks()
    
    central_area = pygame.Rect(
        (SCREEN_WIDTH - SCREEN_WIDTH // 3) // 2, 
        (SCREEN_HEIGHT - SCREEN_HEIGHT // 3) // 2, 
        SCREEN_WIDTH // 3, 
        SCREEN_HEIGHT // 3
    )
    
    total_questions_generated = 0  # Keep track of the total number of questions generated
    
    level = int(player.get_sub())
    
    
    current_question = Question(player)
    
    while not done:
        current_time = pygame.time.get_ticks()
        ans = handle_events(dumpling_positions, central_area, questions)
        
        
        if ans == 2:
            lose_screen(correct_answer, questions[0])
            done = True
            break
        
        elif ans == 3:
            return
        
        elif ans == 1 and questions:
            correct_answer = correct_answer + 1
            questions.pop(0)  # Remove the answered question
            photo_positions.pop(0)  # Remove the corresponding photo
        
        last_photo_time, photo_added = update_photos(photo_positions, last_photo_time, current_time, total_questions_generated)
        if photo_added and total_questions_generated < 5:
            question_text = current_question.generate_question('-')
            questions.append(question_text)
            total_questions_generated += 1
            
        draw_screen(dumpling_positions, photo_positions, questions, level)
        
        if total_questions_generated >= 5 and not questions:
            questions.append('done')
            # End the game when all 5 questions have been generated and answered
            if correct_answer == 5:
                level = level + 1
                player.update_sub(str(level))
            win_screen()
            done = True
        
        
        pygame.time.Clock().tick(60)
        pygame.display.flip()
    
    return


def cooking_game(username, password):
    play_music("sound/CookingGameMusic.mp3")
    run = True
    while run:
        # display start screen
        screen.blit(start_screen, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()

        START_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 250), text_input = "START GAME", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")
        INSTRUCTION_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 380), text_input = "INSTRUCTIONS", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")
        RETURN_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 510), text_input = "BACK TO MENU", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")
        
        for button in [START_BUTTON, INSTRUCTION_BUTTON, RETURN_BUTTON]:
            button.changeColour(MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if START_BUTTON.checkInput(MOUSE_POS):
                        playGame(username, password)
                    if INSTRUCTION_BUTTON.checkInput(MOUSE_POS):
                        instruction()
                    if RETURN_BUTTON.checkInput(MOUSE_POS):
                        run = False
                        break
        # Update the display
        pygame.display.update()

    # Quit back to the game map
    pygame.mixer.music.stop()
    return
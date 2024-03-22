import pygame, sys
from Button import Button
from question import Question


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
start_screen = pygame.image.load("images/Running Army Start Screen.png")
image = pygame.image.load("images/running_army_bg.png")
panda = pygame.transform.scale(pygame.image.load("images/panda1.png"), (50, 50))
gate = pygame.transform.scale(pygame.image.load("images/gates.png"), (400, 125))
qbox = pygame.transform.scale(pygame.image.load("images/questionscreen.png"), (400, 125))
arrow = pygame.transform.scale(pygame.image.load("images/parrow.png"), (50, 50))
question_scroll = pygame.image.load("images/bigScroll.png")

image_height = image.get_height()
image_width = image.get_width()

# define colours
white = (255, 255, 255)

# movement for panda/arrow
arrow_rect = arrow.get_rect()
panda_rect = panda.get_rect()


# Calculate the new height of the image to maintain the aspect ratio
scaled_height = int(image_height * (SCREEN_WIDTH / image_width))

# Scale the image to fill the width of the screen while maintaining the aspect ratio
scaled_image = pygame.transform.scale(image, (SCREEN_WIDTH, scaled_height))


# get the font
def get_font(size):
    return pygame.font.Font("fonts/Shojumaru-Regular.ttf", size)

# Intructions screen
def instruction1():
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
            
    #    # Get mouse position
    #     mouse_pos = pygame.mouse.get_pos()
    #     mouse_x, mouse_y = mouse_pos

    #     # Display mouse position on the screen
    #     font = pygame.font.Font(None, 36)
    #     text = font.render(f"Mouse Position: ({mouse_x}, {mouse_y})", True, (0, 0, 0))
    #     screen.blit(text, (10, 10))

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
    run = True
    while run:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        screen.blit(INSTRUCTION2, (0, 0))
        
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
                if INSTRUCTIONS_BACK.checkInput(GAME_MOUSE_POS) or INSTRUCTIONS_NEXT.checkInput(GAME_MOUSE_POS):
                    run = False

        pygame.display.update()

def check_answer(answer, correct_answer):
    # Display question screen
    screen.blit(question_scroll, (25, 100))
    title = get_font(25).render("Answer the Following Question:", True, white)
    titleRect = title.get_rect()
    titleRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
    screen.blit(title, titleRect)
            
    if answer == correct_answer:
        # Display user's input text
        correct = get_font(20).render('CORRECT', True, white)
        inputRect = correct.get_rect()
        inputRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Adjust position as needed
        screen.blit(correct, inputRect)

    else:
        # Display user's input text
        incorrect = get_font(20).render('Incorrect', True, white)
        inputRect = incorrect.get_rect()
        inputRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Adjust position as needed
        screen.blit(incorrect, inputRect)

    # Update the display
    pygame.display.update()
    pygame.time.delay(3000)

    return True


def question():
    answer = ""
    correct_answer = "5"
    run = True

    while run:
        # Display question screen
        screen.blit(question_scroll, (25, 100))
        title = get_font(25).render("Answer the Following Question:", True, white)
        titleRect = title.get_rect()
        titleRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
        screen.blit(title, titleRect)

        # Display user's input text
        input_text = get_font(20).render(answer, True, white)
        inputRect = input_text.get_rect()
        inputRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Adjust position as needed
        screen.blit(input_text, inputRect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Check if Enter key is pressed to submit answer
                    if check_answer(answer, correct_answer):
                       run = False
                elif event.key == pygame.K_BACKSPACE:  # Check if Backspace key is pressed to delete characters
                    answer = answer[:-1]
                else:
                    # Check if a printable character is pressed and append it to the answer
                    if event.unicode.isprintable():
                        answer += event.unicode

        # Update the display
        pygame.display.update()

def end_game_screen(levels):
    run = True
    NEXT_BUTTON = Button(pygame.transform.rotate(pygame.image.load("images/back_button.png"), 180), pos = (650, 400), text_input = "", font = get_font(15), base_colour = "White", hovering_colour = "#b51f09")


    while run:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()
        # Display question screen
        screen.blit(question_scroll, (25, 100))

        if levels > 0:
            title = get_font(25).render("Congratulations you imroved " + " levels", True, white)
        else:
            title = get_font(25).render("Keep practicing!", True, white)
        titleRect = title.get_rect()
        titleRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
        screen.blit(title, titleRect)

        # Display user's input text
        # input_text = get_font(20).render(title, True, white)
        # inputRect = input_text.get_rect()
        # inputRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Adjust position as needed
        # screen.blit(input_text, inputRect)

        if (660<MOUSE_X<685 and 390<MOUSE_Y<415):
            screen.blit(RESIZED_NEXT, (510, 249))
        
        NEXT_BUTTON.update(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEXT_BUTTON.checkInput(GAME_MOUSE_POS):
                    run = False
        # Update the display
        pygame.display.update()

def start_game():
    # Scrolling variables
    scroll = 0
    scroll_speed = 2
    x = (SCREEN_WIDTH) // 2
    speed = 5
    num_arrows = 1
    num_pandas = 2
    
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
                end_game_screen(0)  # Adjust the parameter as needed
                run = False  # Exit the function if game ends

            else:
                num_pandas -= num_arrows
                print(num_pandas)

        #checks what gate the panda enters
        if scroll == 400:
            if x > SCREEN_WIDTH // 2:
                print("panda on the right half")
            else:
                print("panda on the left half")

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the scaled image twice to create the looping effect and gates
        screen.blit(scaled_image, (0, scroll - scaled_height))
        screen.blit(scaled_image, (0, scroll))
        screen.blit(gate, (200, scroll - 125))

        # Draw the panda and arrow
        screen.blit(panda, (x, 395))
        screen.blit(arrow, (x, scroll - 450))

        # Display number of arrows and pandas
        arrow_text = get_font(20).render(str(num_arrows), True, white)
        screen.blit(arrow_text, (x+20, scroll - 475))

        panda_text = get_font(20).render(str(num_pandas), True, white)
        screen.blit(panda_text, (x + 15, 450))

        # gets numbers for the gates


        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

    return


def running_army():
    # Main game loop
    run = True
    while run:
        # display start screen
        screen.blit(start_screen, (0,0))
        MOUSE_POS = pygame.mouse.get_pos()

        START_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 250), text_input = "START GAME", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")
        INSTRUCTION_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 380), text_input = "INSTRUCTIONS", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")
        RETURN_BUTTON = Button(image = pygame.image.load("images/scroll_button.png"), pos = (395, 510), text_input = "BACK TO MENU", font = get_font(22), base_colour = "#b51f09", hovering_colour = "White")

        for button in [START_BUTTON, INSTRUCTION_BUTTON, RETURN_BUTTON] :
            button.changeColour(MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if START_BUTTON.checkInput(MOUSE_POS):
                        start_game()
                    if INSTRUCTION_BUTTON.checkInput(MOUSE_POS):
                        print("working")
                        instruction1()
                    if RETURN_BUTTON.checkInput(MOUSE_POS):
                        run = False
                        break

        # Update the display
        pygame.display.update()

    # Quit back to the game map
    return

# running_army()
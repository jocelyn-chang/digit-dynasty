import pygame
from Button import Button

pygame.init()

#Load Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Load Images
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DIGIT DYNASTY')
BACKGROUND = pygame.image.load("images/AE_background.png")
EMPERORMONKEY = pygame.image.load("images/emperor_monkey.png")
EMPERORPIG = pygame.image.load("images/emperor_pig.png")
EMPERORPHOENIX = pygame.image.load("images/emperor_phoenix.png")
EMPERORDRAGON = pygame.image.load("images/emperor_dragon.png")
QUESTIONSCROLL = pygame.image.load("images/bigScroll.png")

#Set up Variables
emperorLevel = 0
pandaHealth = 100
emperorHealth = 100 #multiply these by emperor level once determined
addAttackPower = 10 #multiply these by strength once determined
emperorHealthDisplayFactor = 188/emperorHealth
pandaHealthDisplayFactor = 188/pandaHealth
subAttackPower = 10
mulAttackPower = 10
divAttackPower = 10

# define colours
white = (255, 255, 255)

def get_font(font, size):
    if font == "Sawarabi":
        return pygame.font.Font("fonts/SawarabiMincho-Regular.ttf", size)
    elif font == "Shojumaru":
        return pygame.font.Font("fonts/Shojumaru-Regular.ttf", size)

def attack_emperor(attackType):
  global emperorHealth, emperorHealthDisplay
  emperorHealth = emperorHealth - attackType

def check_answer(answer, correct_answer):
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
        # Display user's input text
        incorrect = get_font("Shojumaru", 20).render(f"Incorrect, Correct answer = {correct_answer}  your answer = {answer}", True, white)
        inputRect = incorrect.get_rect()
        inputRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Adjust position as needed
        SCREEN.blit(incorrect, inputRect)

    # Update the display
    pygame.display.update()
    pygame.time.delay(3000)

    return correct

def question():
    answer = ""
    correct_answer = 6
    run = True

    while run:
      
        # Display question screen
        SCREEN.blit(QUESTIONSCROLL, (25, 100))
        title = get_font("Shojumaru", 20).render("Answer the Following Question:", True, white)
        titleRect = title.get_rect()
        titleRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
        SCREEN.blit(title, titleRect)

        title = get_font("Shojumaru", 40).render(f"3 X 2", True, white)
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
                       run = False
                elif event.key == pygame.K_BACKSPACE:  # Check if Backspace key is pressed to delete characters
                    answer = answer[:-1]
                else:
                    # Check if a printable character is pressed and append it to the answer
                    if event.unicode.isprintable():
                        answer += event.unicode

        # Update the display
        pygame.display.update()

def start_game():
  global emperorHealth, emperorHealthDisplayFactor, pandaHealthDisplayFactor
  while True:

    # Draw the background image onto the screen
    SCREEN.blit(BACKGROUND, (0, 0))
    SCREEN.blit(EMPERORMONKEY, (460, 40))
    pygame.draw.rect(SCREEN, (239, 39, 39), pygame.Rect(130, 102, emperorHealthDisplayFactor*emperorHealth, 20))
    pygame.draw.rect(SCREEN, (239, 39, 39), pygame.Rect(543, 430, 188, 20))

    #Get Mouse Pos
    MOUSE_POS = pygame.mouse.get_pos()  

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
            attack_emperor(addAttackPower)
            question()
        if DIV_BUTTON.checkInput(MOUSE_POS):
            attack_emperor(divAttackPower)
            question()
        if SUB_BUTTON.checkInput(MOUSE_POS):
            attack_emperor(subAttackPower)
            question()
        if MUL_BUTTON.checkInput(MOUSE_POS):
            attack_emperor(mulAttackPower)
            question()

    mouse_x, mouse_y = MOUSE_POS
    font = pygame.font.Font(None, 36)
    text = font.render(f"Mouse Position: ({mouse_x}, {mouse_y})", True, (0,0,0))
    SCREEN.blit(text,(10,10))

    # Update the display
    pygame.display.flip()

start_game()
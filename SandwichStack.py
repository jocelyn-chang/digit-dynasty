# Import appropriate libraries
import pygame, sys, random
from Button import Button
from Player import Player
from question import Question

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PANDA_SPEED = 4

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SANDWICH STACK')
BACKGROUND = pygame.image.load("images/sandwich_stack_bg.png")
START_SCREEN = pygame.image.load("images/sandwich_stack_start.png")
DIVISION_INSTRUCTIONS = pygame.image.load("images/division_instruction.png")
SS_INSTRUCTIONS = pygame.image.load("images/ss_instructions.png")
RECTANGLE = pygame.image.load("images/rectangle.png")
LINE = pygame.image.load("images/line.png")
BACK = pygame.image.load("images/back_button.png")
RESIZED_BACK = pygame.image.load("images/resized_back.png")
RESIZED_NEXT = pygame.transform.rotate(pygame.image.load("images/resized_back.png"), 180)

PANDA = pygame.transform.scale(pygame.image.load("images/panda_tray.png"), (190, 126))
CARROT = pygame.transform.scale(pygame.image.load("images/carrot.png"), (75, 79))
BREAD = pygame.transform.scale(pygame.image.load("images/bread.png"), (90, 62))
CUCUMBER = pygame.transform.scale(pygame.image.load("images/cucumber.png"), (70, 70))
MEAT = pygame.transform.scale(pygame.image.load("images/meat.png"), (115, 54))

food_items = [CARROT, BREAD, CUCUMBER, MEAT]
panda_rect = PANDA.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - 50))

GAME_STATES = {'START' : 1,
               'INSTRUCTION1': 2,
               'INSTRUCTION2': 3,
               'PLAY': 4}
current_state = GAME_STATES['START']

def get_font(font, size):
    if font == "Sawarabi":
        return pygame.font.Font("fonts/SawarabiMincho-Regular.ttf", size)
    elif font == "Shojumaru":
        return pygame.font.Font("fonts/Shojumaru-Regular.ttf", size)
    pass

def spawn_food(answer_bank):
    food = random.choice(food_items)
    answer = str(random.choice(answer_bank))
    x_pos = random.randrange(0, SCREEN_WIDTH - food.get_width())
    y_pos = -food.get_height()
    food_rect = food.get_rect(topleft = (x_pos, y_pos))

    font = get_font('Shojumaru', 9)
    text_surface = font.render(answer, True, "black")
    text_rect = text_surface.get_rect(center = (food_rect.centerx, food_rect.top - 10))
    return food, food_rect, answer

current_food, current_food_rect, current_answer = spawn_food([random.randint(1, 144), random.randint(1, 144)])

# Intructions screen
def instruction1():
    global current_state
    MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
    GAME_MOUSE_POS = pygame.mouse.get_pos()

    SCREEN.blit(DIVISION_INSTRUCTIONS, (0, 0))
    
    INSTRUCTIONS_BACK = Button(pygame.image.load("images/back_button.png"), pos = (70, 55), text_input = "", font = get_font("Shojumaru", 15), base_colour = "White", hovering_colour = "#b51f09")
    INSTRUCTIONS_NEXT = Button(pygame.transform.rotate(pygame.image.load("images/back_button.png"), 180), pos = (680, 475), text_input = "", font = get_font("Shojumaru", 15), base_colour = "White", hovering_colour = "#b51f09")
    INSTRUCTIONS_BACK.update(SCREEN)
    INSTRUCTIONS_NEXT.update(SCREEN)

    if (40 < MOUSE_X < 75 and 40 < MOUSE_Y < 70):
        SCREEN.blit(RESIZED_BACK, (-90,-96))
    if (690 < MOUSE_X < 705 and 465 < MOUSE_Y < 490):
        SCREEN.blit(RESIZED_NEXT, (540, 324))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if INSTRUCTIONS_BACK.checkInput(GAME_MOUSE_POS):
                current_state = GAME_STATES['START']
                return
            if INSTRUCTIONS_NEXT.checkInput(GAME_MOUSE_POS):
                current_state = GAME_STATES['INSTRUCTION2']
                return

        pygame.display.update()
        pass

def instruction2():
    global current_state
    MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
    GAME_MOUSE_POS = pygame.mouse.get_pos()

    SCREEN.blit(SS_INSTRUCTIONS, (0, 0))
    
    INSTRUCTIONS_BACK = Button(pygame.image.load("images/back_button.png"), pos = (70, 55), text_input = "", font = get_font("Shojumaru", 15), base_colour = "White", hovering_colour = "#b51f09")
    INSTRUCTIONS_BACK.update(SCREEN)

    if (40 < MOUSE_X < 75 and 40 < MOUSE_Y < 70):
        SCREEN.blit(RESIZED_BACK, (-90,-96))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if INSTRUCTIONS_BACK.checkInput(GAME_MOUSE_POS):
                current_state = GAME_STATES['INSTRUCTION1']
                return

    pygame.display.update()
    pass


def sandwich_stack(username, password):
    global current_state
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
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if START_BUTTON.checkInput(MOUSE_POS):
                    current_state = GAME_STATES['PLAY']
                    return
            if INSTRUCTION_BUTTON.checkInput(MOUSE_POS):
                    current_state = GAME_STATES['INSTRUCTION1']
                    return
            if RETURN_BUTTON.checkInput(MOUSE_POS):
                    return

    # Update the display
    pygame.display.update()
    pass

def start_game(username, password):
    global current_state
    lives = 3
    score = 0

    #player = Player(username, password)
    #player.load_player()
    
    while lives > 0:
        global current_food, current_food_rect, current_answer
        MOUSE_POS = pygame.mouse.get_pos()
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()

        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(PANDA, panda_rect)
        SCREEN.blit(current_food, current_food_rect)
        SCREEN.blit(RECTANGLE, (0,0))
        SCREEN.blit(LINE, (0, 47))
        SCREEN.blit(LINE, (0, 149))

        BACK = Button(image = "images/back_button.png", pos = (40, 25), text_input = "", font = get_font("Shojumaru",22), base_colour = "White", hovering_colour = "#b51f09")
        BACK.update(SCREEN)

        if (10 < MOUSE_X < 45 and 10 < MOUSE_Y < 40):
            SCREEN.blit(RESIZED_BACK, (-120,-126))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkInput(MOUSE_POS):
                    current_state = GAME_STATES['START']
                    return

        cur_question = Question(username, password)
        question = cur_question.generate_question("/")

        answer_bank = [random.randint(1, 144), question[1]]
        current_food, current_food_rect, current_answer = spawn_food(answer_bank)

        font = get_font('Shojumaru', 13)
        text_surface = font.render('What is the answer to:', True, "White")
        question_surface = font.render(str(question[0]), True, "white")
        SCREEN.blit(text_surface, (50, 80))
        SCREEN.blit(question_surface, (50, 100))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and panda_rect.left > 0:
            panda_rect.x -= PANDA_SPEED
        if keys[pygame.K_RIGHT] and panda_rect.right < SCREEN_WIDTH:
            panda_rect.x += PANDA_SPEED

        current_food_rect.y += 2

        if panda_rect.colliderect(current_food_rect):
            if current_answer == question[1]:
                score += 1
            else:
                lives -= 1
            current_food, current_food_rect, current_answer = spawn_food(answer_bank)

        if current_food_rect.top > SCREEN_HEIGHT:
            current_food, current_food_rect, current_answer = spawn_food(answer_bank)

    pygame.display.update()
    pass

username = "Audrey"
password = "AudreyLi192004"
# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw based on the current game state
    if current_state == GAME_STATES['START']:
        sandwich_stack(username, password)
    elif current_state == GAME_STATES['INSTRUCTION1']:
        instruction1()
    elif current_state == GAME_STATES['INSTRUCTION2']:
        instruction2()
    elif current_state == GAME_STATES['PLAY']:
        start_game(username, password)  # This function now needs to handle drawing and updating the game state itself

    pygame.display.flip()

pygame.quit()
sys.exit()
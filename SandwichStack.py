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
WIN_SCREEN = pygame.image.load("images/ss_win_screen.png")
LOSE_SCREEN = pygame.image.load("images/ss_lose_screen.png")
RECTANGLE = pygame.image.load("images/rectangle.png")
LINE = pygame.image.load("images/line.png")
BACK = pygame.image.load("images/back_button.png")
RESIZED_BACK = pygame.image.load("images/resized_back.png")
RESIZED_NEXT = pygame.transform.rotate(pygame.image.load("images/resized_back.png"), 180)
HEART_F = pygame.image.load("images/heart_full.png")
HEART_E = pygame.image.load("images/heart_empty.png")
HEART_FULL = pygame.transform.scale(HEART_F, (50, 50))
HEART_EMPTY = pygame.transform.scale(HEART_E, (50, 50))

PANDA = pygame.transform.scale(pygame.image.load("images/panda_tray.png"), (190, 126))
CARROT = pygame.transform.scale(pygame.image.load("images/carrot.png"), (75, 79))
BREAD = pygame.transform.scale(pygame.image.load("images/bread.png"), (90, 62))
CUCUMBER = pygame.transform.scale(pygame.image.load("images/cucumber.png"), (70, 70))
MEAT = pygame.transform.scale(pygame.image.load("images/meat.png"), (115, 54))

food_items = [CARROT, BREAD, CUCUMBER, MEAT]
panda_rect = PANDA.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - 50))

def get_font(font, size):
    if font == "Sawarabi":
        return pygame.font.Font("fonts/SawarabiMincho-Regular.ttf", size)
    elif font == "Shojumaru":
        return pygame.font.Font("fonts/Shojumaru-Regular.ttf", size)

def spawn_food(answer_bank):
    food = random.choice(food_items)
    answer = random.choice(answer_bank)
    x_pos = random.randrange(0, SCREEN_WIDTH - food.get_width())
    y_pos = -food.get_height()
    food_rect = food.get_rect(topleft = (x_pos, y_pos))

    font = get_font('Shojumaru', 15)
    text_surface = font.render(str(answer), True, "white")
    text_rect = text_surface.get_rect(center = (food_rect.centerx, food_rect.y - 20))
    return food, food_rect, answer, text_surface, text_rect


current_food, current_food_rect, current_answer, answer_text_surface, answer_text_rect = spawn_food([random.randint(1, 144), random.randint(1, 144)])

# Intructions screen
def instruction1():
    while True:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(DIVISION_INSTRUCTIONS, (0, 0))
        
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
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkInput(GAME_MOUSE_POS):
                    return
                if INSTRUCTIONS_NEXT.checkInput(GAME_MOUSE_POS):
                    instruction2()

        pygame.display.update()

def instruction2():
    while True:
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
                    return

        pygame.display.update()

def sandwich_stack(username, password):
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
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.checkInput(MOUSE_POS):
                      start_game(username, password)
                if INSTRUCTION_BUTTON.checkInput(MOUSE_POS):
                     instruction1()
                if RETURN_BUTTON.checkInput(MOUSE_POS):
                     return

        # Update the display
        pygame.display.update()

def win_screen(score):
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(WIN_SCREEN, (0, 0))
        score_font = get_font("Shojumaru", 20)
        score_surface = score_font.render(f"Your Division Level is Now: {score}", True, "White")
        SCREEN.blit(score_surface, (215, 420))
            
        RETURN = Button(image = pygame.image.load("images/scroll_button.png"), pos = (SCREEN_WIDTH / 2, 520), text_input = "TITLE SCREEN", font = get_font("Shojumaru", 18), base_colour = "#b51f09", hovering_colour = "White")
        RETURN.changeColour(MOUSE_POS)
        RETURN.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN.checkInput(MOUSE_POS):
                    return

        pygame.display.update()

def lose_screen(username, password, score):
    player = Player(username, password)
    player.load_player()
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(LOSE_SCREEN, (0, 0))
        level_font = get_font("Shojumaru", 20)
        level_surface = level_font.render(f"Current level: {player.get_div()}", True, "White")
        SCREEN.blit(level_surface, (130, 340))

        score_font = get_font("Shojumaru", 20)
        score_surface = score_font.render(f"Score: {score} / 5", True, "White")
        SCREEN.blit(score_surface, (520, 340))

        RETURN = Button(image = pygame.image.load("images/scroll_button.png"), pos = (SCREEN_WIDTH / 2, 440), text_input = "TITLE SCREEN", font = get_font("Shojumaru", 18), base_colour = "#b51f09", hovering_colour = "White")
        RETURN.changeColour(MOUSE_POS)
        RETURN.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN.checkInput(MOUSE_POS):
                    return

        pygame.display.update()

def start_game(username, password):
    MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
    MOUSE_POS = pygame.mouse.get_pos()
    lives = 3
    score = 0

    message_active = True
    display_correct_message = False
    display_incorrect_message = False
    message_duration = 2000
    message_start_time = 0

    player = Player(username, password)
    player.load_player()

    answer_bank = [random.randint(1, 144) for _ in range(4)]  # Create an initial answer bank
    current_question = Question(player)
    correct_answer, question = current_question.generate_question("/")
    answer_bank[0] = correct_answer  # Ensure one of the answers is correct
    answers = [correct_answer, correct_answer]
    previous_answer = answers[0]

    # Re-use the global variables to keep the current state
    global current_food, current_food_rect, current_answer, answer_text_surface, answer_text_rect
    current_food, current_food_rect, current_answer, answer_text_surface, answer_text_rect = spawn_food(answer_bank)

    clock = pygame.time.Clock()  # To control the game's framerate

    game_active = True
    while game_active:
        MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
        MOUSE_POS = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkInput(MOUSE_POS):
                    return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and panda_rect.left > 0:
            panda_rect.x -= PANDA_SPEED
        if keys[pygame.K_RIGHT] and panda_rect.right < SCREEN_WIDTH:
            panda_rect.x += PANDA_SPEED

        current_food_rect.y += 3

        answer_text_rect.centerx = current_food_rect.centerx
        answer_text_rect.y = current_food_rect.y - 20

        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(PANDA, panda_rect)
        SCREEN.blit(current_food, current_food_rect)
        SCREEN.blit(answer_text_surface, answer_text_rect)
        SCREEN.blit(RECTANGLE, (0,0))
        SCREEN.blit(LINE, (0, 47))
        SCREEN.blit(LINE, (0, 149))

        font = get_font('Shojumaru', 20)
        text_surface = font.render('What is the answer to:', True, "White")
        question_surface = font.render(question, True, "White")
        SCREEN.blit(text_surface, (50, 75))
        SCREEN.blit(question_surface, (158, 100))

        BACK = Button(image = "images/back_button.png", pos = (40, 25), text_input = "", font = get_font("Shojumaru", 22), base_colour = "White", hovering_colour = "#b51f09")
        BACK.update(SCREEN)

        if (10<MOUSE_X<45 and 10<MOUSE_Y<40):
            SCREEN.blit(RESIZED_BACK, (-120,-126))

        if lives == 3:
            SCREEN.blit(HEART_FULL, (400, 90))
            SCREEN.blit(HEART_FULL, (450, 90))
            SCREEN.blit(HEART_FULL, (500, 90))
        elif lives == 2:
            SCREEN.blit(HEART_FULL, (400, 90))
            SCREEN.blit(HEART_FULL, (450, 90))
            SCREEN.blit(HEART_EMPTY, (500, 90))
        elif lives == 1:
            SCREEN.blit(HEART_FULL, (400, 90))
            SCREEN.blit(HEART_EMPTY, (450, 90))
            SCREEN.blit(HEART_EMPTY, (500, 90))

        score_surface = font.render(f'Score: {score} / 5', True, "White")
        lives_surface = font.render('Lives:', True, "White")
        SCREEN.blit(score_surface, (600, 80))
        SCREEN.blit(lives_surface, (440, 65))

        if panda_rect.colliderect(current_food_rect):
            message_start_time = pygame.time.get_ticks()
            message_active = True

            if current_answer == correct_answer:
                display_correct_message = True
                display_incorrect_message = False
                score += 1
            else:
                display_incorrect_message = True
                display_correct_message = False
                lives -= 1

            if score == 2:
                new_score = int(player.get_div()) + 1
                player.update_div(str(new_score))
                win_screen(new_score)
                return
            elif lives > 0:
                # Generate a new question and answer set
                answer_bank = [random.randint(1, 144) for _ in range(4)]
                correct_answer, question = current_question.generate_question("/")
                answer_bank[0] = correct_answer  # Update the answer bank with the new correct answer
                answers = [answers[1], correct_answer]
                previous_answer = answers[0]
                current_food, current_food_rect, current_answer, answer_text_surface, answer_text_rect = spawn_food(answer_bank)
            else:
                game_active = False  # End game loop if no lives left
                lose_screen(username, password, score)
                return

        if current_food_rect.top > SCREEN_HEIGHT:
            current_food, current_food_rect, current_answer, answer_text_surface, answer_text_rect = spawn_food(answer_bank)

        if message_active:
            elapsed_time = pygame.time.get_ticks() - message_start_time
            if elapsed_time < message_duration:
                if display_correct_message:
                    message_font = get_font("Shojumaru", 19)
                    message_surface = message_font.render("Correct!", True, "White")
                    SCREEN.blit(message_surface, (360, 160))
                if display_incorrect_message:
                    message_font = get_font('Shojumaru', 19)
                    message_surface = message_font.render(f"Incorrect. The answer is: {previous_answer}", True, "White")
                    SCREEN.blit(message_surface, (220, 160))
            else:
                message_active = False
                display_correct_message = False
                display_incorrect_message = False

        pygame.display.update()
        clock.tick(60)  # Keep the game running at 60 FPS


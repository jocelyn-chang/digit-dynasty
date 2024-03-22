# Import appropriate libraries
import pygame, sys, random
from Button import Button

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PANDA_SPEED = 4

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SANDWICH STACK')
BACKGROUND = pygame.image.load("images/sandwich_stack_bg.png")

PANDA = pygame.transform.scale(pygame.image.load("images/panda_tray.png"), (190, 126))
CARROT = pygame.transform.scale(pygame.image.load("images/carrot.png"), (75, 79))
BREAD = pygame.transform.scale(pygame.image.load("images/bread.png"), (90, 62))
CUCUMBER = pygame.transform.scale(pygame.image.load("images/cucumber.png"), (70, 70))
MEAT = pygame.transform.scale(pygame.image.load("images/meat.png"), (115, 54))

food_items = [CARROT, BREAD, CUCUMBER, MEAT]
panda_rect = PANDA.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - 50))

def spawn_food():
    food = random.choice(food_items)
    x_pos = random.randrange(0, SCREEN_WIDTH - food.get_width())
    y_pos = -food.get_height()
    food_rect = food.get_rect(topleft = (x_pos, y_pos))
    return food, food_rect

current_food, current_food_rect = spawn_food()

def sandwich_stack():
    global current_food, current_food_rect

    while True:
        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(PANDA, panda_rect)
        SCREEN.blit(current_food, current_food_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and panda_rect.left > 0:
            panda_rect.x -= PANDA_SPEED
        if keys[pygame.K_RIGHT] and panda_rect.right < SCREEN_WIDTH:
            panda_rect.x += PANDA_SPEED

        current_food_rect.y += 2

        if panda_rect.colliderect(current_food_rect):
            current_food, current_food_rect = spawn_food()

        if current_food_rect.top > SCREEN_HEIGHT:
            current_food, current_food_rect = spawn_food()

        pygame.display.update()

sandwich_stack()
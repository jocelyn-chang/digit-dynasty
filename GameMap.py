import pygame, sys
from Button import Button
from Player import Player
from runningArmy import running_army
from SnakeGame import snakeSums
from CookingGame import cooking_game
from SandwichStack import sandwich_stack
from ArithmeticEmperor import arithmetic_emperor

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DIGIT DYNASTY')
BACKGROUND = pygame.image.load("images/Map Screen.png")
LOCK_BACKGROUND = pygame.image.load("images/lock_map_screen.png")

LEFTTEMP = pygame.image.load("images/templeleft.png")
MULTTEMP = pygame.image.load("images/templeright.png")
TOPTEMP = pygame.image.load("images/templetop.png")
BOTTOMTEMP = pygame.image.load("images/templebottom.png")
MIDDLETEMP = pygame.image.load("images/templemiddle.png")
LOCKBOSS = pygame.image.load("images/lock_boss.png")
RESIZED_LEFTTEMP = pygame.transform.scale(LEFTTEMP, (110, 110))
RESIZED_MULTTEMP = pygame.transform.scale(MULTTEMP, (110, 110))
RESIZED_TOPTEMP = pygame.transform.scale(TOPTEMP, (103, 103))
RESIZED_BOTTOMTEMP = pygame.transform.scale(BOTTOMTEMP, (120, 120))
RESIZED_MIDDLETEMP = pygame.transform.scale(MIDDLETEMP, (150, 150))
RESIZED_LOCKBOSS = pygame.transform.scale(LOCKBOSS, (120, 120))
RESIZED_BACK = pygame.image.load("images/resized_back.png")


# Main Colours
gold1 = (230, 224, 174)
gold2 = (223, 188, 94)
red1 = (238, 97, 70)
red2 = (215, 60, 55)
red3 = (181, 31, 9)

# Secondary Colours
green1 = (116, 217, 219)
green2 = (153, 216, 196)
green3 = (113, 182, 135)
green4 = (88, 133, 120)
green5 = (117, 132, 133)

def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

def get_font(font, size):
    """
    Loads and returns a Pygame font object based on a given font name and size.

    Parameters:
    - font (str): A string representing the font name. If the font is "Sawarabi" or "Shojumaru",
            a specific font fle is loaded
    - size (int): The size of the font in points

    Returns:
    A Pygame font object.
    """
    if font == "Sawarabi":
        return pygame.font.Font("fonts/SawarabiMincho-Regular.ttf", size)
    elif font == "Shojumaru":
        return pygame.font.Font("fonts/Shojumaru-Regular.ttf", size)

def load_map(username, password):
  player = Player(username, password)
  player.load_player()

  run = True
  no_entry = False
  while run:

    MULTTEMP = Button(pygame.image.load("images/templeright.png"), pos = (600, 131), text_input = "", font = get_font("Shojumaru", 15), base_colour = "White", hovering_colour = "#b51f09")
    TOPTEMP = Button(pygame.image.load("images/templetop.png"), pos = (372, 32), text_input = "", font = get_font("Shojumaru", 15), base_colour = "White", hovering_colour = "#b51f09")
    MIDTEMP = Button(pygame.image.load("images/templemiddle.png"), pos = (350, 220), text_input = "", font = get_font("Shojumaru", 15), base_colour = "White", hovering_colour = "#b51f09")
    LOCKTEMP = Button(RESIZED_LOCKBOSS, pos = (342, 203), text_input = "", font = get_font("Shojumaru", 15), base_colour = "White", hovering_colour = "#b51f09")
    BOTTEMP = Button(RESIZED_MIDDLETEMP, pos = (340, 352), text_input = "", font = get_font("Shojumaru", 15), base_colour = "White", hovering_colour = "#b51f09")
    LEFTTEMP = Button(pygame.image.load("images/templeleft.png"), pos = (160, 160), text_input="", font=get_font("Shojumaru", 15), base_colour="White", hovering_colour="#b51f09")

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
    
    # Draw the background image onto the screen
    if int(player.get_add()) and int(player.get_sub()) and int(player.get_mul()) and int(player.get_div()) == (int(player.get_bosses()) + 1) * 5:
       screen.blit(BACKGROUND, (0, 0))
    else:
       screen.blit(LOCK_BACKGROUND, (0, 0))

    # Get the current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    MOUSE_POS = pygame.mouse.get_pos()
    

    Back_Button = Button(pygame.image.load("images/back_button.png"), pos = (70, 55), text_input = "", font = get_font("Shojumaru", 15), base_colour = "White", hovering_colour = "#b51f09")
    Back_Button.update(screen)

    # go back
    if (40<mouse_x<75 and 40<mouse_y<70):
        screen.blit(RESIZED_BACK, (-90,-96))
        if event.type == pygame.MOUSEBUTTONDOWN:
          if Back_Button.checkInput(MOUSE_POS):
            return
          
    # cooking game
    if (133<mouse_x<180 and 139<mouse_y<202):
      screen.blit(RESIZED_LEFTTEMP, (110, 92))
      if event.type == pygame.MOUSEBUTTONDOWN:
         if LEFTTEMP.checkInput(MOUSE_POS):
            pygame.mixer.music.stop()
            cooking_game(username, password)
            play_music("sound/EDM.mp3")


    # snake game
    if (372<mouse_x<419 and 32<mouse_y<95):
      screen.blit(RESIZED_TOPTEMP, (348, -2))
      if event.type == pygame.MOUSEBUTTONDOWN:
         if TOPTEMP.checkInput(MOUSE_POS):
            pygame.mixer.music.stop()
            snakeSums(username, password)
            play_music("sound/EDM.mp3")
    
    # running army
    if (600<mouse_x<647 and 131<mouse_y<194):
      screen.blit(RESIZED_MULTTEMP, (582, 90))
      if event.type == pygame.MOUSEBUTTONDOWN:
        if MULTTEMP.checkInput(MOUSE_POS):
            pygame.mixer.music.stop()
            running_army(username, password)
            play_music("sound/EDM.mp3")
    
    # sandwich stack game
    if (363<mouse_x<410 and 383<mouse_y<446):
      screen.blit(RESIZED_BOTTOMTEMP, (340, 352))
      if event.type == pygame.MOUSEBUTTONDOWN:
         if BOTTEMP.checkInput(MOUSE_POS):
            pygame.mixer.music.stop()
            sandwich_stack(username, password)
            pygame.mixer.music.stop()
            play_music("sound/EDM.mp3")
    
    # boss battle (arithmetic emperor)
    if int(player.get_add()) and int(player.get_sub()) and int(player.get_mul()) and int(player.get_div()) == (int(player.get_bosses()) + 1) * 5:
      if (350<mouse_x<450 and 220<mouse_y<380):
        screen.blit(RESIZED_MIDDLETEMP, (360, 223))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if MIDTEMP.checkInput(MOUSE_POS):
              arithmetic_emperor(username, password)
    else:
       if (350<mouse_x<450 and 220<mouse_y<380):
        screen.blit(RESIZED_LOCKBOSS, (342, 203))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if LOCKTEMP.checkInput(MOUSE_POS):
              no_entry = True

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()
    mouse_x, mouse_y = mouse_pos

    font = get_font("Shojumaru", 20)
    name_surface = font.render(f"{player.get_name()}'s Game", True, "#a6d9db")
    add_surface = font.render(f"Addition: {player.get_add()}", True, "White")
    sub_surface = font.render(f"Subtraction: {player.get_sub()}", True, "White")
    mul_surface = font.render(f"Multiplication: {player.get_mul()}", True, "White")
    div_surface = font.render(f"Division: {player.get_mul()}", True, "White")
    screen.blit(name_surface, (550, 15))
    screen.blit(add_surface, (550, 35))
    screen.blit(sub_surface, (550, 55))
    screen.blit(mul_surface, (550, 75))
    screen.blit(div_surface, (550, 95))

    if no_entry:
      font = get_font('Shojumaru', 18)
      text_surface = font.render(f'Your ability powers', True, "White")
      text2_surface = font.render(f'must be level {str((int(player.get_bosses()) + 1) * 5)} to enter.', True, 'white')
      screen.blit(text_surface, (20, 545))
      screen.blit(text2_surface, (20, 565))
    
    pygame.display.update()

  pygame.quit()

username = "jocelyn"
password = 12345678
load_map(username, password)

'''    # Display mouse position on the screen
    font = pygame.font.Font(None, 36)
    text = font.render(f"Mouse Position: ({mouse_x}, {mouse_y})", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    # Update the display
    Back_Button.update(screen)'''
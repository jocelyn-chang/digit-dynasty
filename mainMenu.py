import pygame

pygame.init()

# creates game window
screen_width = 1000
height = 600
win = pygame.display.set_mode((screen_width, height))
pygame.display.set_caption('DINO GAME')

# colours
green = (0, 154, 23)
blue = (135, 206, 235)
yellow = (255, 239, 0)
white = (255, 255, 255)


def main():
    run = True

   # this function redraws the playing window each frame
    def redraw_window():

        win.fill(BLUE)
        pygame.draw.rect(win, GREEN, (0, 550, 1000, 50))

        # update the screen
        pygame.display.update()

    while run:
        redraw_window()

    pygame.quit()

import pygame

#Initialize PyGame
pygame.init()

#Create the Screen
screen = pygame.display.set_mode((800,600))

#Title and Loop
pygame.display.set_caption("Digit Dynasty")
icon = pygame.image.load('images/game_icon.png')
pygame.display.set_icon(icon)


#Crete Button
button_width, button_height = 200, 100
button_color = (255, 0, 0)  # Red color
button_surface = pygame.Surface((button_width, button_height))
button_surface.fill(button_color)

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    screen.blit(button_surface, (200, 200)) 

    pygame.display.update()

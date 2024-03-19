import pygame, sys

# Button class for image-based buttons
class Button():
    def __init__(self, image = None, pos = (0,0), text_input = "", font = 0, base_colour = "Black", hovering_colour = "White"):
        if isinstance(image, str):
            self.image = pygame.image.load(image)
        else:
            self.image = image
        self.x_pos, self.y_pos = pos
        self.font = font
        self.base_colour, self.hovering_colour = base_colour, hovering_colour
        self.text_input = text_input
        if self.font:
            self.text = self.font.render(self.text_input, True, pygame.Color(self.base_colour))
        else:
            self.text = None
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        if self.text:
            text_rect = self.text.get_rect(center = self.rect.center)
            screen.blit(self.text, text_rect)

            # Shadow offset
            shadow_offset = 2

            # Draw shadow first
            shadow_color = (135, 135, 135)  # Black shadow
            shadow_text = self.font.render(self.text_input, True, shadow_color)
            shadow_rect = shadow_text.get_rect(center=(self.rect.centerx + shadow_offset, self.rect.centery + shadow_offset))
            screen.blit(shadow_text, shadow_rect)

            # Draw the actual text
            screen.blit(self.text, text_rect)

    def checkInput(self, position):
        return self.rect.collidepoint(position)
    
    def changeColour(self, position):
        if self.rect.collidepoint(position):
            if self.font:
                self.text = self.font.render(self.text_input, True, pygame.Color(self.hovering_colour))
            else:
                if self.font:
                    self.text = self.font.render(self.text_input, True, pygame.Color(self.base_colour))
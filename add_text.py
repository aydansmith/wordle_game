import pygame
import sys

# rgb colors
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)

# font text is from https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
# learned how to do text in pygame and based code off of https://stackoverflow.com/questions/10467863/how-to-remove-replace-text-in-pygame
# adds text to top of screen
def add_text(screen, text):
    # fills the screen black in the area wanted so that previous text doesn't show up still
    screen.fill(BLACK, (0, 0, 600, 90))
    font = pygame.font.Font('freesansbold.ttf', 50)
    text = font.render(text, True, WHITE)
    textRect = text.get_rect()
    textRect.center = (300, 50)
    screen.blit(text, textRect)

def add_text_to_rectangle(screen, rect, text):
    x = rect.x
    y = rect.y
    width = rect.width
    height = rect.height
    centerX = x + (width/2)
    centerY = y + (height/2)
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(text, True, WHITE)
    textRect = text.get_rect()
    textRect.center = (centerX, centerY)
    screen.blit(text, textRect)
    
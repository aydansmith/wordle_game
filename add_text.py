from turtle import clear
import pygame
import sys

# rgb colors
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)

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

# take rectangle object and put text in center
def add_text_to_rectangle(screen, rect, text):
    x = rect.x # get x from rect
    y = rect.y # get y from rect
    width = rect.width # get width
    height = rect.height # get height
    centerX = x + (width/2) #calculate center x and center y
    centerY = y + (height/2)
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(text, True, WHITE)
    textRect = text.get_rect()
    textRect.center = (centerX, centerY)
    screen.blit(text, textRect) # put text at center of rectangle

def remove_text_from_rectangle(screen, rect):
    screen.fill(BLACK, (rect.x + 2, rect.y + 2, rect.width - 6, rect.height - 6))

def add_message(screen, text):
    # fills the screen black in the area wanted so that previous text doesn't show up still
    clear_message(screen)
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(text, True, RED)
    textRect = text.get_rect()
    textRect.center = (300, 80)
    screen.blit(text, textRect)

def clear_message(screen):
    screen.fill(BLACK, (0, 70, 600, 20))
    
# File Name: add_text.py
# Description: add_text handles any and all prinitng of text to the screen
# Date Created: 4/12/22
# Date Edited: 4/19/22
# Last Revision: Aydan added in ability to print tests
# Author: Aydan Smith

from turtle import clear
import pygame
import sys

# rgb colors
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)

# add_text displays text at the top of the screen
# preconditions: screen is pygame object, text is string to display at top
# postconditions: text is displayed at top of screen
# side effects: screen gets updated
# invariants: none
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

# add_text_to_rectangle displays text at center of rect
# preconditions: screen is pygame object, rect is a Rectangle object, text is string to display at top
# postconditions: text is displayed at center of the rectangle
# side effects: screen gets updated
# invariants: none
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

# remove_text_from_rectangle removes text from rect
# preconditions: screen is pygame object, rect is Rectangle object
# postconditions: text is removed from rect
# side effects: screen gets updated
# invariants: none
def remove_text_from_rectangle(screen, rect):
    screen.fill(BLACK, (rect.x + 2, rect.y + 2, rect.width - 6, rect.height - 6))


# add_message displays text at the top of the screen
# preconditions: screen is pygame object, text is string to display at top
# postconditions: text is displayed at top of screen
# side effects: screen gets updated
# invariants: none
def add_message(screen, text):
    # fills the screen black in the area wanted so that previous text doesn't show up still
    clear_message(screen)
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(text, True, RED)
    textRect = text.get_rect()
    textRect.center = (300, 80) # center of rectangle
    screen.blit(text, textRect) # display text


# clear_message removes text from top of screen
# preconditions: screen is pygame object
# postconditions: text is removed from top of screen
# side effects: screen gets updated
# invariants: none
def clear_message(screen):
    screen.fill(BLACK, (0, 70, 600, 20))


# add_tests displays data from tests.txt file
# preconditions: screen is pygame object, tests.txt is occupied
# postconditions: tests get displayed to screen
# side effects: screen gets updated
# invariants: none
def add_tests(screen):
    # open tests.txt
    with open('tests.txt') as f:
        lines = f.readlines()
        f.close() 
    font = pygame.font.Font('freesansbold.ttf', 10) # set font
    text = "Our tests consist of every main feature that we have. We also performed significant visual testing" # summary
    y = 110 # initialize y
    text = font.render(text, True, WHITE)
    textRect = text.get_rect()
    textRect.center = (300, y)
    screen.blit(text, textRect) # print initial summary
    y = y + 25
    # loop through tests
    for x in lines:
        # format the test
        x = x.strip() # remove new line from end and beginning
        text = font.render(x, True, WHITE)
        textRect = text.get_rect()
        textRect.center = (300, y)
        screen.blit(text, textRect) # display the test
        y = y + 25 # update y
    
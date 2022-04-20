# File Name: display_tests.py
# Description: the screen function displays the tests. It calls
# the add_text file to print out all the tests after getting tests from test.py
# if you click anywhere you go to home screen
# Date Created: 4/19/22
# Date Edited: 4/19/22
# Last Revision: Aydan added in ability to call add_text to print tests
# Author: Aydan Smith

from audioop import add
from imp import reload
from itertools import count
import pygame
import sys
import random
from scipy import rand
import add_text
import words
import main
import test
import HomePage
#colors in RGB form

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
YELLOW = (201, 148, 48)
GREEN = (14, 135, 48)

# height of window for pygame
WINDOW_HEIGHT = 600
#width of window for pygame
WINDOW_WIDTH = 600
#initializes screen in pygame
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CAPTION = pygame.display.set_caption("Wordle")

# screen handles all the logic for displaying the tests to the user
# on a click, the user gets returned to home screen
# preconditions: pygame object is created
# postconditions: user is shown the tests and returned to home screen when they want
# side effects: none
# invariants: none
def screen():
    # following code is inspired and similar to thread on creating a grid for a snake game in pygane
    # https://stackoverflow.com/questions/33963361/how-to-make-a-grid-in-pygame
    global SCREEN, CLOCK
    # initializes pygame
    pygame.init()
    # creates clock in pygame
    CLOCK = pygame.time.Clock()
    #fill screen to black
    SCREEN.fill(BLACK)
    # adds Tests to top of screen
    add_text.add_text(SCREEN, "Tests")
    add_text.add_message(SCREEN, "Click anywhere to exit to home screen") # let user know how to get to home page
    add_text.add_tests(SCREEN)
    #pygame.draw.rect(SCREEN, GREEN, rect, 1)
    pygame.display.update()
    while True:
        pos = pygame.mouse.get_pos() # gets the position of the mouse
        pygame.display.update()
        for event in pygame.event.get():
                # if the user wants to quit, close pygame
                # if the user clicks, we respond accordingly
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # on a click reimport HomePage
                    reload(HomePage)
                    HomePage.screen() # navigate back to home page
    

# so that each import does not call main function
if __name__ == "__main__":
    screen()
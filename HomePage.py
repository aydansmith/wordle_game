from imp import reload
from itertools import count
import pygame
import sys
import random
from scipy import rand
import add_text
import words
import main
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

# screen will print two boxes, one for testing and one for playing the game
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
    # adds wordle to top of screen
    add_text.add_text(SCREEN, "Welcome To Wordle")
    rect = pygame.Rect(150, 200, 300, 60)
    pygame.draw.rect(SCREEN, WHITE, rect, 1)
    rect2 = pygame.Rect(150, 290, 300, 60)
    pygame.draw.rect(SCREEN, WHITE, rect2, 1)
    image = pygame.display.get_surface()
    image.fill(YELLOW, rect)
    add_text.add_text_to_rectangle(SCREEN, rect, 'Play Wordle')
    image = pygame.display.get_surface()
    image.fill(YELLOW, rect2)
    add_text.add_text_to_rectangle(SCREEN, rect2, 'Run Tests')
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
                    if rect.collidepoint(pos):
                        reload(main)
                        main.main()
    

# so that each import does not call main function
if __name__ == "__main__":
    screen()
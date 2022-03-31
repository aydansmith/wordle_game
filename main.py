import pygame
import sys
import add_text
#colors in RGB form

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
YELLOW = (255, 196, 37)
GREEN = (50, 205, 50)

# height of window for pygame
WINDOW_HEIGHT = 600
#width of window for pygame
WINDOW_WIDTH = 600
#initializes screen in pygame
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CAPTION = pygame.display.set_caption("Wordle")


ROW_1 = []
ROW_2 = []
ROW_3 = []
ROW_4 = []
ROW_5 = []
ROW_6 = []

ALPHABET_ORDER = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'ENTER', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'BACK']
ALPHABET = []

# main handles all the logic and passing between files
def main():

    # following code is inspired and similar to thread on creating a grid for a snake game in pygane
    # https://stackoverflow.com/questions/33963361/how-to-make-a-grid-in-pygame
    global SCREEN, CLOCK
    # initializes pygame
    pygame.init()
    # creates clock in pygame
    CLOCK = pygame.time.Clock()
    #fill screen to black
    SCREEN.fill(BLACK)
    add_text.add_text(SCREEN, "Wordle")
    createBoxesForGuesses()
    fillAlphabet()
    printAlphabet()
    while True:
        pos = pygame.mouse.get_pos()
        printBoxesForGuesses()
        pygame.display.update()
        for event in pygame.event.get():
                # if the user wants to quit, close pygame
                # if the user clicks, we respond accordingly
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



def createBoxesForGuesses():
    fillRowOne()
    fillRowTwo()
    fillRowThree()
    fillRowFour()
    fillRowFive()
    fillRowSix

def printBoxesForGuesses():
    printRowOne()
    printRowTwo()
    printRowThree()
    printRowFour()
    printRowFive()
    printRowSix()

def fillRowOne():
    blockSize = 40 # set blcok size
    x = 180 # initial x
    y = 100 # constant y
    # we will add 4 blocks
    for count in range(0,5):
        rect = pygame.Rect(x, y, blockSize, blockSize) # create rectangle 
        ROW_1.append(rect) # add rectangle to row
        x = x + 50 # update x

def fillRowTwo():
    blockSize = 40 # set blcok size
    x = 180 # initial x
    y = 150 # constant y
    # we will add 4 blocks
    for count in range(0,5):
        rect = pygame.Rect(x, y, blockSize, blockSize) # create rectangle 
        ROW_2.append(rect) # add rectangle to row
        x = x + 50 # update x

def fillRowThree():
    blockSize = 40 # set blcok size
    x = 180 # initial x
    y = 200 # constant y
    # we will add 4 blocks
    for count in range(0,5):
        rect = pygame.Rect(x, y, blockSize, blockSize) # create rectangle 
        ROW_3.append(rect) # add rectangle to row
        x = x + 50 # update x

def fillRowFour():
    blockSize = 40 # set blcok size
    x = 180 # initial x
    y = 250 # constant y
    # we will add 4 blocks
    for count in range(0,5):
        rect = pygame.Rect(x, y, blockSize, blockSize) # create rectangle 
        ROW_4.append(rect) # add rectangle to row
        x = x + 50 # update x

def fillRowFive():
    blockSize = 40 # set blcok size
    x = 180 # initial x
    y = 300 # constant y
    # we will add 4 blocks
    for count in range(0,5):
        rect = pygame.Rect(x, y, blockSize, blockSize) # create rectangle 
        ROW_5.append(rect) # add rectangle to row
        x = x + 50 # update x

def fillRowSix():
    blockSize = 40 # set blcok size
    x = 180 # initial x
    y = 350 # constant y
    # we will add 4 blocks
    for count in range(0,5):
        rect = pygame.Rect(x, y, blockSize, blockSize) # create rectangle 
        ROW_6.append(rect) # add rectangle to row
        x = x + 50 # update x

def printRowOne():
    # prints each rectangle in row array
    for x in ROW_1:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

def printRowTwo():
    # prints each rectangle in row array
    for x in ROW_2:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

def printRowThree():
    # prints each rectangle in row array
    for x in ROW_3:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

def printRowFour():
    # prints each rectangle in row array
    for x in ROW_4:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

def printRowFive():
    # prints each rectangle in row array
    for x in ROW_5:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

def printRowSix():
    # prints each rectangle in row array
    for x in ROW_6:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

def fillAlphabet():
    blockWidth = 30 
    blockHeight = 40
    x = 105
    y = 420
    for count in range (0, 10):
        rect = pygame.Rect(x, y, blockWidth, blockHeight)
        ALPHABET.append(rect)
        x = x + 40
    x = 125
    y = 470
    for count in range (0, 9):
        rect = pygame.Rect(x, y, blockWidth, blockHeight)
        ALPHABET.append(rect)
        x = x + 40
    x = 105
    y = 520
    rect = pygame.Rect(x, y, 50, blockHeight)
    ALPHABET.append(rect)
    x = x + 60
    for count in range (0, 7):
        rect = pygame.Rect(x, y, blockWidth, blockHeight)
        ALPHABET.append(rect)
        x = x + 40
    rect = pygame.Rect(x, y, 50, blockHeight)
    ALPHABET.append(rect)

def printAlphabet():
    counter = 0
    for x in ALPHABET:
        add_text.add_text_to_rectangle(SCREEN, x, ALPHABET_ORDER[counter])
        counter = counter + 1
    for x in ALPHABET:
        pygame.draw.rect(SCREEN, WHITE, x, 1)


# so that each import does not call main function
if __name__ == "__main__":
    main()

import pygame
import sys
import random
from scipy import rand
import add_text
import words
#colors in RGB form

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
YELLOW = (255, 196, 37)
GREEN = (14, 135, 48)

# height of window for pygame
WINDOW_HEIGHT = 600
#width of window for pygame
WINDOW_WIDTH = 600
#initializes screen in pygame
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CAPTION = pygame.display.set_caption("Wordle")

# the rows will store the rectangle objects for the guesses of the words
ROW_1 = []
ROW_2 = []
ROW_3 = []
ROW_4 = []
ROW_5 = []
ROW_6 = []
currentWord = []
# alphabet appears on keyboard in this manner
ALPHABET_ORDER = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'ENTER', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'BACK']
ALPHABET = [] # will store rectangle objects for alphabet
# main handles all the logic and passing between files
def main():
    wordGuessCount = 0
    wordLetterCount = 0
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
    add_text.add_text(SCREEN, "Wordle")
    # call all the functions to get the boxes for guess, boxes for alphabet, and put the alphabet on the boxes
    createBoxesForGuesses()
    printBoxesForGuesses()
    fillAlphabet()
    printAlphabet()
    word = getWord()
    print(word)
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
                    letterIndex = getLetter(pos)
                    if letterIndex != -1:
                        letter = ALPHABET_ORDER[letterIndex]
                        if letter != 'ENTER' and letter != 'BACK':
                            data = AddLetter(letter, wordLetterCount, wordGuessCount, False)
                            wordLetterCount = data[0]
                            wordGuessCount = data[1]
                            pygame.display.update()
                        elif letter == 'ENTER':
                            if wordLetterCount == 5:
                                print(word)
                                data = OnEnter(wordLetterCount, wordGuessCount, word)
                                wordLetterCount = data[0]
                                wordGuessCount = data[1]
                                pygame.display.update()

def AddLetter(letter, wordLetterCount, wordGuessCount, testing):
    if wordLetterCount != 5:
        arrayToWrite = getGuessArray(wordGuessCount)
        if not testing:
            add_text.add_text_to_rectangle(SCREEN, arrayToWrite[wordLetterCount], letter)
        currentWord.append(letter)
        wordLetterCount = wordLetterCount + 1
    return(wordLetterCount, wordGuessCount)

def OnEnter(wordLetterCount, wordGuessCount, word):
    currentArray = getGuessArray(wordGuessCount)
    for x in range(0, 5):
        rect = currentArray[x]
        currentLetter = currentWord[x].lower()
        letterInWord = word[x].lower()
        if currentLetter == letterInWord:
            image = pygame.display.get_surface()
            image.fill(GREEN, rect)
            add_text.add_text_to_rectangle(SCREEN, rect, letterInWord.upper())
            #pygame.draw.rect(SCREEN, GREEN, rect, 1)
            pygame.display.update()
    wordLetterCount = 0
    wordGuessCount = wordGuessCount + 1
    currentWord.clear()
    return(wordLetterCount, wordGuessCount)

# returns array to write to based on wordGuessCount    
def getGuessArray(wordGuessCount):
    if wordGuessCount == 0:
        return ROW_1
    elif wordGuessCount == 1:
        return ROW_2
    elif wordGuessCount == 2:
        return ROW_3
    elif wordGuessCount == 3:
        return ROW_4
    elif wordGuessCount == 4:
        return ROW_5
    elif wordGuessCount == 5:
        return ROW_6

# gets letter that was clicked on by returning index
# returns -1 if you didn't click a letter    
def getLetter(pos):
    counter = 0
    for x in ALPHABET:
        if x.collidepoint(pos):
            return counter
        counter = counter+1
    return(-1)
    
#generates word that will be solution
def getWord():
    letter = 'ENTER' # start at enter so that our loop will run
    while letter == 'ENTER' or letter == 'BACK':
        letter = random.randint(0,27) # generate a random starting letter
        letter = ALPHABET_ORDER[letter]
    letter = letter.lower()
    length = len(words.allowedSolutions[letter]) # get number of possible words starting with that letter
    index = random.randint(0, length-1) # generate which word index to use
    word = words.allowedSolutions[letter][index] # get word
    return word # return word
# calls the functions to fill each ROW array with rectangle objects
def createBoxesForGuesses():
    fillRowOne()
    fillRowTwo()
    fillRowThree()
    fillRowFour()
    fillRowFive()
    fillRowSix()
# prints the rectangles in the ROW arrays
def printBoxesForGuesses():
    printRowOne()
    printRowTwo()
    printRowThree()
    printRowFour()
    printRowFive()
    printRowSix()

# fills ROW_1 array with rectangles
def fillRowOne():
    blockSize = 40 # set blcok size
    x = 180 # initial x
    y = 100 # constant y
    # we will add 4 blocks
    for count in range(0,5):
        rect = pygame.Rect(x, y, blockSize, blockSize) # create rectangle 
        ROW_1.append(rect) # add rectangle to row
        x = x + 50 # update x

# fills ROW_2 array with rectangles
def fillRowTwo():
    blockSize = 40 # set blcok size
    x = 180 # initial x
    y = 150 # constant y
    # we will add 4 blocks
    for count in range(0,5):
        rect = pygame.Rect(x, y, blockSize, blockSize) # create rectangle 
        ROW_2.append(rect) # add rectangle to row
        x = x + 50 # update x

# fills ROW_3 array with rectangles
def fillRowThree():
    blockSize = 40 # set blcok size
    x = 180 # initial x
    y = 200 # constant y
    # we will add 4 blocks
    for count in range(0,5):
        rect = pygame.Rect(x, y, blockSize, blockSize) # create rectangle 
        ROW_3.append(rect) # add rectangle to row
        x = x + 50 # update x

# fills ROW_4 array with rectangles
def fillRowFour():
    blockSize = 40 # set blcok size
    x = 180 # initial x
    y = 250 # constant y
    # we will add 4 blocks
    for count in range(0,5):
        rect = pygame.Rect(x, y, blockSize, blockSize) # create rectangle 
        ROW_4.append(rect) # add rectangle to row
        x = x + 50 # update x

# fills ROW_5 array with rectangles
def fillRowFive():
    blockSize = 40 # set blcok size
    x = 180 # initial x
    y = 300 # constant y
    # we will add 4 blocks
    for count in range(0,5):
        rect = pygame.Rect(x, y, blockSize, blockSize) # create rectangle 
        ROW_5.append(rect) # add rectangle to row
        x = x + 50 # update x

# fills ROW_6 array with rectangles
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
    # prints each rectangle in row 1 array
    for x in ROW_1:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

def printRowTwo():
    # prints each rectangle in row 2 array
    for x in ROW_2:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

def printRowThree():
    # prints each rectangle in row 3 array
    for x in ROW_3:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

def printRowFour():
    # prints each rectangle in row 4 array
    for x in ROW_4:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

def printRowFive():
    # prints each rectangle in row 5 array
    for x in ROW_5:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

def printRowSix():
    # prints each rectangle in row 6 array
    for x in ROW_6:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

# creates the blocks for the alphabet boxes
def fillAlphabet():
    blockWidth = 30 # set block width
    blockHeight = 40 # set block height
    x = 105 #initial x
    y = 420 #initial y
    # loops to create first row of alphabet
    for count in range (0, 10):
        rect = pygame.Rect(x, y, blockWidth, blockHeight)
        ALPHABET.append(rect)
        x = x + 40
    x = 125 # new x
    y = 470 # new y
    # sevcond row of alphabet
    for count in range (0, 9):
        rect = pygame.Rect(x, y, blockWidth, blockHeight)
        ALPHABET.append(rect)
        x = x + 40
    x = 105 #new x
    y = 520 #new y
    # ENTER box
    rect = pygame.Rect(x, y, 50, blockHeight)
    ALPHABET.append(rect)
    x = x + 60
    # third alphabet row
    for count in range (0, 7):
        rect = pygame.Rect(x, y, blockWidth, blockHeight)
        ALPHABET.append(rect)
        x = x + 40
    # BACK box
    rect = pygame.Rect(x, y, 50, blockHeight)
    ALPHABET.append(rect)

# prints all the alphabet characters that are stored in order in ALPHABET_ORDER
def printAlphabet():
    counter = 0
    for x in ALPHABET:
        add_text.add_text_to_rectangle(SCREEN, x, ALPHABET_ORDER[counter])
        counter = counter + 1
    for x in ALPHABET:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

def getCurrentWord():
    wordTemp = ""
    for x in range(0, len(currentWord)):
        wordTemp = wordTemp + currentWord[x]
    return wordTemp

# so that each import does not call main function
if __name__ == "__main__":
    main()

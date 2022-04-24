# File Name: main.py
# Description: the main function is what is called to run the wordle game.
# This file is used to run the game and contains all of the logic.
# Any logic that requires text to be displayed uses add_text.py
# Date Created: 4/9/22
# Date Edited: 4/19/22
# Last Revision: Aydan updated the onBack() function to have a testing parameter
# Author: Aydan Smith

from itertools import count
from matplotlib.pyplot import pause
import pygame
import sys
import random
from scipy import rand
import add_text
import words
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

# the rows will store the rectangle objects for the guesses of the words
ROW_1 = []
ROW_2 = []
ROW_3 = []
ROW_4 = []
ROW_5 = []
ROW_6 = []
# stores the letters from the current guess
currentWord = []
# alphabet appears on keyboard in this manner
ALPHABET_ORDER = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'ENTER', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'BACK']
ALPHABET = [] # will store rectangle objects for alphabet

# main handles all the logic and passing between files
# preconditions: none
# postconditions: pygame has exited and user game is over
# side effects: pygame gets called
# invariants: while loop runs til user clicks exit
def main():
    wordGuessCount = 0 # how many guesses the user has tried
    wordLetterCount = 0 # how many letters have been guessed for the most recent
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
    # gets random word for hash tables
    word = getWord()
    # prints word to console for testing
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
                elif event.type == pygame.KEYDOWN:
                    # based on https://www.geeksforgeeks.org/how-to-get-keyboard-input-in-pygame/
                    # if the key is an 'A' then call AddLetter with that
                    if event.key == pygame.K_a:
                        data = AddLetter('a', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_b:
                        # if the key is an 'B' then call AddLetter with that
                        data = AddLetter('b', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_c:
                        # if the key is an 'C' then call AddLetter with that
                        data = AddLetter('c', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_d:
                        # if the key is an 'D' then call AddLetter with that
                        data = AddLetter('d', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_e:
                        # if the key is an 'E' then call AddLetter with that
                        data = AddLetter('e', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_f:
                        # if the key is an 'F' then call AddLetter with that
                        data = AddLetter('f', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_g:
                        # if the key is an 'G' then call AddLetter with that
                        data = AddLetter('g', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_h:
                        # if the key is an 'H' then call AddLetter with that
                        data = AddLetter('h', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_i:
                        # if the key is an 'I' then call AddLetter with that
                        data = AddLetter('i', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_j:
                        # if the key is an 'J' then call AddLetter with that
                        data = AddLetter('j', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_k:
                        # if the key is an 'K' then call AddLetter with that
                        data = AddLetter('k', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_l:
                        # if the key is an 'L' then call AddLetter with that
                        data = AddLetter('l', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_m:
                        # if the key is an 'M' then call AddLetter with that
                        data = AddLetter('m', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_n:
                        # if the key is an 'N' then call AddLetter with that
                        data = AddLetter('n', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_o:
                        # if the key is an 'O' then call AddLetter with that
                        data = AddLetter('o', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_p:
                        # if the key is an 'P' then call AddLetter with that
                        data = AddLetter('p', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_q:
                        # if the key is an 'Q' then call AddLetter with that
                        data = AddLetter('q', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_r:
                        # if the key is an 'R' then call AddLetter with that
                        data = AddLetter('r', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_s:
                        # if the key is an 'S' then call AddLetter with that
                        data = AddLetter('s', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_t:
                        # if the key is an 'T' then call AddLetter with that
                        data = AddLetter('t', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_u:
                        # if the key is an 'U' then call AddLetter with that
                        data = AddLetter('u', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_v:
                        # if the key is an 'V' then call AddLetter with that
                        data = AddLetter('v', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_w:
                        # if the key is an 'W' then call AddLetter with that
                        data = AddLetter('w', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_x:
                        # if the key is an 'X' then call AddLetter with that
                        data = AddLetter('x', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_y:
                        # if the key is an 'Y' then call AddLetter with that
                        data = AddLetter('y', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_z:
                        # if the key is an 'Z' then call AddLetter with that
                        data = AddLetter('z', wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0]
                        wordGuessCount = data[1]
                        pygame.display.update()
                    if event.key == pygame.K_RETURN:
                        # if ENTER is hit, check that you have 5 letters in the current guess
                        if wordLetterCount == 5:
                            data = OnEnter(wordLetterCount, wordGuessCount, word) # call the function meant to handle enters
                            # update counts
                            wordLetterCount = data[0]
                            wordGuessCount = data[1]
                            pygame.display.update() # update the screen
                        else:
                            add_text.add_message(SCREEN, "that is not a five letter word")
                    if event.key == pygame.K_BACKSPACE:
                        # if BACK is hit call the function for handling BACKspaces
                        data = onBack(wordLetterCount, wordGuessCount, False)
                        wordLetterCount = data[0] # update counts
                        wordGuessCount = data[1]
                        pygame.display.update() # update screen
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # get index of rectangle that was clicked
                    letterIndex = getLetter(pos)
                    if letterIndex != -1:
                        # use that index to get the letter
                        letter = ALPHABET_ORDER[letterIndex]
                        # if letter is not ENTER or BACK then try to add the letter and update word letter cound and word guess count
                        if letter != 'ENTER' and letter != 'BACK':
                            data = AddLetter(letter, wordLetterCount, wordGuessCount, False)
                            wordLetterCount = data[0]
                            wordGuessCount = data[1]
                            pygame.display.update()
                        elif letter == 'ENTER':
                            # if ENTER is hit, check that you have 5 letters in the current guess
                            if wordLetterCount == 5:
                                data = OnEnter(wordLetterCount, wordGuessCount, word) # call the function meant to handle enters
                                # update counts
                                wordLetterCount = data[0]
                                wordGuessCount = data[1]
                                pygame.display.update() # update the screen
                            else:
                                add_text.add_message(SCREEN, "that is not a five letter word")
                        elif letter == 'BACK':
                            # if BACK is hit call the function for handling BACKspaces
                            data = onBack(wordLetterCount, wordGuessCount, False)
                            wordLetterCount = data[0] # update counts
                            wordGuessCount = data[1]
                            pygame.display.update() # update screen
                        


# AddLetter handles all the logic for adding a letter to a guess
# preconditions: letter is a char of an alphabet character, wordLetterCount is an int and wordGuessCount is an int, and testing is a boolean
# postconditions: updated wordGuessCount and wordLetterCount get returned. Letter gets printed to screen 
# side effects: screen gets updated
# invariants: none
def AddLetter(letter, wordLetterCount, wordGuessCount, testing):
    add_text.clear_message(SCREEN) # clear the screen message
    # check that you have less than 5 letters
    if wordLetterCount != 5:
        # get array of rectangles based on word guess count
        arrayToWrite = getGuessArray(wordGuessCount)
        # update screen if you are not testing
        if not testing:
            add_text.add_text_to_rectangle(SCREEN, arrayToWrite[wordLetterCount], letter.upper())
        # add letter to current word
        currentWord.append(letter)
        wordLetterCount = wordLetterCount + 1 # update count
    return(wordLetterCount, wordGuessCount) # return counts

# OnBack handles all the logic for removing a letter
# preconditions: wordLetterCount is an int and wordGuessCount is an int, and testing is a boolean
# postconditions: updated wordGuessCount and wordLetterCount get returned. Letter gets removed from screen if guesses != 0
# side effects: screen gets updated
# invariants: none
def onBack(wordLetterCount, wordGuessCount, testing):
    if not testing:
        add_text.clear_message(SCREEN)
    if wordLetterCount != 0:
        arrayToWrite = getGuessArray(wordGuessCount)
        if not testing:
            add_text.remove_text_from_rectangle(SCREEN, arrayToWrite[wordLetterCount - 1])
        test = currentWord.pop()
        wordLetterCount = wordLetterCount - 1
    return(wordLetterCount, wordGuessCount)

# changeLetter handles all the logic for changing the color of a square on the keyboard
# preconditions: letter is the current letter and color is an RGB code
# postconditions: keyboard letter for letter gets changed to the color specified
# side effects: screen gets updated
# invariants: none
def changeLetter(letter, color):
    letter = letter.upper()
    counter = 0
    # get letter index
    for x in ALPHABET_ORDER:   
        if x == letter:
            break
        counter += 1
    rectangle = ALPHABET[counter] 
    image = pygame.display.get_surface()
    image.fill(color, rectangle)
    add_text.add_text_to_rectangle(SCREEN, rectangle, letter) 
# OnEnter handles all the logic for checking if a word is correct
# preconditions: wordLetterCount is an int and wordGuessCount is an int, and word is a string that is the correct word
# postconditions: updated wordGuessCount and wordLetterCount get returned. If the word is correct then the user is notified
# side effects: screen gets updated
# invariants: none
def OnEnter(wordLetterCount, wordGuessCount, word):
    lettersRead = [] # store the letters that have been guessed
    wordToTest = getCurrentWord() # get the current word
    # make sure it is a word
    if inWordList(wordToTest): 
        currentArray = getGuessArray(wordGuessCount) # get correct rectangles
        # loop through letter guesses
        for x in range(0, 5):
            rect = currentArray[x] # get rectangle to update
            currentLetter = currentWord[x].lower() # convert letter guess to lowercase for consistency
            letterInWord = word[x].lower() # get letter at that index of actual word
            # if letter is in right spot
            if currentLetter == letterInWord:
                # create image so that we can fill the rectangle
                image = pygame.display.get_surface()
                image.fill(GREEN, rect) # fill the rectangle gree
                add_text.add_text_to_rectangle(SCREEN, rect, letterInWord.upper()) # add letter to colored in rectangle
                lettersRead.append(currentLetter) # add letter to lettersRead
                changeLetter(currentLetter, GREEN)
                #pygame.draw.rect(SCREEN, GREEN, rect, 1)
                pygame.display.update()
            else:
                # otherwise check if it is the wrong spot
                isWrongSpot = inWrongSpot(currentLetter, lettersRead, word)
                if isWrongSpot:
                    # if it is wrong spot then fill rectangle yellow
                    image = pygame.display.get_surface()
                    image.fill(YELLOW, rect)
                    add_text.add_text_to_rectangle(SCREEN, rect, currentLetter.upper()) # add letter to rectangle
                    lettersRead.append(currentLetter)
                    changeLetter(currentLetter, YELLOW)
                    #pygame.draw.rect(SCREEN, GREEN, rect, 1)
                    pygame.display.update()
        wordLetterCount = 0 # reset wordLetterCount
        wordGuessCount = wordGuessCount + 1 # up your wordGuessCount
        # check for win
        if getCurrentWord().lower() == word.lower():
            if wordGuessCount == 1: 
                add_text.add_message(SCREEN, "Congrats, you got the word in " + str(wordGuessCount) + " try!") # print out congrats if user won
            else:
                add_text.add_message(SCREEN, "Congrats, you got the word in " + str(wordGuessCount) + " tries!") # print out congrats if user won
            pygame.display.update()
            pause(5) # pause
            HomePage.screen() # exit the game

        elif wordGuessCount == 6:
            add_text.add_message(SCREEN, "Sorry your ran out of attempts. Better luck next time!") # print out better luck next time if user lost
            pygame.display.update()
            pause(5) # pause
            HomePage.screen() # exit
        currentWord.clear() # clear current word
        return(wordLetterCount, wordGuessCount) # return count
    # if word is not valid, then notify the user and don't update your counts
    else:
        add_text.add_message(SCREEN, "That is not a valid word")
        return(wordLetterCount, wordGuessCount)


# inWrongSpot handles all the logic for checking if a letter is incorrectly place
# preconditions: currentLetter is the letter that you are checking, lettersRead is the letters already checked, word is the correct word
# postconditions: true is returned if letter is in wrong spot, false is returned otherwise
# side effects: none
# invariants: none
def inWrongSpot(currentLetter, lettersRead, word):
    countOfLetter = 0 # store letter appearances in word
    countOfLetterGuessed = 0 # store appearances in guess list
    # loop through word
    for i in range(0, len(word)):
        if word[i] == currentLetter:
            countOfLetter = countOfLetter + 1
    # loop through letters read
    for i in range(0, len(lettersRead)):
        if lettersRead[i] == currentLetter:
            countOfLetterGuessed = countOfLetterGuessed + 1
    # if letterCount > user guesses of that letter then return true
    if countOfLetter > countOfLetterGuessed:
        return True
    else:
        return False


# inWordList handles all the logic for checking if a word is valid
# preconditions: wordToTest is a string containing the word you want to check
# postconditions: bool is returned to tell you if the word is valid or not
# side effects: none
# invariants: none
def inWordList(wordToTest):
    # get first letter since that is hash key 
    firstLetter = wordToTest[0]
    firstLetter = firstLetter.lower() # convert to lower
    # get allowed solutions and allowed guesses
    allowedSolutions = words.allowedSolutions[firstLetter]
    allowedWords = words.allowedGuesses[firstLetter]
    # loop through them and check for the word
    # if the word is found then return true
    for x in allowedSolutions:
        if x == wordToTest.lower():
            return True
    for x in allowedWords:
        if x == wordToTest.lower():
            return True
    return False

# getGuessArray returns the correct array of guess rectangles based on wordGuessCount
# preconditions: wordGuessCount is an int between 0 and 5
# postconditions: correct array gets returned
# side effects: none
# invariants: none
# return -1 if it is an invalid wordGuessCount
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
    else:
        return(-1)

# getLetter returns the index for the correct letter based on position of click
# preconditions: pos is (x,y) coordinate
# postconditions: correct letter is returned or -1 is returned if not a letter
# side effects: none
# invariants: none
# gets letter that was clicked on by returning index
# returns -1 if you didn't click a letter    
def getLetter(pos):
    counter = 0
    for x in ALPHABET:
        if x.collidepoint(pos):
            return counter
        counter = counter+1
    return(-1)

# getWord returns the word that will be the solution
# preconditions: words.py is formatted correctly
# postconditions: word of the game is returned
# side effects: none
# invariants: none
#generates word that will be solution
def getWord():
    letter = 'ENTER' # start at enter so that our loop will run
    while letter == 'ENTER' or letter == 'BACK' or letter == 'X':
        letter = random.randint(0,27) # generate a random starting letter
        letter = ALPHABET_ORDER[letter]
    letter = letter.lower()
    length = len(words.allowedSolutions[letter]) # get number of possible words starting with that letter
    index = random.randint(0, length-1) # generate which word index to use
    word = words.allowedSolutions[letter][index] # get word
    return word # return word

# createBoxesForGuesses calls all the functions to fill the ROW arrays
# preconditions: none
# postconditions: boxes are filled with Rect objects
# side effects: none
# invariants: none
# calls the functions to fill each ROW array with rectangle objects
def createBoxesForGuesses():
    fillRowOne()
    fillRowTwo()
    fillRowThree()
    fillRowFour()
    fillRowFive()
    fillRowSix()

# printBoxesForGuesses calls all the functions to print the ROW arrays
# preconditions: boxes are already filled
# postconditions: boxes are printed out
# side effects: none
# invariants: none
# prints the rectangles in the ROW arrays
def printBoxesForGuesses():
    printRowOne()
    printRowTwo()
    printRowThree()
    printRowFour()
    printRowFive()
    printRowSix()

# fillRowOne creates rect objects for row 1
# preconditions: none
# postconditions: array is filled with rect objects
# side effects: none
# invariants: none
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

# fillRowTwo creates rect objects for row 2
# preconditions: none
# postconditions: array is filled with rect objects
# side effects: none
# invariants: none
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

# fillRowThree creates rect objects for row 3
# preconditions: none
# postconditions: array is filled with rect objects
# side effects: none
# invariants: none
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

# fillRowFour creates rect objects for row 4
# preconditions: none
# postconditions: array is filled with rect objects
# side effects: none
# invariants: none
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

# fillRowFive creates rect objects for row 5
# preconditions: none
# postconditions: array is filled with rect objects
# side effects: none
# invariants: none
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

# fillRowSix creates rect objects for row 6
# preconditions: none
# postconditions: array is filled with rect objects
# side effects: none
# invariants: none
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

# printRowOne prints rect objects for row 1
# preconditions: none
# postconditions: array of rect objects is displayed to screen
# side effects: none
# invariants: none
def printRowOne():
    # prints each rectangle in row 1 array
    for x in ROW_1:
        pygame.draw.rect(SCREEN, WHITE, x, 1)


# printRowTwo prints rect objects for row 2
# preconditions: none
# postconditions: array of rect objects is displayed to screen
# side effects: none
# invariants: none
def printRowTwo():
    # prints each rectangle in row 2 array
    for x in ROW_2:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

# printRowThree prints rect objects for row 3
# preconditions: none
# postconditions: array of rect objects is displayed to screen
# side effects: none
# invariants: none
def printRowThree():
    # prints each rectangle in row 3 array
    for x in ROW_3:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

# printRowFour prints rect objects for row 4
# preconditions: none
# postconditions: array of rect objects is displayed to screen
# side effects: none
# invariants: none
def printRowFour():
    # prints each rectangle in row 4 array
    for x in ROW_4:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

# printRowFive prints rect objects for row 5
# preconditions: none
# postconditions: array of rect objects is displayed to screen
# side effects: none
# invariants: none
def printRowFive():
    # prints each rectangle in row 5 array
    for x in ROW_5:
        pygame.draw.rect(SCREEN, WHITE, x, 1)


# printRowSix prints rect objects for row 6
# preconditions: none
# postconditions: array of rect objects is displayed to screen
# side effects: none
# invariants: none
def printRowSix():
    # prints each rectangle in row 6 array
    for x in ROW_6:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

# fillAlphabet fills alphabet array with rect objects 
# preconditions: none
# postconditions: array of rect objects is stored for alphabet
# side effects: none
# invariants: none
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

# printAlphabet prints rect objects for alphabet
# preconditions: alphabet exists
# postconditions: array of rect objects is displayed to screen
# side effects: none
# invariants: none
# prints all the alphabet characters that are stored in order in ALPHABET_ORDER
def printAlphabet():
    counter = 0
    for x in ALPHABET:
        add_text.add_text_to_rectangle(SCREEN, x, ALPHABET_ORDER[counter])
        counter = counter + 1
    for x in ALPHABET:
        pygame.draw.rect(SCREEN, WHITE, x, 1)

# getCurrentWord returns the string version of the chars stored in currentWord array
# preconditions: none
# postconditions: string of current guess is returned
# side effects: none
# invariants: none
def getCurrentWord():
    wordTemp = ""
    for x in range(0, len(currentWord)):
        wordTemp = wordTemp + currentWord[x]
    return wordTemp

# so that each import does not call main function
if __name__ == "__main__":
    main()

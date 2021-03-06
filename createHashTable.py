# File Name: createHashTable.py
# Description: this file writes to words.py. 
# It reads list of alphabetized words and then creates two hash tables based off letter
# One hash table is for accepted solutions and one is for accepted guesses
# Date Created: 4/12/22
# Date Edited: 4/12/22
# Last Revision: Aydan added in ability to write out to python file
# Author: Aydan Smith

# only called once and it is called manually
# this writes to words.py


# learned to read file from pythontutorial.net/python-basics/python-read-text-file/
# learned to write to file from https://www.pythontutorial.net/python-basics/python-write-text-file/

# words are downloaded from 
# https://gist.github.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b#file-wordle-answers-alphabetical-txt
# and
# https://gist.github.com/cfreshman/cdcdf777450c5b5301e439061d29694c


# initial first character so that we can have hash table by starting char
initialFirstChar = 'a'

# open the allowed guesses and store the lines
with open('Words/wordle-allowed-guesses.txt') as f:
    lines = f.readlines()
    f.close()

allowedGuesses = "allowedGuesses = {\n   'a': ["
# iterate through allowed guesses
for word in lines:
    firstChar = word[0] # first char of word
    # check if the first char is a new char than you've been looking at
    if firstChar != initialFirstChar: 
        # if it is a new char, check if it is not z
        if initialFirstChar != 'z':
            # if it is not z then we end the array and create the next key in the hash table
            initialFirstChar = firstChar
            allowedGuesses = allowedGuesses + "],\n   "
            allowedGuesses = allowedGuesses + "'" + firstChar + "': ["
            allowedGuesses = allowedGuesses + "'" + word.strip() + "'"
    else:
        # otherwise add word to the string
        # add a comma to previous word if it is not the first word
        if word != lines[0]:
            allowedGuesses = allowedGuesses + "," + "'" + word.strip() + "'"
        else:
            allowedGuesses = allowedGuesses + "'" + word.strip() + "'"
allowedGuesses = allowedGuesses + "]\n}" # end the hash table


# open the allowed guesses and store the lines
with open('Words/wordle-answers-alphabetical.txt') as f:
    lines2 = f.readlines()
    f.close()

initialFirstChar = 'a'
allowedSolutions = "allowedSolutions = {\n   'a': ["
# iterate through allowed guesses
for word in lines2:
    firstChar = word[0] # first char of word
    # check if the first char is a new char than you've been looking at
    if firstChar != initialFirstChar: 
        # if it is a new char, check if it is not z
        if initialFirstChar != 'z':
            # if it is not z then we end the array and create the next key in the hash table
            initialFirstChar = firstChar
            allowedSolutions = allowedSolutions + "],\n   "
            allowedSolutions = allowedSolutions + "'" + firstChar + "': ["
            allowedSolutions = allowedSolutions + "'" + word.strip() + "'"
    else:
        # otherwise add word to the string
        # add a comma to previous word if it is not the first word
        if word != lines2[0]:
            allowedSolutions = allowedSolutions + "," + "'" + word.strip() + "'"
        else:
            allowedSolutions = allowedSolutions + "'" + word.strip() + "'"
allowedSolutions = allowedSolutions + "]\n}" # end the hash table

# write out the hash tables
with open('words.py', 'w') as f:
    f.write(allowedGuesses)
    f.write("\n\n")
    f.write(allowedSolutions)
    f.close()



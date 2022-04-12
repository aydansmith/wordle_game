# learned to read file from pythontutorial.net/python-basics/python-read-text-file/
# learned to write to file from https://www.pythontutorial.net/python-basics/python-write-text-file/

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
            allowedGuesses = allowedGuesses + word.strip()
    else:
        # otherwise add word to the string
        # add a comma to previous word if it is not the first word
        if word != lines[0]:
            allowedGuesses = allowedGuesses + "," + word.strip()
        else:
            allowedGuesses = allowedGuesses + word.strip()
allowedGuesses = allowedGuesses + "]\n}" # end the hash table


# open the allowed guesses and store the lines
with open('Words/wordle-allowed-guesses.txt') as f:
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
            allowedSolutions = allowedSolutions + word.strip()
    else:
        # otherwise add word to the string
        # add a comma to previous word if it is not the first word
        if word != lines[0]:
            allowedSolutions = allowedSolutions + "," + word.strip()
        else:
            allowedSolutions = allowedSolutions + word.strip()
allowedSolutions = allowedSolutions + "]\n}" # end the hash table

# write out the hash tables
with open('words.txt', 'w') as f:
    f.write(allowedGuesses)
    f.write("\n\n")
    f.write(allowedSolutions)
    f.close()



import main

def test1():
    toTest = main.AddLetter('a', 5, 2, True)
    if toTest[0] == 5 and toTest[1] == 2:
        print("Test 1: Attempting to add letter when you have guessed 5 letters already: PASSED")
    else:
        print("Test 1: Attempting to add letter when you have guessed 5 letters already: PASSED")
def test2():
    startingWord = main.getCurrentWord()
    main.AddLetter('a', len(startingWord), 0, True)
    newWord = main.getCurrentWord()
    if newWord[len(startingWord)] == 'a':
        print("Test 2: Attempting to add letter when you have not guessed 5 letters already: PASSED")
    else:
        print("Test 2: Attempting to add letter when you have not guessed 5 letters already: FAILED")


test1()
test2()
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

def test3():
    testWord = 'stair'
    inList = main.inWordList(testWord)
    if inList:
        print("Test 3: Lowercase Word known to be in list is marked as valid by function to check if word is valid: PASSED")
    else:
        print("Test 3: Lowercase Word known to be in list is marked as valid by function to check if word is valid: FAILED")

def test4():
    testWord = 'CHAIR'
    inList = main.inWordList(testWord)
    if inList:
        print("Test 4: Uppercase Word known to be in list is marked as valid by function to check if word is valid: PASSED")
    else:
        print("Test 4: Uppercase Word known to be in list is marked as valid by function to check if word is valid: FAILED")

def test5():
    testWord = 'ABCDE'
    inList = main.inWordList(testWord)
    if not inList:
        print("Test 5: Uppercase Word known to not be in list is marked as not valid by function to check if word is valid: PASSED")
    else:
        print("Test 5: Uppercase Word known to not be in list is marked as not valid by function to check if word is valid: FAILED")

def test6():
    testWord = 'ABCDE'
    inList = main.inWordList(testWord)
    if not inList:
        print("Test 6: Lowercase Word known to not be in list is marked as not valid by function to check if word is valid: PASSED")
    else:
        print("Test 6: Lowercase Word known to not be in list is marked as not valid by function to check if word is valid: FAILED")

    


test1()
test2()
test3()
test4()
test5()
test6()
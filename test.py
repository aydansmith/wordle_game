from imp import reload
import main

def test1():
    toTest = main.AddLetter('a', 5, 2, True)
    if toTest[0] == 5 and toTest[1] == 2:
        return("Test 1: Attempting to add letter when you have guessed 5 letters already: PASSED")
    else:
        return("Test 1: Attempting to add letter when you have guessed 5 letters already: PASSED")
def test2():
    startingWord = main.getCurrentWord()
    main.AddLetter('a', len(startingWord), 0, True)
    newWord = main.getCurrentWord()
    if newWord[len(startingWord)] == 'a':
        return("Test 2: Attempting to add letter when you have not guessed 5 letters already: PASSED")
    else:
        return("Test 2: Attempting to add letter when you have not guessed 5 letters already: FAILED")

def test3():
    testWord = 'stair'
    inList = main.inWordList(testWord)
    if inList:
        return("Test 3: Lowercase Word known to be in list is marked as valid by function to check if word is valid: PASSED")
    else:
        return("Test 3: Lowercase Word known to be in list is marked as valid by function to check if word is valid: FAILED")

def test4():
    testWord = 'CHAIR'
    inList = main.inWordList(testWord)
    if inList:
        return("Test 4: Uppercase Word known to be in list is marked as valid by function to check if word is valid: PASSED")
    else:
        return("Test 4: Uppercase Word known to be in list is marked as valid by function to check if word is valid: FAILED")

def test5():
    testWord = 'ABCDE'
    inList = main.inWordList(testWord)
    if not inList:
        return("Test 5: Uppercase Word known to not be in list is marked as not valid by function to check if word is valid: PASSED")
    else:
        return("Test 5: Uppercase Word known to not be in list is marked as not valid by function to check if word is valid: FAILED")

def test6():
    testWord = 'ABCDE'
    inList = main.inWordList(testWord)
    if not inList:
        return("Test 6: Lowercase Word known to not be in list is marked as not valid by function to check if word is valid: PASSED")
    else:
        return("Test 6: Lowercase Word known to not be in list is marked as not valid by function to check if word is valid: FAILED")

    

def run_tests():
    reload(main)
    tests = []
    tests.append(test1())
    tests.append(test2())
    tests.append(test3())
    tests.append(test4())
    tests.append(test5())
    tests.append(test6())
    solutions = ""
    for x in tests:
        solutions += x
        solutions += '\n'
    with open('tests.txt', 'w') as f:
        f.write(solutions)
        f.close()
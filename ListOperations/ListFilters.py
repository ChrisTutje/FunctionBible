def keepAllElements(lst: list) -> list:
    return lst

keepAll = keepAllElements
def removeAllElements(lst: list) -> list:
    lst.clear()

removeAll = removeAllElements
clear = removeAllElements
def keepAlphaNumerical(lst: list) -> list:
    pass

def removeAlphaNumerical(lst: list) -> list:
    pass

def keepNumericalElements(lst: list) -> list:
    return [x for x in lst if isinstance(x, (int, float))]

keepNumbers = keepNumericalElements

def removeNumericalElements(lst: list) -> list:
    return [x for x in lst if not isinstance(x, (int, float))]

removeNumbers = removeNumericalElements

def keepIntegerElements(lst: list) -> list:
    return [x for x in lst if isinstance(x, (int))]

keepIntegers = keepIntegerElements
keepInts = keepIntegerElements

def removeIntegerElements(lst: list) -> list:
    return [x for x in lst if not isinstance(x, (int))]

removeIntegers = removeIntegerElements
removeInts = removeIntegerElements

def keepFloats(lst: list) -> list:
    pass

def removeFloats(lst: list) -> list:
    pass

def keepEvenElements(lst: list) -> list:
    return [x for x in lst if isinstance(x, int) and x % 2 == 0]

keepEvens = keepEvenElements

def removeEvenElements(lst: list) -> list:
    return [x for x in lst if not (isinstance(x, int) and x % 2 == 0)]

removeEvens = removeEvenElements

def keepOddElements(lst: list) -> list:
    return [x for x in lst if isinstance(x, int) and x % 2 != 0]

keepOdds = keepOddElements

def removeOddElements(lst: list) -> list:
    return [x for x in lst if not (isinstance(x, int) and x % 2 != 0)]

removeOdds = removeOddElements


def keepPositiveElements(lst: list) -> list:
    return [x for x in lst if isinstance(x, (int, float)) and x > 0]

keepPositives = keepPositiveElements

def removePositiveElements(lst: list) -> list:
    return [x for x in lst if not (isinstance(x, (int, float)) and x > 0)]

removePositives = removePositiveElements

def keepNegativeElements(lst: list) -> list:
    return [x for x in lst if isinstance(x, (int, float)) and x < 0]

keepNegatives = keepNegativeElements

def removeNegativeElements(lst: list) -> list:
    return [x for x in lst if not (isinstance(x, (int, float)) and x < 0)]

removeNegatives = removeNegativeElements

def keepPrime(lst: list) -> list:
    pass

def removePrime(lst: list) -> list:
    pass

def keepAntiPrime(lst: list) -> list:
    pass

def removeAntiPrime(lst: list) -> list:
    pass

def keepGreaterThan():
    pass

def removeGreaterThan():
    pass

def keepLesserThan():
    pass

def removelesserThan():
    pass

def keepEqualTo():
    pass

def removeEqualTo():
    pass

def keepLetters(lst: list) -> list:
    pass

def removeLetters(lst: list) -> list:
    pass

def keepVowels(lst: list) -> list:
    pass

def removeVowels(lst: list) -> list:
    pass

def keepConsonants(lst: list) -> list:
    pass

def removeConsonants(lst: list) -> list:
    pass

def keepUpperCase(lst: list) -> list:
    pass

def removeUpperCase(lst: list) -> list:
    pass

def keepLowerCase(lst: list) -> list:
    pass

def removeLowerCase(lst: list) -> list:
    pass

def keepSpecialCharacters():
    pass

def removeSpecialCharacters():
    pass

def keepPunctuation():
    pass

def removePunctutation():
    pass

def keepDuplicateCharacters(lst: list) -> list:
    pass

def removeDuplicateCharacters(lst: list) -> list:
    pass

def keepUniqueCharacters(lst: list) -> list:
    pass

def removeUniqueCharacters(lst: list) -> list:
    pass


def keepCharacterInstances(lst: list, *keep: str) -> list:
    return [x for x in lst if x in keep]

keepCharInstances = keepCharacterInstances
keepCharacters =keepCharacterInstances
keepCharacter = keepCharacterInstances
keepChars = keepCharacterInstances
keepChar = keepCharacterInstances
def removeCharacterInstances(lst: list, *remove: str) -> list:
    return [x for x in lst if x not in remove]

removeCharInstances = removeCharacterInstances
removeCharacters = removeCharacterInstances
removeCharacter = removeCharacterInstances
removeChars = removeCharacterInstances
removeChar = removeCharacterInstances

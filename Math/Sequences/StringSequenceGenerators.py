def generateAlphabet():
    for i in range(26):
        uppercaseLetter = chr(ord('A') + i)
        lowercaseLetter = chr(ord('a') + i)
        print(f"{uppercaseLetter}{lowercaseLetter}", end=" ")
def generateAlphabetUppercase():
    for i in range(26):
        uppercaseLetter = chr(ord('A') + i)
        print(f"{uppercaseLetter}", end=" ")

generateUppercase = generateAlphabetUppercase

def generateAlphabetLowercase():
    for i in range(26):
        lowercaseLetter = chr(ord('a') + i)
        print(f"{lowercaseLetter}", end=" ")

def generateVowels():
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return vowels

def generateConsonants():
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    return consonants

def generatePunctuation():
    pass

def generateSpecialCharacters():
    pass
def generatePassword():
    pass
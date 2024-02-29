def listStringBooleansCommands():
    functions = [name for name, obj in globals().items() if callable(obj) and name != 'listStringBooleansCommands']
    for func_name in functions:
        print(func_name)
def isPalindrome(str):
    pass

def isVowel():
    pass

def isConsonant():
    pass

def isUpperCase():
    pass

def isLowerCase():
    pass

def isSpecialCharacter():
    pass

def isDigit():
    pass

def isPunctuation():
    pass
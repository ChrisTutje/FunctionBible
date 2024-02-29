def listDatatypeBooleansCommands():
    functions = [name for name, obj in globals().items() if callable(obj) and name != 'listDatatypeBooleansCommands']
    for func_name in functions:
        print(func_name)

def isNumber():
    pass

def isInteger():
    pass

def isFloat():
    pass
isDouble = isFloat

def isAlphaNumeric():
    pass

def isString():
    pass

def isCharacter():
    pass

def isBoolean():
    pass
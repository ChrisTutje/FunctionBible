def listNumericalBooleansCommands():
    functions = [name for name, obj in globals().items() if callable(obj) and name != 'listNumericalBooleansCommands']
    for func_name in functions:
        print(func_name)

def isEven(x):
    return x % 2 == 0

def isOdd(x: (int, float)) -> bool:
    return x % 2 != 0

def isPositive(x: (int, float)) -> bool:
    return x >= 0

def isNegative(x: (int, float)) -> bool:
    return x < 0

def isPrime(x):
    pass

def isNotPrime(x):
    pass

def isAntiprime(x):
    pass

def isSquare(x):
    return x >= 0 and int(x ** 0.5) ** 2 == x

def isCube():
    pass
def listListBooleansCommands():
    functions = [name for name, obj in globals().items() if callable(obj) and name != 'listListBooleansCommands']
    for func_name in functions:
        print(func_name)

def isEmpty():
    pass

def isFull():
    pass

def isFirst():
    pass
isHead = isFull

def isLast():
    pass
isTail = isLast

def isMiddle():
    pass
isCenter = isMiddle

def isMutable():
    pass
isChangeable = isMutable

def isImmutable():
    pass
isUnchangeable = isImmutable

def isUnique():
    pass
isDistinct = isUnique
isNonDuplicitous = isUnique

def isDuplicitous():
    pass

def isOrdinal():
    pass
isOrdered = isOrdinal

def isUnordered():
    pass

def hasStaticMemory():
    pass

def hasDynamicMemory():
    pass

def isHomogenous():
    pass

def isHeterogenous():
    pass

def isFifo():
    pass
isQueue = isFifo

def isLifo():
    pass
isStack = isLifo

def hasKeys():
    pass
hasHash = hasKeys

def hasAny(array, value):
    return any(element == value for element in array)

def isIn(array: list, value) -> bool:
    return value in array

def hasAll(array, value):
    return all(element == value for element in array)
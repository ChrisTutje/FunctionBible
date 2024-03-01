def createList():
    pass

def insert():
    pass

def insertAt():
    pass

def insertAll():
    pass

def append():
    pass

def appendAll():
    pass

def dequeue():
    pass

def dequeueAll():
    pass

def pop():
    pass

def popAll():
    pass

def overwrite():
    pass

def overwriteAt():
    pass

def remove():
    pass

def removeAt():
    pass

def drop():
    pass

def find():
    pass
search = find

def peek():
    pass
def size():
    pass
count = size
length = size
def printItem():
    pass
def printStack():
    pass

def printMiddle():
    pass

def reverseOrder():
    pass

def cycle():
    pass
wrapAround = cycle

def merge():
    pass

def zipArray(array1, array2):
    zipped = []

    # Ensure both arrays have the same length
    min_len = min(len(array1), len(array2))

    for i in range(min_len):
        zipped.append(array1[i])
        zipped.append(array2[i])

    # Add any remaining elements from longer array
    zipped.extend(array1[min_len:])
    zipped.extend(array2[min_len:])

    return zipped
zip = zipArray

def unZipArray(array):
    unZipped1 = array[::2]
    unZipped2 = array[1::2]
    return unZipped1, unZipped2
unZip = unZipArray

def map():
    pass

#def filter():
    #pass

def reduce():
    pass

def spread():
    pass
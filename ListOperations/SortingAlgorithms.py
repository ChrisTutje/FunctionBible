import random

def shuffle(lst: list) -> list:
    random.shuffle(lst)
    return lst


def rotateListByX(lst, rotation):
    if rotation == 0:
        return lst

    rotation = rotation % len(lst)

    if rotation > 0:
        return lst[-rotation:] + lst[:-rotation]
    else:
        rotation = abs(rotation)
        return lst[rotation:] + lst[:rotation]

rotateListBy = rotateListByX
rotateBy = rotateListByX
rotateList = rotateListByX
rotate = rotateListByX

def alphabeticalSort(lst: list) -> list:
    if all(isinstance(item, str) for item in lst):
        return sorted(lst)
    else:
        raise ValueError("List must contain only alphabetical strings")

def reverseAlphabeticalSort(lst: list) -> list:
    if all(isinstance(item, str) for item in lst):
        return sorted(lst, reverse = True)
    else:
        raise ValueError("List must contain only alphabetical strings")
def numericalSort(lst: list) -> list:
    if all(isinstance(item, (int, float)) for item in lst):
        return sorted(lst)
    else:
        raise ValueError("List must contain only numbers")
def reverseNumericalSort(lst: list) -> list:
    if all(isinstance(item, (int, float)) for item in lst):
        return sorted(lst, reverse=True)
    else:
        raise ValueError("List must contain only numbers")

def linearSort():
    pass

def ascendingBubbleSort(lst: list) -> list: #linear
    n = len(lst)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
bubbleSort = ascendingBubbleSort

def descendingBubbleSort(lst: list) -> list: #linear
    n = len(lst)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
reverseBubbleSort = descendingBubbleSort

def ascendingSelectionSort(lst: list) -> list: #linear
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst
selectionSort = ascendingSelectionSort

def ascendingInsertionSort(lst: list) -> list: #linear
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst
insertionSort = ascendingInsertionSort

def descendingInsertionSort(lst: list) -> list: #linear
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key > lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst
reverseInsertionSort = descendingInsertionSort

def ascendingMergeSort(lst: list) -> list: ##quasi-linear, recursive
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    ascendingMergeSort(left_half)
    ascendingMergeSort(right_half)

    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            lst[k] = left_half[i]
            i += 1
        else:
            lst[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        lst[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        lst[k] = right_half[j]
        j += 1
        k += 1

    return lst
mergeSort = ascendingMergeSort


def descendingMergeSort(lst: list) -> list: #quasi-linear
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    descendingMergeSort(left_half)
    descendingMergeSort(right_half)

    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] > right_half[j]:
            lst[k] = left_half[i]
            i += 1
        else:
            lst[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        lst[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        lst[k] = right_half[j]
        j += 1
        k += 1

    return lst
reverseMergeSort = descendingMergeSort


def ascendingQuickSort(lst: list) -> list: #quasi-linear
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return ascendingQuickSort(left) + middle + ascendingQuickSort(right)
quickSort = ascendingQuickSort


def descendingQuickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]

    return descendingQuickSort(left) + middle + descendingQuickSort(right)
reverseQuickSort = descendingQuickSort


def heapSort():
    pass

def radixSort():
    pass

def standardSort():
    pass

def standardStableSort():
    pass

def shellSort():
    pass

def cocktailShakerSort():
    pass

def gnomeSort():
    pass

def bitonicSort():
    pass


def bogoSort(lst: list)-> list:
    def is_sorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    while not is_sorted(lst):
        random.shuffle(lst)

    return lst

def stalinSort(lst: list) -> list:
    i = 0
    while i < len(lst) - 1:
        if lst[i] > lst[i + 1]:
            del lst[i + 1]
        else:
            i += 1
    return lst

def sleepSort():
    pass

def slowSort():
    pass

def bozoSort():
    pass

def bogobogoSort():
    pass



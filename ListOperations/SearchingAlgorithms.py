def binarySearch(lst: list, target) -> (int, str):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return "not found"

def interpolationSearch():
    pass


def linearSearch(lst: list, target) -> (int, str):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return "not found"
sequentialSearch = linearSearch





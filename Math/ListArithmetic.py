from typing import List, Union, Any

def length(lst: List) -> int:
    return len(lst)
size = length
count = length

def summation(lst: List[Union[int, float]]) -> Union[int, float]:
    if not lst:
        return 0
    return sum(lst)

def difference(lst: List[Union[int, float]]) -> Union[int, float]:
    if not lst:
        return 0
    result = lst[0]
    for num in lst[1:]:
        result -= num
    return result

def product(lst: List[Union[int, float]]) -> Union[int, float]:
    if not lst:
        return 0
    result = lst[0]
    for num in lst[1:]:
        result *= num
    return result

def quotient(lst: List[Union[int, float]]) -> Union[int, float]:
    if not lst:
        return 0
    result = lst[0]
    for num in lst[1:]:
        result /= num
    return result
def exponentiation(lst: List[Union[int, float]]) -> Union[int, float]:
    pass
def rootExtraction(lst: List[Union[int, float]]) -> Union[int, float]:
    pass

def shifting(lst: List[Any], shiftAmount: Union[int, float]) -> List[Any]:
    return [x + shiftAmount for x in lst]

shift = shifting
def shiftByNumberOfElements(lst: List[int]) -> List[int]:
    x = len(lst)
    return [num + x for num in lst]

shiftByElements = shiftByNumberOfElements
def minimum(lst: List[Union[int, float]]) -> Union[int, float, None]:
    if not lst:
        return None

    minimum = lst[0]

    for i in lst:
        if i < minimum:
            minimum = i

    return minimum
#min = minimum

def maximum(lst: List[Union[int, float]]) -> Union[int, float, None]:
    if not lst:
        return None

    maximum = lst[0]

    for i in lst:
        if i > maximum:
            maximum = i

    return maximum
#max = maximum

def range(lst: List[Union[int, float]]) -> Union[int, float, None]:
    if not lst:
        return None

    minimum = maximum = lst[0]

    for num in lst:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num

    return maximum - minimum


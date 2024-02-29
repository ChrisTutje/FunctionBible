def summation(*args):
    return sum(args)

def difference(*args):
    pass

def product(*args):
    pass

def quotient(*args):
    pass

def minimum(list):
    if not list:
        return None

    minimum = list[0]

    for i in list:
        if i < minimum:
            minimum = list

    return minimum
#min = minimum

def maximum(list):
    if not list:
        return None

    maximum = list[0]

    for i in list:
        if i > maximum:
            maximum = i

    return maximum
#max = maximum

def range():
    pass


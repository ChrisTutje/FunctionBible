def add(x, y):
    return x + y


def increment(x, y):
    pass


def subtract(x, y):
    return x - y


def decrement(x, y):
    pass


def multiply(x, y):
    return x * y


def augment(x, y):
    pass


def double(x):
    return x * 2


def triple(x):
    return x * 3


def divide(x, y):
    if y == 0:
        raise ValueError("Can't' divide by zero")
    return x / y


def diminish(x, y):
    pass


def halve(x):
    return x / 2


def quarter(x):
    return x / 4


def floorDivide(x, y):
    if y == 0:
        raise ValueError("Can't' divide by zero")
    return x // y


def modulo(x, y):
    if y == 0:
        raise ValueError("Can't' modulo by zero")
    return x % y


def exponent(x, y):
    return x ** y
power = exponent


def reciprocal(x, y):
    if x == 0:
        raise ValueError("Reciprocal of zero is undefined")
    return pow(x, -y)


def square(x):
    return x ** 2


def squareRoot(x):
    return x ** 0.5


def cubeRoot(x):
    return x ** (1/3)


def root(x, y):
    return pow(x, 1.0 / y)


def permutate(x):
    result = 0
    for i in range(1, x + 1):
        result += i
    return result

def subtractivePermutate(x):
    result = 0
    for i in range(1, x + 1):
        result -= i
    return result


def factorial(x):
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

def divisiveFactorial(x):
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, x + 1):
        result /= i
    return result


def primeFactorization(x):
    pass


def absoluteValue(x):
    return abs(x)


def negation(x):
    return -x

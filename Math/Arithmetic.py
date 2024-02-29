def listArithmeticCommands():
    functions = [name for name, obj in globals().items() if callable(obj) and name != 'listArithmeticCommands']
    for func_name in functions:
        print(func_name)

def addition(x: (int, float), y: (int, float)) -> (int, float):
    return x + y


add = addition


def increment(x, y):
    pass


def subtraction(x: (int, float), y: (int, float)) -> (int, float):
    return x - y

subtract = subtraction


def decrement(x, y):
    pass


def multiplication(x: (int, float), y: (int, float)) -> (int, float):
    return x * y

multiply = multiplication


def augment(x, y):
    pass


def double(num: (int, float)) -> (int, float):
    return num * 2


def triple(num: (int, float)) -> (int, float):
    return num * 3


def division(x: (int, float), y: (int, float)) -> (int, float):
    if y == 0:
        raise ValueError("Can't' divide by zero")
    return x / y

divide = division


def diminish(x, y):
    pass


def halve(num: (int, float)) -> (int, float):
    return num / 2


def quarter(num: (int, float)) -> (int, float):
    return num / 4


def floorDivision(x: (int, float), y: (int, float)) -> (int, float):
    if y == 0:
        raise ValueError("Can't' divide by zero")
    return x // y

floorDivide = floorDivision


def modularDivision(x: (int, float), y: (int, float)) -> (int, float):
    if y == 0:
        raise ValueError("Can't' modulo by zero")
    return x % y

modula = modularDivision


def exponent(x: (int, float), y: (int, float)) -> (int, float):
    return x ** y


power = exponent


def reciprocal(x: (int, float), y: (int, float)) -> (int, float):
    if x == 0:
        raise ValueError("Reciprocal of zero is undefined")
    return pow(x, -y)


def square(num: (int, float)) -> (int, float):
    return num ** 2


def squareRoot(num: (int, float)) -> (int, float):
    return num ** 0.5


def cubeRoot(num: (int, float)) -> (int, float):
    return num ** (1/3)


def root(base: (int, float), power: (int, float)) -> (int, float):
    return pow(base, 1.0 / power)


def permutate(num: (int, float)) -> (int, float):
    result = 0
    for i in range(1, num + 1):
        result += i
    return result


def subtractivePermutate(num: (int, float)) -> (int, float):
    result = 0
    for i in range(1, num + 1):
        result -= i
    return result


def factorial(num: (int, float)) -> (int, float):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def divisiveFactorial(num: (int, float)) -> (int, float):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, num + 1):
        result /= i
    return result


def primeFactorization(num: (int, float)) -> (int, float):
    factors = []
    divisor = 2

    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1

    return factors

def simplification():
    pass


def absoluteValue(num: (int, float)) -> (int, float):
    return abs(num)


def negation(num: (int, float)) -> (int, float):
    return -num

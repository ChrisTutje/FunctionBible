def add(x, y):
    return x + y


addition = add


def increment(x, y):
    pass


def subtract(x, y):
    return x - y

subtraction = subtract


def decrement(x, y):
    pass


def multiply(x, y):
    return x * y

multiplication = multiply


def augment(x, y):
    pass


def double(num):
    return num * 2


def triple(num):
    return num * 3


def divide(x, y):
    if y == 0:
        raise ValueError("Can't' divide by zero")
    return x / y

division = divide


def diminish(x, y):
    pass


def halve(num):
    return num / 2


def quarter(num):
    return num / 4


def floorDivide(x, y):
    if y == 0:
        raise ValueError("Can't' divide by zero")
    return x // y

floorDivision = floorDivide


def modulo(x, y):
    if y == 0:
        raise ValueError("Can't' modulo by zero")
    return x % y

modularDivision = modulo


def exponent(x, y):
    return x ** y


power = exponent


def reciprocal(x, y):
    if x == 0:
        raise ValueError("Reciprocal of zero is undefined")
    return pow(x, -y)


def square(num):
    return num ** 2


def squareRoot(num):
    return num ** 0.5


def cubeRoot(num):
    return num ** (1/3)


def root(base, power):
    return pow(base, 1.0 / power)


def permutate(num):
    result = 0
    for i in range(1, num + 1):
        result += i
    return result


def subtractivePermutate(num):
    result = 0
    for i in range(1, num + 1):
        result -= i
    return result


def factorial(num):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def divisiveFactorial(num):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, num + 1):
        result /= i
    return result


def primeFactorization(num):
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


def absoluteValue(num):
    return abs(num)


def negation(num):
    return -num

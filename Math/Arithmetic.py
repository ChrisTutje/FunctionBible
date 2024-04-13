def listArithmeticCommands():
    functions = [name for name, obj in globals().items() if callable(obj) and name != 'listArithmeticCommands']
    for func_name in functions:
        print(func_name)

def reassignment(input, newValue):
    input = newValue
    return input

assignment = reassignment

def addition(x: (int, float), y: (int, float)) -> (int, float):
    return x + y


add = addition


def increment(num: (int, float)) -> (int, float):
    num += 1
    return num

proliferate = increment

def incrementByX(base: (int, float), incrementer: (int, float)) -> (int, float):
    base += incrementer
    return base

incrementBy = incrementByX


def subtraction(x: (int, float), y: (int, float)) -> (int, float):
    return x - y

subtract = subtraction


def decrement(num: (int, float)) -> (int, float):
    num -= 1
    return num

def multiplication(x: (int, float), y: (int, float)) -> (int, float):
    return x * y

multiply = multiplication


def augmentByX(base: (int, float), augmenter: (int, float)) -> (int, float):
    base *= augmenter
    return base

augmentBy = augmentByX
multiplyAssignment = augmentByX

def nullify(num: (int, float)) -> int:
    return num * 0

def increaseByOneAndAHalf(num: (int, float)) -> int:
    return num * 1.5

def double(num: (int, float)) -> (int, float):
    return num * 2


def triple(num: (int, float)) -> (int, float):
    return num * 3


def division(x: (int, float), y: (int, float)) -> (int, float):
    if y == 0:
        raise ValueError("Can't' divide by zero")
    return x / y

divide = division


def diminishByX(base: (int, float), diminisher: (int, float)) -> (int, float):
    base /= diminisher
    return base

diminishBy = diminishByX
divideAssignment = diminishByX

def decreaseByOneAndAHalf(num: (int, float)) -> int:
    return num / 1.5


def halve(num: (int, float)) -> (int, float):
    return num / 2

half = halve


def quarter(num: (int, float)) -> (int, float):
    return num / 4


def floorDivision(x: (int, float), y: (int, float)) -> (int, float):
    if y == 0:
        raise ValueError("Can't' divide by zero")
    return x // y

floorDivide = floorDivision

def floorDivisionAssignmentByX(base: (int, float), divisor: (int, float)) -> (int, float):
    base //= divisor
    return base


def modularDivision(x: (int, float), y: (int, float)) -> (int, float):
    if y == 0:
        raise ValueError("Can't' modulo by zero")
    return x % y

modulo = modularDivision

def modularDivisionAssignmentByX(base: (int, float), modulator: (int, float)) -> (int, float):
    base %= modulator
    return base


def exponent(x: (int, float), y: (int, float)) -> (int, float):
    return x ** y

power = exponent

def exponentAssignmentByX(base: (int, float), Power: (int, float)) -> (int, float):
    base **= power
    return base


def reciprocal(x: (int, float), y: (int, float)) -> (int, float):
    if x == 0:
        raise ValueError("Reciprocal of zero is undefined")
    return pow(x, -y)

def raiseToZeroithPower(num: (int, float)) -> int:
    return num ** 0

def square(num: (int, float)) -> (int, float):
    return num ** 2


def squareRoot(num: (int, float)) -> (int, float):
    return num ** 0.5


#def babylonianSquareRoot(num: int) -> int:
    #if num == 0:
        #return 0

    #left, right = 1, num
    #while left <= right:
        #mid = (left + right) // 2
        #if mid * mid == num:
            #return mid
        #elif mid * mid < num:
            #left = mid + 1
            #ans = mid
        #else:
            #right = mid - 1

    #return ans

def babylonianSquareRoot(num: int) -> int:
    if num == 0 or num == 1:
        return num

    low = 1
    high = num
    while low <= high:
        mid = (low + high) //2
        if mid * mid == num:
            return mid
        elif mid * mid < num:
            low = mid + 1
            ans = mid
        else:
            high = mid - 1
        return ans

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

def sigma(num: (int, float)) -> (int, float):
    result = 0
    for i in range(1, num + 1):
        if num % i == 0:
            result += i
    return result

def simplification():
    pass


def absoluteValue(num: (int, float)) -> (int, float):
    return abs(num)


def negation(num: (int, float)) -> (int, float):
    return -num

negate = negation

def calculateMaxTriangularNumber(num: int) -> int:
    low = 1
    high = num

    while low <= high:
        mid = (low + high) // 2
        total = mid * (mid + 1) // 2
        if total == num:
            return mid
        elif total < num:
            low = mid + 1
        else:
            high = mid - 1
    return high



import math
def listMathematicalFormulasCommands():
    functions = [name for name, obj in globals().items() if callable(obj) and name != 'listMathematicalFormulasCommands']
    for func_name in functions:
        print(func_name)


def pythagoreanTheorem(a: (int, float), b: (int, float)) -> (int, float):
    if a < 0 or b < 0:
        raise ValueError("Both sides of the triangle must be non-negative.")

    hypotenuseSquared = (a ** 2) + (b ** 2)
    hypotenuseLength = hypotenuseSquared ** 0.5

    return hypotenuseLength

calculateHypotenuse = pythagoreanTheorem

def quadraticFormula(a: (int, float), b: (int, float), c: (int, float)) -> (int, float):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        real_part = -b / (2 * a)
        imaginary_part = (-discriminant) ** 0.5 / (2 * a)
        return (real_part + imaginary_part * 1j, real_part - imaginary_part * 1j)

def calculateDistance(x1: (int, float), y1: (int, float), x2: (int, float), y2: (int, float) ) -> (int, float):
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

distanceFormula = calculateDistance

def calculateGrowth(initialValue: (int, float), growthRate: (int, float), timePeriod: (int, float)) -> (int, float):
    finalValue = initialValue * ((1 + growthRate) ** timePeriod)
    return finalValue

def calculateInterest(principal: (int, float), rate: (int, float), time: (int, float), timesCompounded: (int, float)) -> (int, float):
    amount = principal * (1 + rate / timesCompounded) ** (timesCompounded * time)
    return amount

def calculateCircleArea(radius: (int, float)) -> (int, float):
    area = math.pi * (radius ** 2)
    return area

circleArea = calculateCircleArea

def calculateCircleCircumference(radius: (int, float)) -> (int, float):
    circumference = 2 * math.pi * radius
    return circumference

circleCircumference = calculateCircleCircumference

def calculateTriangleArea(base: (int, float), height: (int, float)) -> (int, float):
    area = 0.5 * base * height
    return area

triangleArea = calculateTriangleArea

def calculateTrianglePerimeter(side1: (int, float), side2: (int, float), side3: (int, float)) -> (int, float):
    perimeter = side1 + side2 + side3
    return perimeter

trianglePerimeter = calculateTrianglePerimeter

def calculateRectangleArea(length : (int, float), width: (int, float)) -> (int, float):
    area = length * width
    return area

rectangleArea = calculateRectangleArea
def calculateRectanglePerimeter(length: (int, float), width: (int, float)) -> (int, float):
    perimeter = 2 * (length * width)
    return perimeter

def calculateSquareArea(sideLength: (int, float)) -> (int, float):
    area = sideLength ** 2
    pass

def calculateSquarePerimeter(sideLength: (int, float)) -> (int, float):
    perimeter = 4 * sideLength
    return perimeter

def calculateTrapezoidArea():
    pass

def calculateSphereVolume():
    pass

def calculateSphereSurfaceArea():
    pass

def calculateCylinderVolume():
    pass

def calculateCylinderSurfaceArea():
    pass

def calculateConeVolume():
    pass

def calculateConeSurfaceArea():
    pass

def calculateRectangularPrismVolume():
    pass

def calculateRectangularPrismSurfaceArea():
    pass

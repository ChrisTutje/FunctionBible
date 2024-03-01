from fractions import Fraction

def convertToInteger(input) -> int:
    try:
        return int(input)
    except (ValueError, TypeError):
        return None

convertToInt = convertToInteger
toInteger = convertToInteger
toInt = convertToInteger
def convertToFloat(input) -> float:
    try:
        return float(input)
    except (ValueError, TypeError):
        return None

convertToDouble = convertToFloat
convertToDecimal = convertToFloat
toDouble = convertToFloat
toDecimal = convertToFloat
def convertToPercent(input: (int, float)) -> float:
    try:
        return float(input) * 0.01
    except (ValueError, TypeError):
        return None

toPercent = convertToPercent

def convertFractionToDecimal(numerator: (int, float), denominator: (int, float))-> float:
    return numerator / denominator

fractionToDecimal = convertFractionToDecimal

def convertDecimalToFraction(decimal: float):
    try:
        fraction = Fraction(decimal).limit_denominator()
        return f"{fraction.numerator}/{fraction.denominator}"
    except (ValueError, TypeError):
        return None

decimalToFraction = convertDecimalToFraction

def convertRatioToDecimal():
    pass

def convertDecimalToRatio():
    pass

def convertRatioToFraction():
    pass

def convertFractionToRatio():
    pass

def convertToCharacter():
    pass

convertToChar = convertToCharacter
toCharacter = convertToCharacter
toChar = convertToCharacter

def convertToString(input) -> str:
    return str(input)

convertToStr = convertToString
toString = convertToString
toStr = convertToString

def convertToUpperCase(string: str) -> str:
    return string.upper()

convertToUpper = convertToUpperCase
toUpperCase = convertToUpperCase
toUpper = convertToUpperCase

def convertToLowerCase(string: str) -> str:
    return string.lower()

convertToLower = convertToLowerCase
toLowerCase = convertToLowerCase
toLower = convertToLowerCase
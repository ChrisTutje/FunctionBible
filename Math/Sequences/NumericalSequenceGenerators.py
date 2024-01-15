
import random
def generateHarmonicSeries(startRange, endRange):
    harmonicSeries = []

    for i in range(startRange, endRange + 1):
        harmonicSeries.append(i)

    return harmonicSeries
generateAutonumber = generateHarmonicSeries
generateIndex = generateHarmonicSeries
generatePrimaryKey = generateHarmonicSeries

def generateEvenNumbers(startRange, endRange):
    evenNumbers = []

    if startRange % 2 != 0:
        startRange += 1

    for i in range(startRange, endRange + 1, 2):
        evenNumbers.append(i)

    return evenNumbers
generateEvens = generateEvenNumbers

def generateOddNumbers(startRange, endRange):
    oddNumbers = []

    if startRange % 2 == 0:
        startRange += 1

    for i in range(startRange, endRange + 1, 2):
        oddNumbers.append(i)

    return oddNumbers
generateOdds = generateOddNumbers

def generatePrimes():
    pass

def generateAntiPrimes():
    pass

def generateIncrementsOfX(startRange, endRange):
    increments = []

    for i in range(startRange, endRange + 1, startRange):
        increments.append(i)

    return increments
generateIncrements = generateIncrementsOfX
countUp = generateIncrementsOfX
generateMultiplesOfX = generateIncrementsOfX

def generateDecrementsOfX(startRange, endRange):
    decrements = []

    for i in range(startRange, endRange - 1, -1):
        decrements.append(i)

    return decrements
generateDecrements = generateDecrementsOfX
countDown = generateDecrementsOfX

def generateSquares():
    pass

def generateBinarySeries():
    pass

def generateRandomSequence(indexValue, lowestValue, highestValue):
    randomSequence = []

    for i in range(indexValue):
        randomSequence.append(random.randint(lowestValue,highestValue))

    return randomSequence
generateRandom = generateRandomSequence

def generateCTSequence(indexValue):
    pass



def sequenceGenerator(startRange, endRange, incrementor, index):
    pass


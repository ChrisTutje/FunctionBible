import random


def randomNumberGenerator(startRange, endRange):
    return random.randint(startRange, endRange)
rng = randomNumberGenerator
def coinFlip():
    result = random.choice(["heads", "tails"])
    return result

def rollD4():
    return random.randint(1,4)

def rollD6():
    return random.randint(1,6)

def rollD8():
    return random.randint(1,8)

def rollD10():
    return random.randint(1,10)

def rollD12():
    return random.randint(1,12)

def rollD20():
    return random.randint(1,20)

def rollD100():
    return random.randint(1,100)

def rollD360():
    return random.randint(1,360)

def rollDX(numSides):
    return random.randint(1, numSides)

def rockPaperScissors():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
rps = rockPaperScissors

def rockPaperScissorsLizardSpock():
    choices = ["rock", "paper", "scissors", "lizard", "Spock"]
    return random.choice(choices)
rpsls = rockPaperScissorsLizardSpock

def leftTrim(str):
    return str.lstrip()
leftStrip = leftTrim

def rightTrim(str):
    return str.rstrip()
rightStrip = rightTrim

def trimAll(str):
    return str.replace(" ", "")
stripAll = trimAll
def removeCommas(str):
    return str.replace(",", "")

def removeSquareBrackets(str):
    return str.replace("[", "").replace("]", "")
def forLoop(counter, sentinelValue, incrementor):
    result = []

    while counter != sentinelValue:
        result.append(counter)
        counter += incrementor

    return result
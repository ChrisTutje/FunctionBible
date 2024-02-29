from Booleans.DatatypeBooleans import *
from Booleans.GeometryBooleans import *
from Booleans.ListBooleans import *
from Booleans.NumericalBooleans import *
from Cataloging.CatalogingFunctions import *
from FileStreaming.IO import *
from FileStreaming.Parsing import *
from ListOperations.ListOperations import *
from Loops.Loops import *
from Math.Arithmetic import *
from Math.ListArithmetic import *
from Math.MathematicalFormulas import *
from Math.RandomMath.RandomMath import *
from Math.Sequences.NumericalSequenceGenerators import *
from Math.Sequences.StringSequenceGenerators import *
from StringOperations.StringOperations import *
from Typecasting.UnitConversion import *

def foo():

    return generateCTSequence(64)

if __name__ == "__main__":
    #listAllCommands()

    #array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = foo()
    #parsedResult = ""

    #print(f"List: {array}")
    print(f"Result: {result}")
    #print(f"Parsed Result: {parsedResult}")

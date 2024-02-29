def listGeometryBooleansCommands():
    functions = [name for name, obj in globals().items() if callable(obj) and name != 'listGeometryBooleansCommands']
    for func_name in functions:
        print(func_name)

def isTriangle():
    pass
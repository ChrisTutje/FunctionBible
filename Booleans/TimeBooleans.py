def listTimeBooleansCommands():
    functions = [name for name, obj in globals().items() if callable(obj) and name != 'listTimeBooleansCommands']
    for func_name in functions:
        print(func_name)

def isLeapYear():
    pass
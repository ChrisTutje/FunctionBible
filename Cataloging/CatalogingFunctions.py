import os
import ast

def listCatalogingCommands():
    functions = [name for name, obj in globals().items() if callable(obj) and name != 'listCatalogingCommands']
    for func_name in functions:
        print(func_name)
def listFilesWithFunctions(directory="."):
    files_with_functions = []

    for root, dirs, files in os.walk(directory):
        # Exclude the .venv directory from traversal
        if ".venv" in dirs:
            dirs.remove(".venv")

        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if "def " in content:
                        files_with_functions.append(file_path)

    print("Files with functions:")
    for file in files_with_functions:
        print(file)


def listAllCommands():
    def getFunctionsFromFile(filePath):
        with open(filePath, 'r') as file:
            tree = ast.parse(file.read(), filename=filePath)

        functions = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append(node.name)

        return functions

    def listFilesWithFunctions(directory="."):
        filesWithFunctions = []

        for root, dirs, files in os.walk(directory):
            # Exclude the .venv directory from traversal
            if ".venv" in dirs:
                dirs.remove(".venv")

            for file in files:
                if file.endswith(".py"):
                    filePath = os.path.join(root, file)
                    with open(filePath, "r", encoding="utf-8") as f:
                        content = f.read()
                        if "def " in content:
                            filesWithFunctions.append(filePath)

        print("Files with functions:")
        for file in filesWithFunctions:
            print(file)
            print("Functions in file:")
            functions = getFunctionsFromFile(file)
            for functionName in functions:
                print(f"- {functionName}")
            print()

    listFilesWithFunctions()
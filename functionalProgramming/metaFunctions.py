def compose(*funcs):
    def composed_function(arg):
        result = arg
        for func in reversed(funcs):
            result = func(result)
        return result
    return composed_function
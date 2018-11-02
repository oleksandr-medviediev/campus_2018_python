def map_functions(target, functions):
    result = target
    for func in functions:
        result = func(result)
    return result


print(map_functions(2, [lambda x: x**2, lambda x: x + 1]))

def map_functions(value, *functions):

    result = []

    for i, func in enumerate(functions):
        result.append(func(value))

    return result

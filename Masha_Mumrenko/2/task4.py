def map_function_list(functions, to_apply):
    result = []
    for func in functions:
        result.append(func(to_apply))

    return result

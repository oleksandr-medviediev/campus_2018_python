import math


def map_function_list(functions, value):
    """function which applies a bunch of functions to the param

    Arguments:
        functions  -- any iterable data structure that contains functions
        value -- decimal value

    Returns:
        list -- list of results of functions
    """

    result = []
    for func in functions:
        result.append(func(value))

    return result


family_of_functions = (math.sin,  math.cos, math.tan)
print(map_function_list(family_of_functions, 0))

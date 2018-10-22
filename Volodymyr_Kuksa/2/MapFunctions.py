import math


def map_functions(argument, functions):
    """
    Apply functions to argument and return list of results.

    :param argument: argument that is passed to the functions.

    :param functions: iterable that consists of functions.
    :type functions: iterable.

    :return: list of results.
    :rtype: list.
    """
    results = list()

    for func in functions:

        results.append(func(argument))

    return results


function_family = (math.sin, math.cos, math.tan)

print(map_functions(math.pi, function_family))

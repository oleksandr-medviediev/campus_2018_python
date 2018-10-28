import math

def func_map(element, *funcs):
    """
    Invokes all of *funcs passing element in it

    :param element: element that will be used as an argument for each of *funcs
    :param *funcs: any number of iterable objects that contain functions which expect one argument
    :return: list of results of calls of each of functions
    """

    results = []

    for tuple_of_funcs in funcs:
        for func in tuple_of_funcs:
            results.append(func(element))

    return results

test_result = func_map(0, [math.sin, math.cos], [math.tan, math.atan])
print(test_result)
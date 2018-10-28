import math


def map_functions(arg, *functions):
    """
    Given object arg and functions - subsequently use those functions on arg.

    Args:
        arg (obj): any object.
        *functions: functions which can take arg.

    Returns:
        arg.
    """
    for func in functions:
        arg = func(arg)
    return arg


num = float(input("Enter number\n"))
print(map_functions(num, math.sin, math.cos))

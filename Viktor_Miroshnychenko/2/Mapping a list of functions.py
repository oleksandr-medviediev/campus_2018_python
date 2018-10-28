def map_functions(variable, functions):
    """
    :param variable: variable which is used by functions
    :type variable: any type that is valid to functions

    :param functions: functions that must process variable
    :type functions: functions

    :return: list of results of functions calls
    :rtype: list
    """
    return_val = []
    for func in functions:
        return_val.append(func(variable))

    return return_val


functions = [ lambda var: var + 2, lambda var: var - 2, lambda var: var / 2 ]

print(map_functions(4, functions))

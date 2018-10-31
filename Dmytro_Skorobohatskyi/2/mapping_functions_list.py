def map_functions(value, *functions):

    """ Function apply functions to value and return list of result values.

    Args:
        value(float): value for applying of functions
        functions(tuple): tuple of variadic function's amount.

    Returns:
        list: new list with values of function's applying to value.
        
    """
    
    result = []

    for i, func in enumerate(functions):
        result.append(func(value))

    return result

def custom_map (func, *iterables):
    """
    Computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.

Parameters:
    func - function applied to iteratables
    iterables - iteratables to which function is applied

Returns:
    list of function results
    """
    
    result = []
    
    min_length = len(iterables[0])

    for i in range(1, len(iterables)):
        min_length = min(min_length, len(iterables[i]))

    for j in range(min_length):
        for i in range(len(iterables)):
            result.append(func(iterables[i][j]))

    return result

def custom_map(func, *iterables):

    """
    def custom_map(func, *iterables)
    Invokes func passing as arguments tuples made from *iterables argument.

    :param func: a function which expects len(*iterables) number of arguments
    :param *iterables: any number of iterables
    :return: list filled with results returned by func argument. length of list
    will be equal to a length of the shortest iterable argument
    :rtype: list
    """

    results = [func(*args) for args in zip(*iterables)]
    return results


find_sum = lambda x, y: x + y
sum_of_vectors = custom_map(find_sum, [1, 2, 1], [-1, -2, -1])
print(sum_of_vectors)

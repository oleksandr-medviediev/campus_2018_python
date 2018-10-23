def map_functions(arg, *functions):

    """
    :param arg: forwarded argument
    :param functions: iterable of unary functions

    :returns: list of results of applying functions to arg
    """

    return [func(arg) for func in functions]


functions = (lambda x : x + 1, lambda x : x + 2, lambda x : x + 3)
assert map_functions(0, *functions) == [1, 2, 3]
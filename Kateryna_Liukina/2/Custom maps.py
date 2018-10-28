def custom_map(func, iter):
    """Applies function to every item in given iterable"""
    return [func(i) for i in iter]


def custom_map_multiple_functions(func, element):
    """Applies every function from func list to given element"""
    return [f(element) for f in func]


def custom_map_extended(func, iter):
    """Applies every function from func list to every item in given iterable"""
    return [f(i) for i in iter for f in func]
def custom_map(func, container):
    """Applies function to every item in given container"""
    return [func(i) for i in container]


def custom_map_multiple_functions(func, element):
    """Applies every function from func list to given element"""
    return [f(element) for f in func]


def custom_map_extended(func, container):
    """Applies every function from func list to every item in given container"""
    return [f(i) for i in container for f in func]
def custom_map(func, container):
    """Applies function to every item in given container
	
	Args:
        func: function or lambda
        container(list): list of items
    Returns:
        list: new list with values
	"""
    return [func(i) for i in container]


def custom_map_multiple_functions(func, element):
    """Applies every function from func list to given element
	
	Args:
        func(list): list of function or lambda
        element: item
    Returns:
        list: new list with values
	"""
    return [f(element) for f in func]


def custom_map_extended(func, container):
    """Applies every function from func list to every item in given container
	
	Args:
        func(list): list of function or lambda
        container(list): list of items
    Returns:
        list: new list with values
	"""
    return [f(i) for i in container for f in func]
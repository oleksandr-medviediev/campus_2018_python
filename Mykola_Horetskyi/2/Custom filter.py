def custom_filter (func, iterable):
    """
    Constructs a list of elements from iterable for which func returns True

Parameters:
    func - filter function
    iterable - iteratable container being filtered

Returns:
    list of elements from iterable for which func returns True
    """
    
    result = []
    
    for element in iterable:
        if func(element):
            result.append(element)

    return result

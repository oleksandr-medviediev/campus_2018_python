def custom_filter(function, iterable):
    """similar to original filter() function"""
    return [item for item in iterable if function(item)]

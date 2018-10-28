def custom_filter(func, items):
    """
    keeps the elements in collection which satisfied a condition supplied by `func`
        :param func: function or None
            if it's function, then keep elements which returns True on this param
            else if it's None, then keep elements which could be interpreted as True
        :param items: collection which should be filtered
        :return: filtered collection
    """

    if func is None:
        def func(item): return bool(item)
    filtered_items = [item for item in items if func(item) is True]

    return filtered_items

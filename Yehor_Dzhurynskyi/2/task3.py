def custom_map(func, items):
    """
    applies function to each element in collection
        :param func: function which is applied to collection
        :param items: collection of any elements
        :return mapped collection
    """

    mapped_items = [func(item) for item in items]

    return mapped_items

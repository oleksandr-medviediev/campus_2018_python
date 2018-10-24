def custom_map(func, items):

    mapped_items = [func(item) for item in items]

    return mapped_items

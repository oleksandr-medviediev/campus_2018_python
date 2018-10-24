def custom_filter(func, items):

    if func is None:
        def func(item): return bool(item)
    filtered_items = [item for item in items if func(item) is True]

    return filtered_items

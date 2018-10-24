def custom_filter(func, items):
    if func is None:
        def func(item): return bool(item)
    return [item for item in items if func(item) is True]

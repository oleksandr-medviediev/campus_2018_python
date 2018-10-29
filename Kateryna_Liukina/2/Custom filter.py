def custom_filter(func, container):
    """Find every item in given container that func of item returns true"""
    return [i for i in container if func(i)]

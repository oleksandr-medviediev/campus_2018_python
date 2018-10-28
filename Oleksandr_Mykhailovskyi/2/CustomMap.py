def custom_map(func, *iterables):
    """
    Implementation of map function.

    Args:
        func (function): any function object.
        *iterables: any containers.

    Returns:
        List of func results.
    """
    res = []
    for args in zip(*iterables):
        res.append(func(*args))
    return res

res = custom_map(lambda x, y: x + y, [1, 2, 3], [0, 1])
print(res)

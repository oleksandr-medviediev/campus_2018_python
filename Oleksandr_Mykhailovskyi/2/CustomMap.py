def custom_map(func, *iterables):
    res = []
    for args in zip(*iterables):
        res.append(func(*args))
    return res

res = custom_map(lambda x, y: x + y, [1, 2, 3], [0, 1])
print(res)

def custom_map(func, iterable):
    result = (func(element) for element in iterable)
    return result


print(list(custom_map(lambda x: x**2, [1, 2, 3])))

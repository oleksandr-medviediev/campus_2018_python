def custom_map(func, iterable):
    return (func(element) for element in iterable)


print(list(custom_map(lambda x: x**2, [1, 2, 3])))

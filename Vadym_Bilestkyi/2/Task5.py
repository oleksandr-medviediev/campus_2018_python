def custom_filter(predicate, iterable):
    return (element for element in iterable if predicate(element))


print(list(custom_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))

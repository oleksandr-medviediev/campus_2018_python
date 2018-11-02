def custom_filter(predicate, iterable):
    result = (element for element in iterable if predicate(element))
    return result


print(list(custom_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))

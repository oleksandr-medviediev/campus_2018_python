
def custom_map(func, *iterables):
    length_list = [len(arg) for arg in iterables]
    min_length = min(length_list)

    result = []
    for index in range(min_length):
        parameters_list = []

        for arg in iterables:
            parameters_list.append(arg[index])

        result.append(func(*parameters_list))

    return result


print("map", *map(lambda x, y: x ** y, [5, 3, 5], [2, 2, 2]))
print("custom_map", custom_map(lambda x, y: x ** y, [5, 3, 5], [2, 2, 2]))

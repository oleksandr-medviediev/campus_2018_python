

def my_map(foo, *arg):
    min_len = min(len(val) for val in arg)
    result = list()

    for i in range(min_len):
        foo_arg = tuple(val[i] for val in arg)
        result.append(foo(*foo_arg))

    return result


print('map', *map(lambda x, y : x ** y, [1, 2, 9], [7, 3]))
print('my_map', *my_map(lambda x, y : x ** y, [1, 2, 9], [7, 3]))

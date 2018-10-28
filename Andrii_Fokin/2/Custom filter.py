
def custom_filter(foo, iterable):
    result = list()

    if foo:
        condition = lambda x: foo(x)
    else:
        condition = lambda x: x

    for val in iterable:
        if condition(val):
            result.append(val)
    return result

print(custom_filter(None, [0, 1, 2]))
print(custom_filter(lambda x: x % 2, [0, 1, 2]))


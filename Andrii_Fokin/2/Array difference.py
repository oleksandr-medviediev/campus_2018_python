
def array_diff(first, second):
    f_set = set(first)
    s_set = set(second)
    return list(f_set.difference(s_set))


print(array_diff([1, 2], [1]))
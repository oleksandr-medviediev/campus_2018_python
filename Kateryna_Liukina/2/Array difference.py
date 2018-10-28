def array_difference(ar1, ar2):
    return list(set(ar1)-set(ar2))


def array_difference2(ar1, ar2):
    return [i for i in ar1 if i not in ar2]


print (array_difference2([1, 2, 2, 2, 3], [2]))
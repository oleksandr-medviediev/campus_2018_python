def array_diff1(list1, list2):
    return set(list1).difference(list2)


def array_diff2(list1, list2):
    return [el for el in list1 if list2.count(el) == 0]

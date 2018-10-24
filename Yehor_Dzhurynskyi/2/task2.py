def array_diff1(list1, list2):

    diff_set = set(list1).difference(list2)

    return diff_set


def array_diff2(list1, list2):

    diff_set = [el for el in list1 if list2.count(el) == 0]

    return diff_set

def array_difference(ar1, ar2):
    """Finds the difference between two list"""
    return list(set(ar1)-set(ar2))


def array_difference2(ar1, ar2):
    """Finds the difference between two list"""
    return [i for i in ar1 if i not in ar2]


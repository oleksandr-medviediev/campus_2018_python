def array_diff(a, b):

    """
    :param a: iterable 
    :param b: iterable
    :returns: intersection of the sets defined by array params
    """
    
    return [x for x in a if x not in b]

def array_diff_sets(a, b):

    """
    :param a: iterable 
    :param b: iterable
    :returns: intersection of the sets defined by array params
    """

    # please, don't tell me this is too complex in return as well :(
    return list(set(a) - set (b))


assert array_diff_sets([1, 2, 3], [1, 2]) == [3]
assert array_diff_sets([1, 2, 2, 2, 3], [2]) == [1, 3]

assert array_diff([1, 2, 3], [1, 2]) == [3]
assert array_diff([1, 2, 2, 2, 3], [2]) == [1, 3]

def array_diff1(lhs, rhs):
    """return the difference of lists"""
    for val in rhs:
        [lhs.remove(val) for i in range(lhs.count(val))]

    return lhs

def array_diff2(lhs, rhs):
    """return the difference of lists"""
    return [val for val in lhs if val not in rhs]

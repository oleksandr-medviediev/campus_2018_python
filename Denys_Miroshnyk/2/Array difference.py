def array_subtract_1(left, right):
    """
    function subtracts one list from another

    Arguments:
        left {list} -- list of integers
        right {list} -- list of integers subtracted  from the first one
        
    Returns:
        list -- elements of right are subtracted from left
    """
    result = left

    for i in result:
        if i in right:
            result.remove(i)

    return result


def array_subtract_2(left, right):
    """
    function subtracts one list from another

    Arguments:
        left {list} -- list of integers
        right {list} -- list of integers subtracted  from the first one

    Returns:
        set -- elements of right are subtracted from left
    """
    diff_set = set(left).difference(right)

    return diff_set


left = [1, 2, 5, 9, 9, 4, 5]
right = [1, 5, 5, 6]

output_1 = array_subtract_1(left, right)
print(output_1)

output_2 = array_subtract_2(left, right)
print(output_2)

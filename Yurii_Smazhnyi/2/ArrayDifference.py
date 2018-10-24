def diff_array_with_set(array_i, array_j):

    """
    returns difference of array_i and array_j using set

    @param array_i: minuend array
    @param array_j: subtrahend array
    @returns: difference array_i - array_j
    """

    difference = list(set(array_i) - set(array_j))

    return difference


def diff_array_manually(array_i, array_j):

    """
    returns difference of array_i and array_j using manual iterations

    @param array_i: minuend array
    @param array_j: subtrahend array
    @returns: difference array_i - array_j
    """

    difference = []

    for i in array_i:

        is_in_array = False

        for j in array_j:

            if i == j:

                is_in_array = True
                break

        if not is_in_array:
            
            difference.append(i)

    return difference
            

test_list = [1, 2, 3, 4, 5, 6, 2, 3, 3, 1]
test_list2 = [1, 2, 3, 4, 6, 2, 3, 3, 1]

print(diff_array_with_set(test_list, test_list2))
print(diff_array_manually(test_list, test_list2))

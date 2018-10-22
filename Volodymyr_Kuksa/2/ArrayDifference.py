def array_diff1(a, b):
    """
    Return the list of all elements that are present in a, but absent from b.

    :param a: minuend array.
    :type a: iterable.

    :param b: subtrahend array.
    :type b: iterable.

    :return: difference array.
    :rtype: list.
    """
    result = list()

    for element in a:

        if not b.count(element):

            result.append(element)

    return result


def array_diff2(a, b):
    """
    Return the list of all elements that are present in a, but absent from b.

    :param a: minuend array.
    :type a: iterable.

    :param b: subtrahend array.
    :type b: iterable.

    :return: difference array.
    :rtype: list.

    Implemented via filter().
    """
    result = list(filter(lambda element: not b.count(element), a))

    return result


test1_a = [1, 2]
test1_b = [1]

print('\ntest1')
print('array_diff1:', array_diff1(test1_a, test1_b))
print('array_diff2:', array_diff2(test1_a, test1_b))

test2_a = [1, 2, 2, 2, 3]
test2_b = [2]

print('\ntest2')
print('array_diff1:', array_diff1(test2_a, test2_b))
print('array_diff2:', array_diff2(test2_a, test2_b))

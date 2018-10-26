def custom_filter(func, array):
    """
    Construct a list from those elements of array for which function returns true.

    :param func: filter function.
    :type func: function.

    :param array: array of elements to be filtered.
    :type array: iterable

    :return: list of filtered.
    :rtype: list.
    """
    results = list()

    for element in array:

        if func(element):

            results.append(element)

    return results


test_list = list(range(10))

print(custom_filter(lambda x: x > 5, test_list))

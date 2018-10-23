def find_odd1(array):
    """
    Return the first element that occurs an odd number of times in the array.

    :param array: the array that is being searched for elements that occur odd number of times.
    :type array: iterable.

    :return: the first element that occurs an odd number of times in the array or None if such element is absent.

    Implemented via list().count().
    """
    result = None

    for element in array:

        number_of_occurrences = array.count(element)
        is_odd = number_of_occurrences % 2

        if is_odd:

            result = element
            break

    return result


def find_odd2(array):
    """
    Return the first element that occurs an odd number of times in the array.

    :param array: the array that is being searched for elements that occur odd number of times.
    :type array: iterable.

    :return: the first element that occurs an odd number of times in the array or None if such element is absent

    Implemented via map().
    """
    occurrences = list(map(lambda element: array.count(element), array))

    result = None

    for i in range(len(array)):

        is_odd = occurrences[i] % 2

        if is_odd:

            result = array[i]

    return result


def find_odd3(array):
    """
    Return the first element that occurs an odd number of times in the array.

    :param array: the array that is being searched for elements that occur odd number of times.
    :type array: iterable.

    :return: the first element that occurs an odd number of times in the array or None if such element is absent

    Implemented via filter().
    """
    filtered_array = list(filter(lambda element: array.count(element) % 2, array))

    result = None

    if len(filtered_array):

        result = filtered_array[0]

    return result


test_array = [1, 2, 3, 1, 3, 2, 1]

print('find_odd1:', find_odd1(test_array))
print('find_odd2:', find_odd1(test_array))
print('find_odd3:', find_odd1(test_array))

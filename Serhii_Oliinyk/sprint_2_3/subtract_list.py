def first_method(array1, array2):
    """Function substract two lists.

    Args:
        array1: type list.
        array2: type list.

    Returns:
        Return substracted list.

    """

    result = []

    for i in array1:
        count = array2.count(i)

        if(count == 0):
            result.append(i)
        else:
            array2.remove(i)

    result += array2

    return result


def second_method(array1, array2):
    """Function substract two lists.

    Args:
        array1: type list.
        array2: type list.

    Returns:
        Return substracted list.

    """

    result = [i for i in array1 if not i in array2 or array2.remove(i)]
    result += array2

    return result


if __name__ == '__main__':
    data1 = [1, 2, 3]
    data2 = [1, 4, 6]

    array = first_method(data1, data2)
    print(array)

    data1 = [1, 2, 3]
    data2 = [1, 4, 6]

    array = second_method(data1, data2)
    print(array)

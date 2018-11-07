def first_method(array):
    """Search the digit which localted in array odd number of times.

    Args:
        array: type list

    Returns:
        Return number from the list.

    """
    for i in array:
        number = array.count(i)
        if(number % 2 != 0):
            return i


def second_method(array):
    """Search the digit which localted in array odd number of times.

    Args:
        array: type list

    Returns:
        Return number from the list.

    """
    array.sort()
    count = 1

    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            count += 1
        elif (count > 1) and (count % 2 != 0):
            return array[i]


def third_method(array):
    """Search the digit which localted in array odd number of times.

    Args:
        array: type list

    Returns:
        Return number from the list.

    """

    for i in range(len(array)):
        count = 0
        for j in range(len(array)):
            if array[i] == array[j]:
                count += 1

        if count % 2 != 0:
            return array[i]


if __name__ == '__main__':
    array = [1, 2, 3, 1, 3, 2, 1]

    value = first_method(array)
    print(value)

    value = second_method(array)
    print(value)

    value = third_method(array)
    print(value)

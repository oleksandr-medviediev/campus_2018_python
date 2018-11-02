def my_map(function, array):
    """Implementation of the function map().

    Args:
        function: type lambda.
        array: type list

    Returns:
        Return list.

    """
    result = []

    for i in array:
        result.append(function(i))

    return result


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]

    result = my_map(lambda x: x**2, array)
    print(result)



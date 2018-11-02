def my_filter(function, array):
    """Implementation of the filter() method.

    Args:
        function: type lambda.
        array: type list.

    Returns:
        Return list with filtered data.

    """
    result = []

    for i in array:
        if(function(i) == True):
            result.append(i)

    return result


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]

    result = my_filter(lambda x: x >= 3, array)
    print(result)

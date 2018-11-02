def my_map(value, listOfFunction):
    """Implementation of the function map() which take bunch of functions.

    Args:
        value: type integer.
        listOfFunction: type list

    Returns:
        Return list of results for each function.

    """
    result = []
    for i in listOfFunction:
        result.append(i(value))

    return result


if __name__ == '__main__':
    list = [lambda x: x ** 2, lambda x: x + 2, lambda x: x - 2]
    value = 3

    result = my_map(value, list)
    print(result)
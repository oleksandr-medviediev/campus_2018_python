def find_odd_linear_search(array):
    """
    Returns int that appears odd number of times

    :param array: list of ints
    :return: int that appeared odd times in array
    :rtype: int
    """

    for num in array:
        if array.count(num) % 2:

            return num


def find_odd_set_method(array):
    """
    Returns int that appears odd number of times

    :param array: list of ints
    :return: int that appeared odd times in array
    :rtype: int
    """

    odds = set()
    for num in array:
        try:
            odds.remove(num)
        except KeyError:
            odds.add(num)
    
    return odds.pop()


if __name__ == "__main__":
    arr = [1, 2, 3, 1, 3, 2, 1]
    number = find_odd_set_method(arr)
    print(number)

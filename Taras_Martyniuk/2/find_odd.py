def find_odd(numbers):

    """
        :param numbers: iterable of ints
        :returns: first odd int in the numbers or None
    """

    # i think, if i first evaluated the comprehention below as list comprehention,
    # it would filter the whole collection
    # this way though, it should stop when the first valid elem is found
    first_odd = next((x for x in numbers if x % 2 == 1), None)
    return first_odd


with_odd = [2, 4, 6, 8, 1, 10]
assert find_odd(with_odd) == 1

without_odd = [42, 42, 42]
assert find_odd(without_odd) is None

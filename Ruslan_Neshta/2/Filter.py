def my_filter(function, iterable):
    """
    Return an iterator yielding those items of iterable for which function(item)
 |  is true. If function is None, return the items that are true.

    :param function: predicate
    :param iterable: iterable collection
    :return: filtered list
    :rtype: list
    """
    
    res = []
    for it in iterable:
        if function is None:
            if it:
                res.append(it)
        elif function(it):
            res.append(it)

    return res


if __name__ == "__main__":
    nums = [1,2,3,4,5]
    odds = my_filter(lambda x: x % 2, nums)
    print(odds)

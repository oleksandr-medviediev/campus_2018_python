def my_filter(pred, iterable):

    """
        :param pred: unary predicate
        :param iterable: iterable
        :returns: iterable of all items in iterable param, satisfying pred
    """
    
    return [x for x in iterable if pred(x)]


pred = lambda x : x % 2 == 0
test_range = range(10)
assert my_filter(pred, test_range) == list(filter(pred, test_range))





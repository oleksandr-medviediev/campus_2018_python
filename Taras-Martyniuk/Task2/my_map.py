def my_map(func, *iterables):

    """
        :param func: an function takin as much args as there are iterables 
        :param *iterables: any amount of iterables
    """

    return [ func(*arg_pack) for arg_pack in zip(*iterables) ]


assert my_map(lambda x, y: x, [1, 2], [11, 12]) == [1, 2]

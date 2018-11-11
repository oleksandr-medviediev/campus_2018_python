def gen_range(start, stop, step=1):
    '''
    Function is used to create a generator that works just like default Python 'range'.
    :param start: a start value of range;
    :param stop: a stop value of range;
    :param step: a step of range;
    :return: a generator that generated the range values;
    :type start: any arithmetic type;
    :type stop: any arithmetic type;
    :type step: any arithmetic type;
    :rtype: any arithmetic type.
    '''
    current_value = start
    while current_value < stop:
        yield current_value
        current_value += step

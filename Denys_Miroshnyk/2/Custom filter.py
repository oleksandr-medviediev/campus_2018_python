def custom_filter(function, values):
    """custom filter

    Arguments:
        function -- function used to filter list
        values {iterable} -- values for function to be applied

    Returns:
        list -- filtered values
    """
    result = []
    for i in values:
        if function(i):
            result.append(i)

    return result


number_list = range(-5, 5)
less_than_zero = list(custom_filter(lambda x: x < 0, number_list))
print(less_than_zero)

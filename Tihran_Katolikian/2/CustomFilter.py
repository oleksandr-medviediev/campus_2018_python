def custom_filter(function, iterable):
    """
    Method constructs an iterator from elements of an iterable for which a function returns true.
    :param function: function that tests if elements of an iterable returns true or false
    If None, the function defaults to Identity function - which returns false if any elements are false
    :param iterable: iterable which is to be filtered, could be sets, lists, tuples, or containers of any iterators
    :return: an iterator that passed the function check for each element in the iterable.
    """

    if function is None:
        function = lambda x: bool(x)

    filtered_elements = []
    for element in iterable:
        if function(element) == True:
            filtered_elements.append(element)
    
    return iter(filtered_elements)

sample = range(10)
result = custom_filter(lambda x: x % 2 == 0, sample)
print(list(result))

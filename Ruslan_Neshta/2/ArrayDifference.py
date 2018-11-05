def array_difference(arr1, arr2):
    """
    Subtracts one list from another and returns the result

    :param arr1: list of ints
    :param arr2: list of ints
    :return: list of ints
    :rtype: list
    """
    
    diff = []
    
    for el in arr1:
        if arr2.count(el) == 0:
            diff.append(el)
    
    return diff


def generate_appender(append_to):
    """
    Generates function(closure) that appends element to list.
    
    :param append_to: list
    :return: function appender
    :rtype: lambda
    """

    return lambda element: append_to.append(element)


def generate_checker(check_in):
    """
    Generates function(closure) that checks element appearence inside of a list.
    
    :param check_in: list
    :return: function checker
    :rtype: lambda
    """

    return lambda element: check_in.count(element) == 0


def check_presence_and_append_if_necessary(appender, checker, x):
    """
    Calls appender if checker returns True.
    
    :param appender: function
    :param checker: function
    :param x: argument for appender and checker
    :return: None
    :rtype: None
    """

    if checker(x):
        appender(x)


def array_diff(arr1, arr2):
    """
    Subtracts one list from another and returns the result

    :param arr1: list of ints
    :param arr2: list of ints
    :return: list of ints
    :rtype: list
    """

    # pretty weird way to do this task =)
    result = []
    list(map(lambda x: check_presence_and_append_if_necessary(generate_appender(result), generate_checker(arr2), x), arr1))
    
    return result


if __name__ == "__main__":
    result = array_diff([1, 2, 2, 2, 3, 4, 5], [2,3])
    print(result)

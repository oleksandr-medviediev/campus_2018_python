def custom_map(func, *args):
    """
    Generate a list of results of executing func on all args (each arg is passed as corresponding func parameter).

    :param func: function that has to be executed.
    :type func: function.

    :param args: flexible number of iterables that are passed to func.
    :type args: iterable.

    :return: list of func returns.
    :rtype: list.
    """
    number_of_iterations = len(args[0])

    for arg in args:

        number_of_iterations = min(number_of_iterations, len(arg))

    result = list()

    for i in range(number_of_iterations):

        params = list()

        for arg in args:

            params.append(arg[i])

        result.append(func(*params))

    return result


test_list = [1, 2, 3, 4]

print(list(custom_map(lambda a, b: a + b, test_list, test_list[::-1])))

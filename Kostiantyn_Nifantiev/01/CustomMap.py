def custom_map(function, *args):
    """
        This custom map could work with multiple input sequences
    """
    result = list()

    if not len(args):

        print('Wrong input')
        return result

    min_arg_len = len(args[0])

    for arg in args:

        if min_arg_len > len(arg): min_arg_len = len(arg)

    for index in range(min_arg_len):

        arguments_pack = list()

        for arg in args: arguments_pack.append(arg[index])

        result.append(function(*arguments_pack))

    return result


print(custom_map(lambda x, y: x * y, [1, 2, 3], [1, 2, 3, 4]))

def custom_map(my_function, *args):
    """
        This custom map could work with multiple input sequences
    """

    if not len(args):

        print('Wrong input')
        return None

    zipped_args = zip(*args)

    result = [my_function(*arg) for arg in zipped_args]

    return result


def my_test_function(x, y):

    return x * y


first_list = [1, 2, 3, 5, 5]
second_list = [1, 2, 3, 4]

print(custom_map(my_test_function, first_list, second_list))

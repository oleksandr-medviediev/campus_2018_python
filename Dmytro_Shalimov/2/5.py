print("Implement custom_filter function, which will behave like the original Python filter() function.")

def my_filter(functor, sequence):
    """
    Function check each element in given sequence by given functor and return new list with values which satisfy functor conditions

    :param functor: function which can process element from sequence
    :param sequence: sequence which element can be passed to functor
    :return: new list of sequence elements which satisfy functor conditions
    :rtype: list
    """

    filtered_list = []

    for x in sequence:

        if functor(x):

            filtered_list.append(x)

    return filtered_list


test_func = lambda x: x > 5

user_input = input("Enter numbers using space between them: ")

user_input_in_int = map(int, user_input.split())

filtered_sequence = my_filter(test_func, user_input_in_int)

for x in filtered_sequence:

    print(x)

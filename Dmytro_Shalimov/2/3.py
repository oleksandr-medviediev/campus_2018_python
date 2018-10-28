print("Implement custom_map function, which will behave like the original Python map() function.")



def my_map(functor, list_arg):
    """
    Function applies given functor to each element of list

    :param functor: any function which can take as argument element from list_arg
    :param list list_arg: list of any elements which can be passed to functor
    :return: new list of of elements from list_arg provessed by functor
    :rtype: list
    """

    new_list = []

    for x in list_arg:

        new_list.append(functor(x))

    return new_list



def double_func(arg):
    """
    Function doubles given arg

    :param arg:
    :return: double arg
    :rtype: arg type
    """
    
    return arg + arg



user_input = input("Enter sequence using spaces: ")
numbers_list = list(map(int, user_input.split()))

print(list(my_map(double_func, numbers_list)))

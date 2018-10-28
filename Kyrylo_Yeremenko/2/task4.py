"""
This script solves task 2.4 from Coding Campus 2018 Python course
(Mapping a list of functions)
"""


def map_functions(func_list, iterable, *iterables):
    """
    map() but for multiple functions
    :param func_list: List of functions to be applied to each iterable's element
    :param iterable: Mandatory iterable, functions are applied to it's elements
    :param iterables: Additional iterables, optional
    :return: List of function list's return values for each iterable's element
    """

    return_list = []

    for args in zip(iterable, *iterables):

        func_return_list = []
        for func in func_list:
            func_return_list.append(func(*args))

        return_list.append(func_return_list)

    return return_list

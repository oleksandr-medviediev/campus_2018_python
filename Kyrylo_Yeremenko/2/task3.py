"""
This script solves task 2.3 from Coding Campus 2018 Python course
(Custom map)
"""


def custom_map(func, iterable, *iterables):
    """
    Manual implementation of default map() function
    :param func: Function to be applied to iterables
    :param iterable: Mandatory iterable, function is applied to it's elements
    :param iterables: Additional iterables, optional
    :return: List of function return values for each iterable's element
    """

    return_list = []

    for args in zip(iterable, *iterables):
        return_list.append(func(*args))

    return return_list


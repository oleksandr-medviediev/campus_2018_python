"""
This script solves task 2.5 from Coding Campus 2018 Python course
(Custom filter)
"""


def custom_filter(iterable, func):
    """
    Manual implementation of default filter function
    :param iterable: Iterable which members to filter
    :param func:  Function to perform checks on each member
    :return: Filtered list containing elements that passed function check
    """
    return [x for x in iterable if func(x)]

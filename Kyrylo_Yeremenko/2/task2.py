"""
This script solves task 2.2 from Coding Campus 2018 Python course
(Array difference)
"""


def list_dif_set(array_a, array_b):
    """
    Subtracts B from A and returns difference array
    :param array_a: Array A, list subtracted from
    :param array_b: Array B, subtracted list
    :return: list containing difference elements
    """

    subtracted_set = set(array_b)
    return_list = array_a.copy()

    for element in subtracted_set:
        return_list = [value for value in return_list if value != element]

    return return_list


def list_dif_loop(array_a, array_b):
    """
    Subtracts B from A and returns difference array
    :param array_a: Array A, list subtracted from
    :param array_b: Array B, subtracted list
    :return: list containing difference elements
    """

    subtracted_set = set(array_b)
    return_list = array_a.copy()

    for element in subtracted_set:

        while element in return_list:
            return_list.remove(element)

    return return_list


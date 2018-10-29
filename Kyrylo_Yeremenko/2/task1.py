"""
This script solves task 2.1 from Coding Campus 2018 Python course
(Find the odd int)
"""


from collections import Counter


def find_odd_set(array):
    """
    :param array: list containing integers
    :return: integer value that appears odd number of times in array
    """

    unique_numbers = set(array)
    return_value = None

    for number in unique_numbers:

        times_occurred = array.count(number)
        if times_occurred % 2 != 0:

            return_value = number
            break

    return return_value


def find_odd_dict(array):
    """
    :param array: list containing integers
    :return: integer value that appears odd number of times in array
    """

    unique_numbers = dict()
    return_value = None

    for number in array:

        if number in unique_numbers:
            unique_numbers[number] += 1
        else:
            unique_numbers[number] = 1

    for key, occurrences in unique_numbers.items():

        if occurrences % 2 != 0:

            return_value = key
            break

    return return_value


def find_odd_counter(array):
    """
    :param array: list containing integers
    :return: integer value that appears odd number of times in array
    """

    unique_numbers = Counter(array)
    return_value = None

    for key, occurrences in unique_numbers.items():

        if occurrences % 2 != 0:

            return_value = key
            break

    return return_value


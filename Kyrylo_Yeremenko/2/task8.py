"""
This script solves task 2.8 from Coding Campus 2018 Python course
(Armstrong numbers)
"""


def is_armstrong_number(number):
    """
    Checks if number given is Armstrong number
    :param number: Number to be checked
    :return: True/False whether number is Armstrong number
    """

    list_digits = [int(d) for d in str(number)]
    armstrong_number = 0
    digit_count = len(list_digits)

    for digit in list_digits:
        armstrong_number += digit ** digit_count

    return armstrong_number == number

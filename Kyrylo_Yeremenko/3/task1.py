"""
This script solves task 3.1 from Coding Campus 2018 Python course
(Spell number)
"""

NUM_POWS_OF_TEN = {100: 'Hundred', 1000: 'Thousand', 1000000: 'Million'}
NUMS = \
    {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety"
    }


def say_number_less_hundred(number):
    """
    Spells number that is less than 100
    :param number: Integer between 0 and 100
    :return: String containing spelled number, if number is higher than range then empty string
    """

    return_string = ""

    if number < 20:
        return_string = NUMS[number]

    elif number < 100:
        return_string = NUMS[number - number % 10]

        if number % 10 != 0:
            return_string += ' ' + NUMS[number % 10]

    return return_string


def say_number(number):
    """
    Spells given number in string
    :param number: Integer between 0 and 999 999 999 999
    :return: String containing spelled number or None if number is not in range
    """

    if not 0 < number < 999999999999:
        return None

    return_string = say_number_less_hundred(number)

    if not return_string:

        max_power = max([key for key in NUM_POWS_OF_TEN.keys() if key <= number])
        return_string = say_number(int(number / max_power)) + ' ' + NUM_POWS_OF_TEN[max_power]

        if number % max_power != 0:
            return_string += ' ' + say_number(number % max_power)

    return return_string

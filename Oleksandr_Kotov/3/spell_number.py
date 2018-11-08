NUMBERS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "fourty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
    1000000: "million",
    1000000000: "billion",
}


def spell_hundreds(number):
    """spell the number less than one thousand

    Arguments:
        number int -- number less than one thousand

    Returns:
        str -- spelled number
    """

    spelled_number = ""

    hundreds = number // 100

    if hundreds != 0:
        spelled_number += NUMBERS[hundreds] + ' ' + NUMBERS[100]

    number %= 100

    if number > 20:

        spelled_number += ' ' + NUMBERS[number - (number % 10)]

        if number % 10 > 0:
            spelled_number += '-' + NUMBERS[number % 10]

    elif number > 0:
        spelled_number += ' ' + NUMBERS[number]

    return spelled_number


def spell_number(number):
    """spell the number less than 999 billion

    Arguments:
        number int -- number to spell

    Returns:
        str -- spelled number
    """

    spelled_number = ""

    divider = 1000000000

    while number != 0:

        hundreds = number // divider

        if hundreds != 0:

            spelled_number += ' ' + spell_hundreds(hundreds)

            if divider != 1:
                spelled_number += ' ' + NUMBERS[divider]

        number %= divider
        divider /= 1000

    return spelled_number

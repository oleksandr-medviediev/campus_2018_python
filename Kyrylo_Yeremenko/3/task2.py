"""
This script solves task 3.2 from Coding Campus 2018 Python course
(Crypto Square)
"""

import math


def encode(string):
    """
    Encodes string using Crypto Square method
    :param string: String to be encoded
    :return: Encoded string
    """

    normalized_string = (''.join(filter(str.isalnum, string))).lower()
    column_count = math.ceil(math.sqrt(len(normalized_string)))
    encoded_list = [normalized_string[c::column_count] for c in range(column_count)]

    return ' '.join(encoded_list)


def decode(string):
    """
    Decodes string using Crypto Square method
    :param string: String to be decoded
    :return: Raw decoded string
    """

    column_list = string.split(' ')
    decoded_list = \
        [
            column_list[column_index][row_index]
            for row_index in range(len(column_list[0]))
            for column_index in range(len(column_list))
            if row_index < len(column_list[column_index])
        ]

    return ''.join(decoded_list)

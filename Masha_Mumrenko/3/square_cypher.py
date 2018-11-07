import string
from math import ceil,sqrt,floor


def crypto_square(input_string):

    new_string = ''.join(el for el in input_string if el.isalnum()).lower()
    number_of_rows = int(ceil(sqrt(len(new_string))))
    
    encoded_string = ''.join(new_string[row::number_of_rows] for row in range(number_of_rows))

    return encoded_string


def decrypto_square(encoded_string):

    number_of_rows = int(floor(sqrt(len(encoded_string))))

    decoded_string = ''.join(encoded_string[row::number_of_rows] for row in range(number_of_rows))

    return decoded_string

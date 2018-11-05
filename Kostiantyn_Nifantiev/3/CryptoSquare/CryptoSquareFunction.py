from math import sqrt
from math import ceil


def encode_string(incoming_string):
    """
    Encoding string using square code
    """
    incoming_string = incoming_string.replace(' ','')
    incoming_string = incoming_string.lower()
    
    square_side = ceil(sqrt(len(incoming_string)))
    
    string_tokens = [incoming_string[index::square_side] for index in range(0, square_side)]
    encoded_string = ''.join(string_tokens)

    return encoded_string


def decode_string(encoded_string):
    """
    Decoding string using square code
    """
    square_side = ceil(sqrt(len(encoded_string)))
    encoded_string = list(encoded_string)

    shorten_rows_number = (square_side ** 2) - len(encoded_string)
    
    encoded_string.append(' ')

    for index in range(1, shorten_rows_number):

        encoded_string.insert(-square_side * index,' ')

    string_tokens = [''.join(encoded_string[index: square_side ** 2: square_side]) for index in range(0, square_side)]
    decoded_string  = ''.join(string_tokens)

    return decoded_string

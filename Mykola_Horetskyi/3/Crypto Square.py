import math

def encode(string):
    """
    Encodes string with crypto square method

Args:
    string (str) string to be encoded

Returns:
    (str) encoded string
    """

    encoded_string = "".join([character.lower() for character in string
                            if character.isalpha()])

    length = len(encoded_string)

    number_of_columns = math.ceil(math.sqrt(length))

    encoded_string = "".join([encoded_string[i::number_of_columns] for i in range(number_of_columns)])

    return encoded_string


def decode(string):
    """
    Decodes string encoded with crypto square method

Args:
    string (str) string to be decoded

Returns:
    (str) dencoded string
    """

    decoded_string = "".join([character.lower() for character in string
                            if character.isalpha()])

    length = len(decoded_string)

    number_of_rows = math.floor(math.sqrt(length))

    decoded_string = "".join([decoded_string[i::number_of_rows] for i in range(number_of_rows)])

    return decoded_string

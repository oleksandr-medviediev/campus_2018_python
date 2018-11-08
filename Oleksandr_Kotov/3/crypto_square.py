from math import sqrt, ceil


def encode(string):
    """encode string using crypto square

    Arguments:
        string str -- string to encode

    Returns:
        str -- encoded string
    """
    string = string.lower()
    characters = [char for char in string if char.isalpha()]

    step = ceil(sqrt(len(characters)))

    output = ""

    for i in range(step):
        output += ''.join(characters[i::step])

    return output


def decode(string):
    """decode string decoded using crypto square

    Arguments:
        string str -- string to decode

    Returns:
        str -- decoded string
    """

    decoded_string = ""

    width = ceil(sqrt(len(string)))
    height = ceil(len(string) / width)

    num_of_complete_columns = width - (width * height - len(string))

    for row in range(height):

        for column in range(width):

            if len(decoded_string) == len(string):
                    break

            if column <= num_of_complete_columns:

                idx = row + column * height
                decoded_string += string[idx]

            else:

                idx = row + num_of_complete_columns * height
                idx += (column - num_of_complete_columns) * (height - 1)

                decoded_string += string[idx]

    return decoded_string

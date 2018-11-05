import math


def normalize(string):
    """
    Function normalize a string
    Args:
        string(str): string to normalize
    Returns:
        bool: return normalized string
    """
    return ''.join([i for i in string.lower() if i not in [' ', ',', '.', '!', '?', '\'', '"']])


def encode(string):
    """
    Function encode string
    Args:
        string(str): string to encode
    Returns:
        bool: return encoded string
    """
    string_normalized = normalize(string)
    number_of_rows = math.ceil(math.sqrt(len(string_normalized)))
    matrix_of_char = [string_normalized[i::number_of_rows] for i in range(number_of_rows)]
    print(matrix_of_char)
    output_string = ''.join(matrix_of_char)
    print(output_string)
    return output_string


def decode(string):
    """
    Function decode string
    Args:
        string(str): string to decode
    Returns:
        bool: return decoded string
    """
    string_normalized = normalize(string)
    number_of_rows = math.ceil(math.sqrt(len(string_normalized)))
    length_string = len(string_normalized)
    matrix_of_char = [[] for i in range(number_of_rows)]

    k = 0
    for i in range(number_of_rows):
        number_of_elements = math.ceil((length_string - i)/number_of_rows)
        for j in range(number_of_elements) :
            matrix_of_char[i].append(string_normalized[k])
            k+=1

    output_string = ""
    for i in range(len(matrix_of_char[0])):
        for j in range(len(matrix_of_char)):
            if i < len(matrix_of_char[j]):
                output_string += matrix_of_char[j][i]

    return output_string





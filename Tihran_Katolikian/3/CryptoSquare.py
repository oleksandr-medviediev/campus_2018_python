from math import sqrt, ceil


def normalize_string(string):
    '''
    Normalizes string (removed punctuation symbols, whitespaces
    and downcasts message)
    :param string: any string
    :return: normalized string
    :type string: str
    :rtype: str
    '''
    normalized_string = filter(str.isalnum, string)
    normalized_string = ''.join(normalized_string)
    normalized_string = normalized_string.lower()
    return normalized_string


def encode(string):
    '''
    The classic crypto method - a square code.
    :param string: any string
    :return: encoded string
    :type string: str
    :rtype: str
    '''
    clean_string = normalize_string(string)
    number_of_columns = ceil(sqrt(len(clean_string)))
    
    encoded = ''.join(clean_string[i::number_of_columns] for i in range(number_of_columns))

    return encoded


def decode(string):
    '''
    Decodes the string that was encoded by a previous function.
    :param string: an encoded string
    :return: normalized decoded string
    :type string: str
    :rtype: str
    '''
    number_of_columns = ceil(sqrt(len(string))) - 1
    rows = [string[i::number_of_columns] for i in range(number_of_columns)]
    return ''.join(rows)

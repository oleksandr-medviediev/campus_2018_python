from itertools import groupby
from re import sub


def encode(string_to_encode):
    """
    Method encodes string using run length encoding
    :param string_to_encode: a string that will be encoded
    :return: an encoded string
    """
    groups = []
    uniques = []

    for key, grp in groupby(string_to_encode):
        groups.append(list(grp))
        uniques.append(key)

    encoded_string = ''
    for i in range(len(uniques)):
        characters_count = groups[i].count(uniques[i])
        if characters_count == 1:
            encoded_string += uniques[i]
        else:
            encoded_string += f'{characters_count}{uniques[i]}'
    
    return encoded_string


def decode(string_to_decode):
    """
    Method decodes string that was encoded using run length encoding
    :param string_to_decode: the string that will be decoded
    :return: an decoded string
    """
    decoded_string = sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), string_to_decode)


sample = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'
encoded = encode(sample)
decoded = decode(encoded)
print(f"{encoded}, {decoded}")

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
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)),
               string_to_decode)

    decoded_string = ''
    for i in range(len(string_to_decode)):
        if string_to_decode[i].isalpha():
            decoded_string += string_to_decode[i]
        else:
            offset = 0
            while string_to_decode[i:i + offset + 1].isdigit() and i + offset + 1 < len(string_to_decode):
                offset += 1
            for j in range(int(string_to_decode[i:i + offset])):
                decoded_string += string_to_decode[i + offset + 1]
            i += offset + 1
        lol = 'lol'
    
    return decoded_string


sample = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'
encoded = encode(sample)
decoded = decode(encoded)
print(f"{encoded}, {decoded}")

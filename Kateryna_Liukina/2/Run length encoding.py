from itertools import groupby


def encode(string_to_encode):
    """Encoding input message and returns encoded list"""
    return "".join([str(len(list(l)))+ch for ch,l in groupby(string_to_encode)])


def decode(encoded_string):
    """Decoding input message and returns decoded list"""
    list_of_string = []
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            list_of_string.append(encoded_string[i+1]*int(encoded_string[i]))

    return ''.join(list_of_string)




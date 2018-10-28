import math
import string


def get_string(lists):
    """
    Args:
        lists ([[str...]...]): list of lists of strs
    Return:
        str.
    """
    res = ""
    for i in lists:
        res += ''.join(i)
    return res


def encode(mstr):
    """
    Square code cipher implementation.

    Args:
        mstr (str): string to encode.
    Return:
        str - encoded message, result - list of lists of strs.
    """
    mstr = mstr.lower()
    mstr = mstr.replace(' ', '')

    root = math.ceil(math.sqrt(len(mstr)))
    while root != math.sqrt(len(mstr)):
        mstr += 'Z'

    result = []
    for i in range(1, root + 1):
        result.append([])

    for i, el in enumerate(mstr):
        result[i % root].append(el)

    return get_string(result), result


def decode(mstr, encoded_msg):
    """
    Square code decoder.

    Args:
        mstr (str): string to decode.
        encoded_msg ([[str...]...]): encoded message.
    Return:
        str - decoded.
    """
    root = math.ceil(math.sqrt(len(mstr)))
    result = []
    for i in range(1, root + 1):
        result.append([])

    for i in range(0, root):
        for j in range(0, root):
            result[i].append(encoded_msg[j][i])

    return get_string(result).replace('Z', '')


print(math.ceil(math.sqrt(55)))

encoded = encode("Ifman  wasmeanttostayonthegroundgodwouldhavegivenusroots")
print(encoded[0])
decoded = decode(encoded[0], encoded[1])
print(decoded)


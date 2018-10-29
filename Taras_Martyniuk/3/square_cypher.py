from math import sqrt, floor
from matrix import transpose
from itertools import zip_longest


get_square_side = lambda string : floor(sqrt(len(string))) + 1
split_even = lambda string, chunk_size : [string[i::chunk_size] for i in range(chunk_size)]


def encode(string):
    """
        square-encodes the string, removing whitespace, and lowercasing string
        :returns: encoded string
    """
    to_remove = {' ', '.', ','}
    string = ''.join(filter(lambda x: x not in to_remove, string))
    string = string.lower()

    side = get_square_side(string)
    cols  = split_even(string, side)

    return ''.join(map(lambda x : ''.join(x), cols))


def decode(string):
    """
        decodes square-encoded string (whitespaces and uppercasing are lost)
        :returns: original string
    """
    side = get_square_side(string) - 1
    rows  = split_even(string, side)

    return ''.join(map(lambda x : ''.join(x), rows))


orig = 'If man was meant to stay on the ground, god would have given us roots.'
encoded = 'imtgdvsfearwermayoogoanouuiontnnlvtwttddesaohghnsseoau'
decoded = 'ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots'

enc = encode(orig)
assert encode(orig) == encoded

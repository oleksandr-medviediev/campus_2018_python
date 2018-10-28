from math import sqrt, ceil


def normalize_string(string):
    """get sequence of lowercase letters"""

    string = string.lower()
    return [char for char in string if char.isalpha()]

def encode(string):
    """encode the string using crypto square"""

    characters = normalize_string(string)

    step = ceil(sqrt(len(characters)))

    output = ""

    for i in range(step):
        output += ''.join(characters[i::step])
       
    return output

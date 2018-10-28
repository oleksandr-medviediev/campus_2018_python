import math

def encode(string):
    """
    Verifies given string for correct open/close of brackets.

    :param string: string with brackets.
    :type string: str.
    :returns: result of verifying
    :rtype: str
    """

    output_string = ""

    for ch in string:

        if ch.isalpha():
            output_string += ch
    
    output_string = output_string.lower()

    columns_count = math.sqrt(len(output_string))
    columns_count = math.ceil(columns_count)

    result = [output_string[i::columns_count] for i in range(columns_count)]

    return "".join(result)


print(encode("If man was meant to stay on the ground, god would have given us roots."))

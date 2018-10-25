import math

def encode(string):


    """
    Verifies given string for correct open/close of brackets.

    @param string: string with brackets.
    @returns: result of verifying
    """

    output_string = ""

    for ch in string:

        if ch.isalpha():
            output_string += ch
    
    output_string = output_string.lower()

    columns_count = math.sqrt(len(output_string))
    columns_count = math.ceil(columns_count)

    lists = [output_string[i:i+columns_count] for i in range(0, len(output_string),columns_count)]
    
    rows_count = len(lists)

    output_string = ""

    for j in range(columns_count):

        for i in range(rows_count):

            if j < len(lists[i]):

                output_string += lists[i][j] 

    return output_string


print(encode("If man was meant to stay on the ground, god would have given us roots."))

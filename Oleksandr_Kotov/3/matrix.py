def read_matrix_rows(matrix):
    """read matrix row by row"""

    output = ""

    row = []

    number = ""

    for char in matrix:

        if char.isnumeric():
            number += char

        elif char == '\n':

            row.append(number)
            number = ""

            for element in row:
                output += element + ', '

            output = output[:-2]
            output += '\n'
            row = []

        else:

            row.append(number)
            number = ""
    else:

        row.append(number)

        for element in row:
            output += element + ', '

        output = output[:-2]
        output += '\n'


    return output

def read_matrix_columns(matrix):
    """read matrix column by column"""
    
    output = ""

    rows = []
    row = []
    number = ""

    for char in matrix:

        if char.isnumeric():
            number += char

        elif char == '\n':

            row.append(number)
            rows.append(row)

            number = ""            
            row = []

        else:

            row.append(number)
            number = ""
    else:
        row.append(number)
        rows.append(row)

    for column in zip(*rows):

        for element in column:
            output += element + ', '

        output = output[:-2]
        output += '\n'

    return output

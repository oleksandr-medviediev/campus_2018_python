def convert_to_matrix(string):

    """
    Converts string to matrix.

    @param string: matrix as string.
    @returns: matrix as list of lists of elements
    """

    matrix = string.split('\n')

    for i in range(len(matrix)):

        matrix[i] = matrix[i].split(', ')

        for j in range(len(matrix[i])):

            matrix[i][j] = int(matrix[i][j])

    return matrix


def read_matrix_rows(string):

    """
    reads rows of matrix.

    @param string: matrix as string.
    @returns: formatted string with matrix's rows.
    """

    matrix = convert_to_matrix(string)
    
    output = ""

    for i in range(len(matrix)):

        output += str(matrix[i])

        if(i != len(matrix) - 1):
            output += '\n'

    return output


def read_matrix_columns(string):

    """
    reads columns of matrix.

    @param string: matrix as string.
    @returns: formatted string with matrix's columns.
    """

    matrix = convert_to_matrix(string)
    
    output = ""

    columns = list(zip(*matrix))

    for i in range(len(columns)):

        output += str(list(columns[i]))

        if(i != len(columns) - 1):
            output += '\n'

    return output


print(read_matrix_columns("1, 2, 3\n4, 5, 6"))

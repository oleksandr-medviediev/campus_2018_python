def string_to_matrix(matrix_string):

    """ Function process matrix string view and
        return matrix as list of lists

        Args:
            matrix_string(str): string view of matrix

        Returns:
            list[list]: matrix in program view

    """

    string_rows = matrix_string.split('\n')

    matrix = []
    for i, el in enumerate(string_rows):
        row = el.split()
        matrix.append(row)

    return matrix


def read_matrix_rows(matrix_string):

    """ Function returns rows of matrix presenting in string(as string)

        Args:
            matrix_string(str): string view of matrix

        Returns:
            str: rows of matrix
            
    """

    matrix = string_to_matrix(matrix_string)

    rows_list = []

    for i, el in enumerate(matrix):
        for j, el in enumerate(matrix[0]):
            rows_list.append(matrix[i][j])
            if j != len(matrix[0]) - 1:
                rows_list.append(', ')

        if i != len(matrix) - 1:
            rows_list.append('\n')

    rows_string = ''.join(rows_list)

    return rows_string


def read_matrix_columns(matrix_string):

    """ Function returns columns of matrix presenting in string(as string)

        Args:
            matrix_string(str): string view of matrix

        Returns:
            str: columns of matrix
            
    """

    matrix = string_to_matrix(matrix_string)

    columns_list = []

    for i, el in enumerate(matrix[0]):
        for j, el in enumerate(matrix):
            columns_list.append(matrix[j][i])
            if j != len(matrix) - 1:
                columns_list.append(', ')

        if i != len(matrix[0]) - 1:
            columns_list.append('\n')

    columns_string = ''.join(columns_list)

    return columns_string

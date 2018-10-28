def matrix_str_to_list(matrix_as_str):
    """
    Convert matrix from string into a two-dimensional list of values.

    :param matrix_as_str: string that represents a matrix.
    :type matrix_as_str: str.

    :return: two-dimensional list of matrix values.
    :rtype: list.
    """
    matrix_as_lists = []
    matrix_rows = matrix_as_str.splitlines()

    for row in matrix_rows:
        matrix_as_lists.append([int(i) for i in row.split()])

    return matrix_as_lists


def read_matrix_row(matrix_as_str):
    """
    Return rows of the given matrix.

    :param matrix_as_str: matrix in a string form.
    :type matrix_as_str: str.

    :return: string representing rows of the matrix.
    :rtype: str.
    """
    matrix_as_lists = matrix_str_to_list(matrix_as_str)
    result = '\n'

    matrix_as_lists = [str(row) for row in matrix_as_lists]
    result = result.join(matrix_as_lists)

    return result


def transpose(matrix_as_lists):
    """
    Transpose a matrix.

    :param matrix_as_lists: matrix as a two-dimensional list.
    :type matrix_as_lists: list.

    :return: transposed matrix as a two-dimensional list.
    :rtype: list.
    """
    transposed = []

    for row in zip(*matrix_as_lists):
        transposed.append(list(row))

    return transposed


def read_matrix_columns(matrix_as_str):
    """
    Return columns of the given matrix.

    :param matrix_as_str: matrix in a string form.
    :type matrix_as_str: str.

    :return: string representing columns of the matrix.
    :rtype: str.
    """
    matrix_as_lists = matrix_str_to_list(matrix_as_str)
    result = '\n'

    matrix_as_lists = transpose(matrix_as_lists)
    matrix_as_lists = [str(row) for row in matrix_as_lists]
    result = result.join(matrix_as_lists)

    return result

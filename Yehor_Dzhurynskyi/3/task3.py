def read_matrix_rows(mat_string):
    """
     displays input matrix in row-major manner
        :param string mat_string: string that should be displayed
        :return: string representation of row-major matrix
        :rtype: str
    """

    rows = mat_string.splitlines()
    matrix = '\n'.join([', '.join(row.split(' ')) for row in rows])

    return matrix


def read_matrix_columns(mat_string):
    """
     displays input matrix in column-major manner
        :param string mat_string: string that should be displayed
        :return: string representation of column-major matrix
        :rtype: str
    """

    rows = mat_string.splitlines()
    size = len(rows)

    numbers = [row.split(' ')[x] for x in range(size) for row in rows]
    matrix = '\n'.join([', '.join(numbers[x * size: x * size + size]) for x in range(size)])

    return matrix

def get_matrix():
    """
    Getting matrix from user. Returns it in form capable for further proceeding 
    """
    input_matrix = input('Enter yor matrix with "," as separator between numbers and ";" between rows:\n')
    input_matrix = "\n".join(input_matrix.split(';'))
    return input_matrix


def split_matrix(matrix):
    """
    Splitting matrix into nested list
    """
    result = [row.split(',') for row in matrix.split('\n')]

    return result


def read_matrix_rows(matrix):
    """
    Making proper output string throug gluing splitted matrix back
    Makes rows
    """
    splitted_matrix = split_matrix(matrix)
    rows = [row for row in splitted_matrix]
    result = '\n'.join([','.join(row) for row in rows])

    return result


def read_matrix_columns(matrix):
    """
    Making proper output string throug gluing splitted matrix back
    Makes columns
    """
    splitted_matrix = split_matrix(matrix)
    columns = [column for column in zip(*splitted_matrix)]
    result = '\n'.join([','.join(column) for column in columns])

    return result

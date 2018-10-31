def get_matrix():
    """
    Getting matrix from user. Returns it in form capable for further proceeding 
    """
    input_matrix = input('Enter yor matrix with "," as separator between numbers and ";" between rows:\n')
    input_matrix = "\n".join(input_matrix.split(';'))
    return input_matrix


def read_matrix_rows(matrix):
    
    return matrix


def read_matrix_columns(matrix):
    """
    Making proper output string through
    splitting matrix int 2D list and further gluing it back
    """
    splitted_matrix = [row.split(',') for row in matrix.split('\n')]

    columns = [column for column in zip(*splitted_matrix)]

    return '\n'.join([','.join(column) for column in columns])

def matrix_from_string(input_string):
    """
    converts string to matrix of integers
    :param input_string: string to convert in matrix in format 1,2,3\n2,3,4
    :paramtype: str
    :return: matrix of integers
    :rtype: list
    """
    string_rows_list = input_string.split('\n')
    matrix = []
    
    for row_index in range(len(string_rows_list)):
        matrix.append(string_rows_list[row_index].split(','))
        for column_index in range(len(matrix[row_index])):
            matrix[row_index][column_index] = int(matrix[row_index][column_index])

    return matrix


def read_rows(input_string):
    """
    reads string and converts it from corresponding matrix to string by rows
    :param input_string: string to convert in matrix in format 1,2,3\n2,3,4
    :paramtype: str
    :return: corresponding matrix by rows
    :rtype: string
    """
    matrix = matrix_from_string(input_string)

    rows = '\n'.join('{},'.format(row[0:len(row)]) for row in matrix)
    
    return rows


def read_columns(input_string):
    """
    reads string and converts it from corresponding matrix to string by columns
    :param input_string: string to convert in matrix in format 1,2,3\n2,3,4
    :paramtype: str
    :return: corresponding matrix by columns
    :rtype: string
    """
    matrix = matrix_from_string(input_string)
    columns = str()
    min_row_length = min(map(len,matrix))
    
    for i in range(min_row_length):
        el = str()
        for j in range(len(matrix)):
            el = el + '{}'.format(matrix[j][i])
            if j != len(matrix) - 1:
                el = el + ','
            
        columns = columns + el
        if i != len(matrix[0]) - 1:
            columns = columns + '\n'
    
    return columns

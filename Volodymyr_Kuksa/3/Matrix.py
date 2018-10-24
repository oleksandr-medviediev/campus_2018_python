test_matrix = '9 8 7\n5 3 2\n6 6 7'


def matrix_str_to_list(matrix_as_str):

    matrix_as_lists = []
    matrix_rows = matrix_as_str.split('\n')

    for row in matrix_rows:

        matrix_as_lists.append(row.split())

        for i in range(len(matrix_as_lists[-1])):

            matrix_as_lists[-1][i] = int(matrix_as_lists[-1][i])

    return matrix_as_lists


def read_matrix_row(matrix_as_str):

    matrix_as_lists = matrix_str_to_list(matrix_as_str)
    result = ''

    for row in matrix_as_lists:

        result += str(row) + '\n'

    return result


def read_matrix_columns(matrix_as_str):

    matrix_as_lists = matrix_str_to_list(matrix_as_str)
    result = ''

    for i in range(len(matrix_as_lists[0])):

        column = []

        for j in range(len(matrix_as_lists)):

            column.append(matrix_as_lists[j][i])

        result += str(column) + '\n'

    return result


print(read_matrix_row(test_matrix))
print(read_matrix_columns(test_matrix))

def build_matrix(matrix_str):
    matrix = [row.split(' ') for row in matrix_str.splitlines()]
    return matrix


def read_matrix_rows(matrix_str):
    matrix = build_matrix(matrix_str)
    rows = '\n'.join(' '.join(column) for column in matrix)
    return rows


def read_matrix_columns(matrix_str):
    matrix = build_matrix(matrix_str)
    matrix_transposed = zip(*matrix)
    columns = '\n'.join(' '.join(column) for column in matrix_transposed)
    return columns


print(read_matrix_rows('9 8 7\n5 3 2\n6 6 7'))
print()
print(read_matrix_columns('9 8 7\n5 3 2\n6 6 7'))


def matrix_from_str(in_str):
    int_matrix = [row for row in in_str.splitlines()]
    for i in range(len(int_matrix)):
        int_matrix[i] = [int(val) for val in int_matrix[i].split()]

    return int_matrix


def str_from_matrix(in_matrix):
    out_str = str()
    for row in in_matrix:
        out_str += ''.join(map(lambda num: str(num) + ' ', row)) + '\n'
    
    return out_str


def read_matrix_rows(str_in):
    matrix_in = matrix_from_str(str_in)
    return str_from_matrix(matrix_in)


def read_matrix_columns(str_in):
    matrix_in = matrix_from_str(str_in)
    matrix_t = [*zip(*matrix_in)]
    return str_from_matrix(matrix_t)


print(read_matrix_rows('9 8 7\n5 3 2\n6 6 7'))
print(read_matrix_columns('9 8 7\n5 3 2\n6 6 7'))

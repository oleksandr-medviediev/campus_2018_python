from MatrixProcessingFunc import get_matrix, read_matrix_rows, read_matrix_columns

while True:
    
    my_matrix = get_matrix()
    print('Rows:\n' + read_matrix_rows(my_matrix))
    print('Columns:\n' + read_matrix_columns(my_matrix))
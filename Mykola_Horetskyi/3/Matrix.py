def string_to_matrix(matrix_string):
    """
    Converts string to matrix

Args:
    matrix_string (str) string to be convertet into matrix

Result:
    list of lists of (int)
"""

    matrix = [row.split(" ") for row in matrix_string.split("\n")]

    return matrix


def  read_matrix_columns(matrix_string):
    """
    Returns columns of the matrix string

Args:
    matrix_string (str) from which columns will be read

Returns:
    (str) rows of matrix with elemnts from the same columns read top-to-bottom
    and separated by spaces, each new column begins from the new line
    """

    matrix = string_to_matrix(matrix_string)

    number_of_columns = len(matrix[0])
    
    columns = []

    for i in range(number_of_columns):
        columns.append(" ".join([row[i] for row in matrix]))

    columns = "\n".join(columns)

    return columns

    

def  read_matrix_rows(matrix_string):
    """
    Returns rows of the matrix string

Args:
    matrix_string (str) from which rows will be read

Returns:
   (str) rows of matrix with elemnts from the same rows read left-to-right
    and separated by spaces, each new rows begins from the new line
    """

    matrix = string_to_matrix(matrix_string)

    matrix = [" ".join(row) for row in matrix]
    matrix = "\n".join(matrix)

    return matrix 

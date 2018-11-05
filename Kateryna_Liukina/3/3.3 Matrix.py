def read_matrix_rows(input_string):
    """
    Function return matrix
    Args:
        input_string(str): string with matrix separated by spaces and line breaks
    Returns:
        bool: return matrix
    """
    input_string = input_string.replace(' ', ', ')
    return input_string


def read_matrix_columns(input_string):
    """
    Function return transpose of a matrix
    Args:
        input_string(str): string with matrix separated by spaces and line breaks
    Returns:
        bool: return transpose of a matrix
    """
    matrix = [line.split(sep=' ')for line in input_string.split(sep='\n')]
    output_string = '\n'.join([', '.join(li) for li in zip(*matrix)])
    return output_string






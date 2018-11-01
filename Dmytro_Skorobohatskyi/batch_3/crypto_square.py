import math


def prepare_to_encode(string):

    """ Function return str which contains only letters
        from string in lower case(without punctuation
        symbols and spaces).

        Args:
            string(str): string which need to encrypt

        Returns:
            str: prepared string without punctuation symbols and spaces.
        
    """
    
    char_list = []
    char_list.extend(string)
    
    only_letters = list(filter(str.isalnum, char_list))

    result_string = ''.join(only_letters)

    lower_string = result_string.lower()
    
    return lower_string


def recognize_amount_col_and_row(amount_cells):

    """ Function return matrix dimension to place amount_cells elements

        Args:
            amount_cells(int): amount of elements need to place in matrix

        Returns:
            (int, int): pairs of numbers - amount of rows and columns
        
    """
     
    col_amount = row_amount = math.trunc(math.sqrt(amount_cells))
    
    pair = None
    if col_amount * row_amount == amount_cells:
        pair = (row_amount, col_amount)
    elif (col_amount + 1) * row_amount >= amount_cells:
        pair = (row_amount, col_amount + 1)
    else:
        pair = (row_amount + 1, col_amount + 1)

    return pair


def encode(string):

    """ Function return encrypted string by Square method.

        Args:
            string(str): string which need to encrypt

        Returns:
            str: encrypted string

    """
    
    process_string = prepare_to_encode(string)

    char_list = []
    char_list.extend(process_string)

    length = len(char_list)
    rows, columns = recognize_amount_col_and_row(length)

    cells_amount = rows * columns
    while len(char_list) != cells_amount:
        char_list.append('')

    crypto_matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(char_list[i * columns + j])

        crypto_matrix.append(row)

    result_list = []

    for i in range(columns):
        for j in range(rows):
            result_list.append(crypto_matrix[j][i])

    result_string = ''.join(result_list)

    return result_string


def decode(string):

    """ Function return decrypted string by Square method.

        Args:
            string(str): string which need to decrypt

        Returns:
            str: decrypted string

    """
    
    char_list = []
    char_list.extend(string)

    length = len(char_list)
    columns, rows = recognize_amount_col_and_row(length)

    empty_cells_amount = rows * columns - length

    crypto_matrix = []
    counter = 0
    for i in range(rows):
        row = []
        
        is_row_full = i < rows - empty_cells_amount
        elements_at_row = columns
        if not is_row_full:
            elements_at_row = columns - 1
            
        for j in range(elements_at_row):
            row.append(char_list[counter])
            counter += 1
            
        if not is_row_full:
            row.append('')
                
        crypto_matrix.append(row)

    result_list = []
       
    for i in range(columns):
        for j in range(rows):
            result_list.append(crypto_matrix[j][i])

    result_string = ''.join(result_list)

    return result_string

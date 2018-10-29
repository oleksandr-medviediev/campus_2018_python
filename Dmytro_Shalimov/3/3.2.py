print("Crypto method - a square code.")


def normalize_string(string):
    """
    Normalizes given string - removes all non-letter symbols and turnes string to lower case

    :param str string: user input
    :return: normalized string
    :rtype: str
    """

    formatted_string = ''.join(x for x in string if x.isalpha())
    normalized_string = formatted_string.lower()

    return normalized_string


def define_rows_and_columns_for_encode(string_len):
    """
    Counts rows and colums for encoding given string

    :param int string_len: length of string to encode
    :return: tuple with row as first element and column as second
    :rtype: tuple
    """

    colums = string_len
    rows = 0

    current_num = colums

    while colums - rows > 1:
        
        if current_num ** 2 > string_len:
            colums = current_num

        else:
            rows = current_num

        current_num = (colums + rows) // 2

    return (rows, colums)


def split_for_encode(string, rows_and_colums):
    """
    Splits given string to encode on parts using given rows and columns amounts

    :param str string: normalized string
    :param tuple rows_and_columns: tuple with row as first element and column as second
    :return: list of splitted string to encode
    :rtype: list
    """

    splitted_text = []
    left_len = len(string)

    columns = rows_and_colums[-1]

    next_start_position = 0
    next_end_position = 0

    while left_len != 0:

        if next_end_position + columns > len(string):

            next_end_position += left_len
            left_len = 0

        else:
            next_end_position += columns
            left_len -= columns

        text_row = string[next_start_position : next_end_position]
        splitted_text.append(text_row)

        next_start_position += columns

    return splitted_text


def encode(normalized_string):
    """
    Encodes given normalized string(only lower case letters) using square code crypto method

    :param str normalized_string: normalized string to encode
    :return: encoded string
    :rtype: str
    """

    rows_and_columns = define_rows_and_columns_for_encode(len(normalized_string))
    splitted_text = split_for_encode(normalized_string, rows_and_columns)

    output = ''
    column_counter = 0
    row_counter = 0

    while len(output) < len(normalized_string):

        if row_counter == rows_and_columns[0] - 1:
            
            if column_counter < len(splitted_text[-1]):

                output += splitted_text[row_counter][column_counter]
                row_counter = 0
                column_counter += 1

            else:

                row_counter = 0
                column_counter += 1

        else:

            output += splitted_text[row_counter][column_counter]
            row_counter += 1

    return output


def define_rows_and_columns_for_decode(string_len):
    """
    Counts rows and colums for decoding given string

    :param int string_len: length of string to encode
    :return: tuple with row as first element and column as second
    :rtype: tuple
    """

    rows = string_len
    colums = 0

    current_num = rows

    while rows - colums > 1:
        
        if current_num ** 2 > string_len:
            rows = current_num

        else:
            colums = current_num

        current_num = (colums + rows) // 2

    return (rows, colums)


def split_for_decode(string, rows_and_colums):
    """
    Splits given string to decode on parts using given rows and columns amounts

    :param str string: normalized string
    :param tuple rows_and_columns: tuple with row as first element and column as second
    :return: list of splitted string to encode
    :rtype: list
    """

    splitted_text = []
    left_len = len(string)

    columns = rows_and_colums[-1]

    next_start_position = 0
    next_end_position = 0

    while left_len != 0:

        if next_end_position + columns > len(string):

            next_end_position += left_len
            left_len = 0

        else:
            next_end_position += columns
            left_len -= columns

        text_row = string[next_start_position : next_end_position]
        splitted_text.append(text_row)

        next_start_position += columns

    return splitted_text


def decode(encoded_string):
    """
    Decodes given string using square code crypto method

    :param str encoded_string: encoded string to decode
    :return: decoded string
    :rtype: str
    """

    rows_and_columns = define_rows_and_columns_for_decode(len(normalized_string))
    splitted_text = split_for_decode(normalized_string, rows_and_columns)

    return ''.join(splitted_text)


user_input = input("Enter a string to encrypt: ")
normalized_string = normalize_string(user_input)

encoded_string = encode(normalized_string)

print("Encoded: ", encoded_string)
print("Decoded: ", decode(encoded_string))

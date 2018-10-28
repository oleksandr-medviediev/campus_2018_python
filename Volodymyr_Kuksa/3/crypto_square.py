def normalize_string(string):
    """
    Return normalized string.
    :param string: string to normalize.
    :type string: str.

    :return: normalized string.
    :rtype: str.
    """
    string = string.lower()

    normalized_characters = [c for c in string if c.isalpha() or c.isdigit()]

    return normalized_characters


def calculate_dimensions(length):
    """
    Return square dimensions for length.

    :param length: length of elements
    :type length: int.

    :return: (rows, columns).
    :rtype: (int, int).
    """
    rows = 1
    columns = length

    while not 0 <= columns - rows <= 1:

        rows += 1
        columns = int(length / rows + 0.5)

    return rows, columns


def encode(string):
    """
    Return a square encoded string.

    :param string: string to encode.
    :type string: str.

    :return: encoded string.
    :rtype: str.
    """
    normalized_characters = normalize_string(string)

    rows, columns = calculate_dimensions(len(normalized_characters))

    matrix = [[] for i in range(rows)]

    for index, char in enumerate(normalized_characters):
        matrix[index // columns].append(char)

    while len(matrix[-1]) != columns:
        matrix[-1].append('')

    result = []

    for column in zip(*matrix):
        result.extend(column)

    result = ''.join(result)
    return result


def decode(string):
    """
    Return a decoded string.

    :param string: square encoded string to decode.
    :type string: str.

    :return: decoded string.
    :rtype: str.
    """
    rows, columns = calculate_dimensions(len(string))
    rows, columns = columns, rows

    matrix = [[] for i in range(rows)]

    rows_in_last_column = len(string) % rows

    for index, char in enumerate(string):

        row_index = index // columns

        if row_index < rows_in_last_column or columns - len(matrix[row_index]) >= 2:
            matrix[index // columns].append(char)
        else:
            matrix[row_index + 1].insert(0, char)

    result = []

    for column in zip(*matrix):
        result.extend(column)

    result = ''.join(result)
    return result

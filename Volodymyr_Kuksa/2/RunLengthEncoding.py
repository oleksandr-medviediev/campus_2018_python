def encode_character(count, char):
    """
    Return run length encoded char.

    :param count: amount of consecutive repeats of char.
    :param char: character that is being encoded.

    :return: string with run length encoded char.
    :rtype: str.
    """
    result = ''

    if count > 1:

        result += str(count)

    result += char

    return result


def encode(string):
    """
    Return run length encoded string.

    :param string: the string that is being encoded.
    :type string: str.

    :return: run length encoded string.
    :rtype: str.
    """
    result = ''

    char = '\0'
    count = 0

    for c in string:

        if c == char:

            count += 1

        else:

            result += encode_character(count, char)

            count = 1
            char = c

    result += encode_character(count, char)

    return result


def decode_char(count, char):
    """
    Decode a run length encoded character into a string.

    :param count: amount of consecutive repeats of char.
    :param char: character that is being decoded.

    :return: decoded char as a string.
    :type: string.
    """
    result = ''

    if not count:

        count += 1

    for i in range(count):

        result += char

    return result


def decode(encoded_string):
    """
    Decode a run length encoded string.

    :param encoded_string: the string that is being decoded.
    :type encoded_string: str.

    :return: run length decoded string.
    :rtype: str.
    """
    result = ''
    count = 0

    for c in encoded_string:

        if c.isdigit():

            count = count*10 + int(c)

        else:

            result += decode_char(count, c)
            count = 0

    return result


test_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
encoded_string = encode(test_string)
decoded_string = decode(encoded_string)

print(test_string)
print(encoded_string)
print(decoded_string)

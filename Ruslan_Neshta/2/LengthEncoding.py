def compress(string):
    """
    Does length encoding on given string.

    :param string: string to encode
    :return: encoded list of strings
    :rtype: list
    """

    res = []
    index = 0

    while index < len(string):
        current = string[index]
        counter = 0

        while index < len(string) and string[index] == current:
            counter += 1
            index += 1

        res.append(current)
        res.append(str(counter))

    return res


def decompress(string):
    """
    Does length decoding on given string.

    :param string: string to decode
    :return: decoded list of strings
    :rtype: list
    """

    res = []
    index = 0

    while index < len(string) - 1:
        current = string[index]
        counter = 0

        if string[index + 1].isnumeric():
            counter = int(string[index + 1])
        else:
            res.append(current)

        while counter > 0:
            res.append(current)
            counter -= 1
        
        index += 2

    return res


def encode(string):
    """
    Does length encoding and decoding on given string.

    :param string: string to encode/decode
    :return: encoded/decoded string
    :rtype: string
    """

    result = ''

    if string.isalpha():
        result = result.join(compress(string))
    else:
        result = result.join(decompress(string))
    
    return result


if __name__ == "__main__":
    line = "WWWBBBBA"
    res1 = encode(line)
    print(line,' -> ', res1)

    res2 = encode(res1)
    print(res1, ' -> ', res2)

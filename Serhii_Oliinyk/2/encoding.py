def encode(string):
    """Function encode input string.

    Args:
        string: type string.

    Returns:
        Return encoding string.

    """
    array = list(string)
    result = []

    count = 1

    for i in range(1, len(array)):
        if array[i - 1] != array[i]:
            if count == 1:
                result.append(array[i - 1])
            else:
                data = str(count) + array[i - 1]
                result.append(data)
                count = 1
                if i == (len(array) - 1):
                    result.append(array[i])
        elif array[i - 1] == array[i]:
            count += 1
            if i == len(array) - 1:
                data = str(count) + array[i - 1]
                result.append(data)
        elif count == 1:
            result.append(array[i])

    if(len(result) == 0):
        result = array

    resultString = ''.join(result)

    return resultString


def decode(string):
    """Function decode input string.

    Args:
        string: type string.

    Returns:
        Return dencoding string.

    """

    array = list(string)
    returnString = ''.join(array)

    return returnString


if __name__ == '__main__':
    string = "WWWBBBBA"

    result = encode(string)
    print(result)

    result = decode(string)
    print(result)

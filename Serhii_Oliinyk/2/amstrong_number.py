def is_amstrong_number(value):
    """Function check if digit is Amstrong number.

    Args:
        value: type integer.

    Returns:
        Return true if number is Amstrong number anf false if not.

    """
    string = str(value)
    array = list(string)

    sum = 0
    for i in array:
        number = int(i) ** len(array)
        sum += number

    result = False

    if(sum == value):
        result = True
    else:
        result =  False

    return result


if __name__ == '__main__':
    result = is_amstrong_number(153)
    print(result)

def is_armstrong(num):
    """
    Checks if given number is Armstrong number.
    An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

    :param num: integer
    :return: is num an armstrong number
    :rtype: bool
    """

    line = str(num)
    sum = 0

    for char in line:
        sum += int(char)**len(line)
    
    return sum == num


if __name__ == "__main__":
    integer = 153
    print(is_armstrong(integer))

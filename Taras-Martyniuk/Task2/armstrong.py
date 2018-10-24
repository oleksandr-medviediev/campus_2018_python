def armstrong(number):

    """
        :param number: int
        :returns: sum of all digits of number to power of number of all digits
    """

    digits = [int(x) for x in str(number)]
    powers = [x ** len(digits) for x in digits]
    return sum(powers)


def is_armstrong(number):

    """
        :param number: int
        :returns: bool - is it an armstrong number?
    """

    return number == armstrong(number)


assert is_armstrong(153)
assert not is_armstrong(10)

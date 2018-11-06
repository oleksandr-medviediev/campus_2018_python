def is_armstrong(number):
    """ Function checks number to be an armstrong number

        Args:
            number(int): any non-negative number

        Returns:
            bool: True if number is armstrong number, otherwise - False.
    """
    if number < 0:
        return False

    # there is no need to check letter to be a digit,
    # because number must be a non-negative integer
    digits = [int(letter) for letter in str(number)]

    powered_sum = 0
    for digit in digits:
        powered_sum += digit ** len(digits)

    return powered_sum == number


print(is_armstrong(513))
print(is_armstrong(153))
print(is_armstrong(9))
print(is_armstrong(10))

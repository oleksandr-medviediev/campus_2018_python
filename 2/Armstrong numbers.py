def is_armstrong(number):
    """function that checks if number is an
    Armstring number

    Arguments:
        number {int} -- number to check

    Returns:
        bool -- True if is and False otherwise
    """

    digits_string = str(number)
    digits_number = len(digits_string)
    sum = 0

    for digit in digits_string:
        sum += int(digit)**digits_number

    return number == sum


print(is_armstrong(153))
print(is_armstrong(9))
print(is_armstrong(10))

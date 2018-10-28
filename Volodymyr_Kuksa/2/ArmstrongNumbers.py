def check_if_armstrong_number(number):
    """
    Check if number is an armstrong number.

    :param number: the number which is beingh checked.
    :type number: int.

    :return: True if number is armstrong number, False otherwise.
    :rtype: bool.
    """
    number_as_string = str(number)
    power = len(number_as_string)
    sum_of_digits = 0

    for c in number_as_string:

        sum_of_digits += int(c) ** power

    result = sum_of_digits == number
    return result


print(check_if_armstrong_number(10))
print(check_if_armstrong_number(9))

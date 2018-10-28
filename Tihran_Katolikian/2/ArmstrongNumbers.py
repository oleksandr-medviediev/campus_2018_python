def check_if_armstrong_number(number):
    """
    Method checks if it's argument is an Armstrong number
    :param number: an positive integer
    :return: True if number is an Armstrong number, False otherwise
    """
    sum = 0
    number_as_string = str(number)
    digits_number = len(number_as_string)
    for character in number_as_string:
        sum += int(character) ** digits_number

    return sum == number


print(check_if_armstrong_number(10))
print(check_if_armstrong_number(153))

def check_if_armstrong_number(number):
    """
    Checks if number is an Armstrong number that is is it equal
    to the sum of its own digits each raised to the power of the number of digits

Args:
    number (int) number being checked

Returns:
    True or False depending on whenether number is an Armstrong number
"""
    number_string = str(number)
    number_of_digits = len(number_string)
    
    sum_of_pow_digits = 0

    for character in number_string:
        sum_of_pow_digits += int(character) ** number_of_digits

    return sum_of_pow_digits == number

    

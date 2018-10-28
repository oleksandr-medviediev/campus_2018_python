def amount_digits(number):

    """ Function recognize amount of digit in number.

    Args:
        number(int): specified number

    Returns:
        int: amount of digits in number
        
    """
    
    counter = 0

    while number != 0:
        counter += 1
        number //= 10

    return counter


def check_if_armstrong_number(number):

    """ Function checks if passed number is armstrong.

    Args:
        number(int): specified number

    Returns:
        bool: Return True if number is armstrong,
              otherwise - return False 
        
    """
    
    sum = 0

    number_length = amount_digits(number)
    process_number = number
    
    while process_number != 0:
        last_digit = process_number % 10
        addition = last_digit ** number_length
        sum += addition

        process_number //= 10

    is_armstrong_number = sum == number

    return is_armstrong_number

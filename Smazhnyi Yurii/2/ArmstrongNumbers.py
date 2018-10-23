def check_if_armstrong_number(number):

    """
    Check if number is armstrong number

    @param number: number to check
    @returns: result of checking
    """

    number_string = str(number)
    number_of_digits = len(number_string)

    out_number = 0

    for ch in number_string:

        out_number += int(ch)**number_of_digits
    
    return out_number == number

print(check_if_armstrong_number(10))

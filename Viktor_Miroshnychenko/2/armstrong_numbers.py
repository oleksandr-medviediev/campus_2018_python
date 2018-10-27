def is_amstrong_number(number):
    """
    :param number: - number to check weather it is an amstrong number
    :type number: - str or int
    
    :return: - True if param1 is Amstrong number, False otherwise
    :rtype: - bool
    """
    if type(number) == int:
        number = str(number)

    power = len(number)
    compare_val = 0
    for digit in number:
        digit = int(digit)
        compare_val += digit**power
        
    number = int(number)
    if number == compare_val:
        return True
    else:
        return False



print(is_amstrong_number(9))
print(is_amstrong_number(10))
print(is_amstrong_number(153))
print(is_amstrong_number(1254))

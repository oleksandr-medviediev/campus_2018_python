def check_if_armstrong_number(number):
    """
        This function checks armastrongness by direct calculations
        Note: inpt coud be either string or integer, 
        but string should be numeric
    """
    token_string = str(number)
    if not token_string.isnumeric(): return 'Wrong input!'

    accumulator = int()
    pow = len(token_string)

    for char in token_string: accumulator += int(char) ** pow

    if token_string == str(accumulator): return True

    else: return False

num_to_check = input('Enter integer for check for Armstrongness: ')
print(check_if_armstrong_number(num_to_check))

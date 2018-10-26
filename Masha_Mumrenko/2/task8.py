def check_if_armstrong(integer_to_check):
    digits_string = str(integer_to_check)
    digits_number = len(digits_string)
    armstrong_sum = 0

    for digit in digits_string:
        armstrong_sum += int(digit)**digits_number

    return integer_to_check == armstrong_sum

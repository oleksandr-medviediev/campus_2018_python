def check_if_armstrong_number(number):
    number = str(number)

    armstrong_number = 0

    for digit in number:
        armstrong_number += int(digit)**len(number)

    return armstrong_number == int(number)
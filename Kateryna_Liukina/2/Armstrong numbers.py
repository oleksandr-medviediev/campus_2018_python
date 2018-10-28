def input_number():
    """Requests input until number is entered, returns number"""
    while True:
        number = input('Enter number:\n')
        if number.isdigit():
            return number
        elif number.lower() == 'quit':
            return 0
        else:
            print ("Invalid input, not number!")


def check_if_armstrong_number(number_str):
    """Checks if given number is Armstrong number"""
    digits = [int(ch)**(len(number_str)) for ch in number_str]
    result = 0
    for i in digits:
        result += i
    return int(number_str) == result


print(check_if_armstrong_number(input_number()))


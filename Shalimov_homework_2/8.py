print("An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.")



def check_if_armstrong_number(num):

    if not num.isnumeric():

        return False

    pow_number = len(num)
    num_in_int = int(num)

    splitted_number = []

    for x in num:

        splitted_number.append(int(x))

    pow_func = lambda x: x ** pow_number

    powered_numbers = map(pow_func, splitted_number)
    powered_sum = sum(powered_numbers)

    if num_in_int == powered_sum:

        return True

    else:

        return False


user_input = input("Enter number: ")

print(check_if_armstrong_number(user_input))

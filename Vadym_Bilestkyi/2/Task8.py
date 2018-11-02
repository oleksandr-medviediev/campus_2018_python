def is_armstrong(number):
    digits = [int(letter) for letter in str(number)]

    powered_sum = 0
    for digit in digits:
        powered_sum += digit ** len(digits)

    return powered_sum == number


print(is_armstrong(513))
print(is_armstrong(153))
print(is_armstrong(9))
print(is_armstrong(10))

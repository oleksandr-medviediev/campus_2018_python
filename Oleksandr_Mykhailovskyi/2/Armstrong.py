
def is_armstrong_number(number):
    """
    Detects whether number is narcissistic or not. More info - https://en.wikipedia.org/wiki/Narcissistic_number .

    Args:
        number (int): given number.

    Returns:
        True if number is narcissistic. False otherwise.
    """
    digits_amount = len(str(number))
    numbers_list = [int(num) for num in str(number)]
    res = 0
    for i in numbers_list:
        res += i ** digits_amount
    return res == number


number = int(input())
print(is_armstrong_number(number))

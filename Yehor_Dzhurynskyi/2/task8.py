def check_if_armstrong_number(num):
    """
    checks if number is an armstrong number
    @ref: https://en.wikipedia.org/wiki/Narcissistic_number
        :param num: interger number that should be checked
        :return: True if `num` is armstrong number else False
    """

    sum_of_digits = sum([int(n) ** len(str(num)) for n in str(num)], 0)
    is_armstrong_num = sum_of_digits == num

    return is_armstrong_num

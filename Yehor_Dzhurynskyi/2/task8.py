def check_if_armstrong_number(num):

    sum_of_digits = sum([int(n) ** len(str(num)) for n in str(num)], 0)
    is_armstrong_num = sum_of_digits == num

    return is_armstrong_num

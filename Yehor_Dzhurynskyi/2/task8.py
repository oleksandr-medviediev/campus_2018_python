def check_if_armstrong_number(num):
    return num == sum([int(n) ** len(str(num)) for n in str(num)], 0)

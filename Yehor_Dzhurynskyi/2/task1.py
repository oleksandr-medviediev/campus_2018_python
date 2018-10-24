def find_odd1(number_list):
    for num in number_list:
        if number_list.count(num) % 2 != 0:
            return num
    return None


def find_odd2(number_list):
    return [num for num in number_list if number_list.count(num) % 2 != 0][0]

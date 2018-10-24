def find_odd1(number_list):

    for num in number_list:
        if number_list.count(num) % 2 != 0:
            return num

    return None


def find_odd2(number_list):

    odd = [num for num in number_list if number_list.count(num) % 2 != 0][0]

    return odd


def find_odd3(number_list):

    odd = list(filter(lambda num: number_list.count(num) % 2 != 0, number_list))[0]

    return odd

def find_odd1(number_list):
    """
    finds the first number that occurs in the collection an odd number of times
        :param number_list: `iterable` collection of numbers
        :return number that occurs in the collection an odd number of times
    """

    for num in number_list:
        if number_list.count(num) % 2 != 0:
            return num

    return None


def find_odd2(number_list):
    """
    finds the first number that occurs in the collection an odd number of times
        :param number_list: `iterable` collection of numbers
        :return number that occurs in the collection an odd number of times
    """

    odd = [num for num in number_list if number_list.count(num) % 2 != 0][0]

    return odd


def find_odd3(number_list):
    """
    finds the first number that occurs in the collection an odd number of times
        :param number_list: `iterable` collection of numbers
        :return number that occurs in the collection an odd number of times
    """

    odd = list(filter(lambda num: number_list.count(num) % 2 != 0, number_list))[0]

    return odd

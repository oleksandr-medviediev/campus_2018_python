def find_odd_in_one_way(list_of_numbers):

    """
    def find_odd_in_one_way(list_of_numbers)
    Finds an integer that present in the list_of_number odd number of times
    This function works as efficient as possible for this task

    :param list_of_numbers: a list of integers in which must be at least one integer
    which has odd number of copies there
    :return: an integer that present in the list_of_number odd number of times
    """

    for number in list_of_numbers:
        if list_of_numbers.count(number) % 2 == 1:
            return number


def find_odd_in_second_way(list_of_numbers):

    """
    def find_odd_in_second_way(list_of_numbers)
    Finds an integer that present in the list_of_number odd number of times.
    This function is likely to work less efficient than find_odd_in_one_way function

    :param list_of_numbers: a list of integers in which must be at least one integer
    which has odd number of copies there
    :return: an integer that present in the list_of_number odd number of times
    """

    for i in list_of_numbers:
        count = 0
        for j in list_of_numbers:
            if i == j:
                count += 1
        if count % 2 == 1:
            return i


print(find_odd_in_second_way([1, 2, 3, 1, 3, 2, 1]))

print("Implement a difference function, which subtracts one list from another and returns the result.")



def list_difference_1(list_1, list_2):
     """
    Function sums given lists and create new one without duplicates.
    Argumetns must be of the same type.

    :param list list_1: a list 
    :param list list_2: a list with elements of the same typr as list_1
    :return: list of unique elements from sum of list_1 and list_2
    :rtype: list 
    """

    lists_sum = list_1 + list_2

    new_list = []

    for x in lists_sum:

        if lists_sum.count(x) == 1:

            new_list.append(x)

    return new_list



def list_difference_2(list_1, list_2):
    """
    Function converts given lists to sets and subtracts set2 from set1.
    Argumetns must be of the same type.

    :param list list_1: a list 
    :param list list_2: a list with elements of the same typr as list_1
    :return: list with subtraction result
    :rtype: list 
    """
    return list(set(list_1) - set(list_2))



user_input = input("Enter first sequence using spaces: ")
first_list = list(map(int, user_input.split()))

user_input = input("Enter second sequence using spaces: ")
second_list = list(map(int, user_input.split()))

print(list_difference_2(first_list, second_list))

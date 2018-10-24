print("Implement a difference function, which subtracts one list from another and returns the result.")



def list_difference_1(list_1, list_2):

    lists_sum = list_1 + list_2

    new_list = []

    for x in lists_sum:

        if lists_sum.count(x) == 1:

            new_list.append(x)

    return new_list



def list_difference_2(list_1, list_2):

    return list(set(list_1) - set(list_2))



user_input = input("Enter first sequence using spaces: ")
first_list = list(map(int, user_input.split()))

user_input = input("Enter second sequence using spaces: ")
second_list = list(map(int, user_input.split()))

print(list_difference_2(first_list, second_list))

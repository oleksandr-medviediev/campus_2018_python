def find_odd_in_one_way(list_of_numbers):

    for number in list_of_numbers:
        if list_of_numbers.count(number) % 2 == 1:
            return number


def find_odd_in_second_way(list_of_numbers):
    for i in list_of_numbers:
        count = 0
        for j in list_of_numbers:
            if i == j:
                count += 1
        if count % 2 == 1:
            return i



print(find_odd_in_second_way([1, 2, 3, 1, 3, 2, 1]))
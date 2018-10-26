def find_odd(integers_list):
    """Function to find the integer, that appears odd number of times.
    This number can be only one in the list.
    :parameter integers_list: list of integers
    :type integer_list: list of integers
    :return:integer from list that apperas odd number of times"""
    answer = 0
    for i in range(len(integers_list)):
        if integers_list.count(integers_list[i])%2 != 0 :
            answer = integers_list[i]

    return answer

def find_odd_v2(integers_list):
    for i in integers_list:
        count = 0
        for j in integers_list:
            if i == j:
                count += 1
        if count % 2 != 0:
            answer = i
            break

    return answer

def find_odd_v3(integers_list):
    answer = 0
    for integer in integers_list:
        answer ^= integer

    return answer

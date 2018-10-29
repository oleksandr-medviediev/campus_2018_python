def find_odd(array_of_integers):
    """This function finds the int that appears an odd number of times. 
    There will always be only one integer that appears an odd number of times.

    Arguments:
            array_of_integers {list} -- list of integers

    Returns:
            integer -- integer from list that apperas odd number of times
    """
    Set = set(array_of_integers)
    for val in Set:
        if array_of_integers.count(val) % 2:
            return val


def find_odd_2(array_of_integers):
    """This function finds the int that appears an odd number of times. 
    There will always be only one integer that appears an odd number of times.

    Arguments:
            array_of_integers {list} -- list of integers

    Returns:
            interer -- integer from list that apperas odd number of times
    """
    for i in array_of_integers:
        count = 0
        for j in array_of_integers:
            if i == j:
                count += 1
        if count % 2 != 0:
            answer = i
            break

    return answer

def find_odd_3(array_of_integers):
    """This function finds the int that appears an odd number of times. 
    There will always be only one integer that appears an odd number of times.

    Arguments:
            array_of_integers {list} -- list of integers

    Returns:
            interer -- integer from list that apperas odd number of times
    """
    for i in array_of_integers:
        if array_of_integers.count(i) % 2 != 0:
            return i

print(find_odd([1, 2, 3, 1, 3, 2, 1]))

print(find_odd_2([1, 2, 3, 1, 3, 2, 1]))

print(find_odd_3([1, 2, 3, 1, 3, 2, 1]))

input()

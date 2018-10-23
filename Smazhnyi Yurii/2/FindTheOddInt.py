def find_odd_int(sequnce):

    """returns first number that enrty's odd count of times"""

    for i in sequnce:

        int_count = sequnce.count(i)
        if int_count % 2:

            return i


test_list = [1,2,3,4,5,6,2,3,3,1]

print(find_odd_int(test_list))
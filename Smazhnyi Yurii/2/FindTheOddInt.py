def find_odd_int(sequence):

    """
    Finds and returns first number that entries odd count of times

    @param sequence: sequnce to search in
    @returns: first number that entries odd count of times
    """

    for i in sequence:

        int_count = sequence.count(i)
        if int_count % 2:

            return i


test_list = [1, 2, 3, 4, 5, 6, 2, 3, 3, 1]

print(find_odd_int(test_list))

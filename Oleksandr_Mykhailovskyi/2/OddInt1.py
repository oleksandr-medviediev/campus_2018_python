import string


def get_number(sequence):
    """
    Detects first instance of number which occurs odd number of times in list.

    Args:
        sequence (iterable): container of numbers.

    Returns:
        If found return number. Otherwise None.
    """
    for i in sequence:
        if i.isnumeric() and sequence.count(i) % 2 != 0:
            return i
    return None


input_string = input("Enter number sequence\n")
print(get_number(input_string))

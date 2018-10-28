

def get_number(number_sequence):
    """
    Detects first instance of number which occurs odd number of times in list.

    Args:
        number_sequence (iterable): container of numbers.

    Returns:
        If found return number. Otherwise None.
    """
    mset = set(number_sequence)
    for entry in mset:
        if number_sequence.count(entry) % 2 != 0:
            return entry
    return None

sequenceA = input()
print(get_number(sequenceA))

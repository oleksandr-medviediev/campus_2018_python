def array_diff(sequenceA, sequenceB):
    """
    Set difference.

    Args:
        sequenceA (iterable): iterable object.
        sequenceB (iterable): iterable object.

    Returns:
        List with elements from A / B.
    """
    return [i for i in sequenceA if sequenceB.count(i) == 0]


sequenceA = input()
number_sequenceA = sequenceA.split()
sequenceB = input()
number_sequenceB = sequenceB.split()
number_sequenceA = array_diff(number_sequenceA, number_sequenceB)
print(number_sequenceA)

def get_number(number_seqeunce):
    """
    Detects first instance of number which occurs odd number of times in list.

    Args:
        number_seqeunce (list): number sequence.

    Returns:
        Int.
    """
    number_sequence.append(None)
    return [i for i in number_seqeunce if number_seqeunce.count(i) % 2 != 0][0]

input_sequence = input("enter number sequence\n")
number_sequence = input_sequence.split()
print(get_number(number_sequence))

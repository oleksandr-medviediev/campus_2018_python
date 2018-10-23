
def get_number(number_sequence):
    mset = set(number_sequence)
    for entry in mset:
        if number_sequence.count(entry) % 2 != 0:
            return entry
    return None

sequenceA = input()
print(get_number(sequenceA))
import string

def get_number(sequence):
    for i in sequence:
        if i.isnumeric() and sequence.count(i) % 2 != 0:
            return i
    return None


input_string = input("Enter number sequence\n")
print(get_number(input_string))
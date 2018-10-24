from collections import Counter

print("Given an array, find the int that appears an odd number of times.")
print("There will always be only one integer that appears an odd number of times.")
print("Do it in 3 different ways (create a separate function for each solution).")

def find_odd_number_1(sequence):

    number = 0

    for x in sequence:

        count = sequence.count(x)
        if count % 2 != 0:

            number = x
            break
    
    return number


def find_odd_number_2(sequence):

    temp = Counter(sequence)

    return list(temp.keys())[0]


user_input = input("Enter sequence using spaces: ")

numbers = list(map(int, user_input.split()))

print(find_odd_number_2(numbers))

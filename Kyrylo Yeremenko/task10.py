"""
This script solves task 10 from Coding Campus 2018 Python course
(Rotational Cipher)
"""

import string

keyString = input("Input key: ")
userString = input("Input string: ")

if keyString.isdigit():

    # Store indices as cipher doesn't work with capital letters
    capitalIndices = [i for i, char in enumerate(userString) if char.isupper()]

    lowerUserString = userString.lower()

    shift = int(keyString)

    alphabet = string.ascii_lowercase
    salphabet = alphabet[shift:] + alphabet[:shift]

    shiftedString = lowerUserString.translate(lowerUserString.maketrans(alphabet, salphabet))

    # Capitalize letters
    for i in capitalIndices:
        shiftedString = shiftedString[:i] + shiftedString[i].upper() + shiftedString[i + 1:]

    print(shiftedString)
else:
    print("Incorrect key!")

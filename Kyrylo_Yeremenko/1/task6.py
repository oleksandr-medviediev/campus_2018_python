"""
This script solves task 6 from Coding Campus 2018 Python course
(Validate PIN code)
"""

userString = input("Input string: ")
isPin = False

if len(userString) == 4 or len(userString) == 6:
    if userString.isdigit():
        isPin = True

print(isPin)

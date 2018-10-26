"""
This script solves task 8 from Coding Campus 2018 Python course
(Validation of 24 hours time)
"""

userString = input("Input string: ")

isValid = True
split = userString.split(':')

if len(split) != 2:
    isValid = False
elif not (split[0].isdigit() and split[1].isdigit()):
    isValid = False
elif int(split[0]) > 24 and int(split[1]) > 59:
    isValid = False

print(isValid)

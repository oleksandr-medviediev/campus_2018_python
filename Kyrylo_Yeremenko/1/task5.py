"""
This script solves task 5 from Coding Campus 2018 Python course
(Get the Middle Character)
"""

userString = input("Input string: ")

floatIndex = len(userString) / 2.0
indexes = [int(floatIndex)]

if floatIndex.is_integer():
    indexes.append(int(floatIndex) - 1)

outputString = ""
for index in reversed(indexes):
    outputString += userString[index]

print(outputString)

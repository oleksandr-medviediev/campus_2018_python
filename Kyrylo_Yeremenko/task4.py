"""
This script solves task 4 from Coding Campus 2018 Python course
(Isogram)
"""

userString = input("Input string: ")
userString = userString.lower()

characters = set(userString)
ignoredCharacters = [' ', '-']
isIsogramFlag = True

for char in characters:
    if char in ignoredCharacters:
        continue
    if userString.count(char) > 1:
        isIsogramFlag = False
        break

print(isIsogramFlag)

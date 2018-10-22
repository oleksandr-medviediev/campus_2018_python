"""
This script solves task 1 from Coding Campus 2018 Python course
(Exes And Ohs)
"""

userString = input("Input string: ")
exes = ohs = pos = 0

exes = userString.count('X') + userString.count('x')
ohs = userString.count('o') + userString.count('O')

if exes == ohs or not (exes and ohs):
    print('True')
else:
    print('False')

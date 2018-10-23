"""
This script solves task 7 from Coding Campus 2018 Python course
(Bob)
"""

userString = input("Input string: ")

if userString.isupper():
    if userString.endswith('?'):
        print("Calm down, I know what I'm doing!")
    else:
        print("Whoa, chill out!")

elif not len(userString):
    print("Fine. Be that way!")

elif userString.endswith('?'):
    print("Sure.")

else:
    print("Whatever.")


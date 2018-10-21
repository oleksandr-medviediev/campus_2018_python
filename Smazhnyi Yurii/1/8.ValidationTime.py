import re

string = input("input your string: ")

if re.match('([01]?[0-9]|2[0-3]):[0-5][0-9]',string):
    print(True)
else:
    print(False)

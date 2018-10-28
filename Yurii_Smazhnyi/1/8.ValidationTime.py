import re

string = input("input your string: ")

valid_time = re.compile('([01]?[0-9]|2[0-3]):[0-5][0-9]')

if valid_time.match(string):
    print(True)
else:
    print(False)

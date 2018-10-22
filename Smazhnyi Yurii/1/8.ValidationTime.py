import re

string = input("input your string: ")

validTime = re.compile('([01]?[0-9]|2[0-3]):[0-5][0-9]')

if validTime.match(string):
    print(True)
else:
    print(False)

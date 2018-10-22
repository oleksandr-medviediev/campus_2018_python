import re

string = input("input your string: ")

if re.match('[0-9]{4,6}', string):
    print (True)
else:
    print (False)

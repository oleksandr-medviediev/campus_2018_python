import re

str = input("input your string: ")

if re.match('[0-9]{4,6}', str):
    print (True)
else:
    print (False)

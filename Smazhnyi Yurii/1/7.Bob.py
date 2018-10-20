import re

str = input("input your string: ")

if len(str) == 0:
    print("Fine. Be that way!")
elif str[-1] == '?':
    if re.match('[a-z]+',str):
        print("Sure.")
    else:
        print("Whoa, chill out!")
elif str[-1] == '!':
    print("Calm down, I know what I'm doing!")
else:
    print("Whatever.")
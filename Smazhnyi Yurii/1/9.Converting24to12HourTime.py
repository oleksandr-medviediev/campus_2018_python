import re

string = input("input your string: ")

valid_time = re.compile('([01]?[0-9]|2[0-3]):[0-5][0-9]')

if valid_time.match(string):

    str_list = string.split(':')

    hour = int(str_list[0])

    if(hour > 12):
        str_list[0] = str(hour % 12)
        str_list[1] += " pm"
    else:
        str_list[1] += " am"

    print(str_list[0] + ':' + str_list[1])
else:
    print("not valid time")

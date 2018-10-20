import re

s = input("input your string: ")

if re.match('([01]?[0-9]|2[0-3]):[0-5][0-9]',s):

    strList = s.split(':')

    hour = int(strList[0])

    if(hour > 12):
        strList[0] = str(hour % 12)
        strList[1] += " pm"
    else:
        strList[1] += " am"

    print(strList[0] + ':' + strList[1])
else:
    print("not valid time")
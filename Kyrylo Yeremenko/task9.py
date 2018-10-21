"""
This script solves task 9 from Coding Campus 2018 Python course
(Converting 24-hour time to 12-hour time)
"""


def validate_24h(string):

    is_valid = True
    split = string.split(':')

    if len(split) != 2:
        is_valid = False
    elif not (split[0].isdigit() and split[1].isdigit()):
        is_valid = False
    elif int(split[0]) > 24 and int(split[1]) > 59:
        is_valid = False

    return is_valid, split


userString = input("Input string: ")
isStringValid, stringSplit = validate_24h(userString)

if isStringValid:

    hours = int(stringSplit[0])
    isAM = True

    if hours > 12:
        hours -= 12
        isAM = False

        hoursString = str(hours)
        if hours < 10:
            hoursString = '0' + hoursString

        stringSplit[0] = hoursString

    outputString = stringSplit[0] + ':' + stringSplit[1]

    if isAM:
        outputString += " AM"
    else:
        outputString += " PM"

    print(outputString)

else:
    print("Invalid time")

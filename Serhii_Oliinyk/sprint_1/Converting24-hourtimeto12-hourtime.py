#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      soliinyk
#
# Created:     23/10/2018
# Copyright:   (c) soliinyk 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main(string):
    if(string.find(":") == -1):
        return "not a valid time"

    array = string.split(":")

    if((not array[0].isdigit()) or (not array[1].isdigit())):
        return "not a valid time"

    if((int(array[0]) < 0) or (int(array[0]) > 23)):
        return "not a valid time"

    if((int(array[1]) < 0) or (int(array[1]) > 59)):
        return "not a valid time"

    result = ""

    if(int(array[0]) >= 12):
        result += "0" + str((int(array[0]) -  12)) + ":" + array[1] + " pm"
    else:
        result += array[0] + ":" + array[1] + " am"

    return result

if __name__ == '__main__':
    result = main("19:20")
    print(result)

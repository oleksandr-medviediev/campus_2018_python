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
        return False

    array = string.split(":")

    if((not array[0].isdigit()) or (not array[1].isdigit())):
        return False

    if((int(array[0]) < 0) or (int(array[0]) > 23)):
        return False

    if((int(array[1]) < 0) or (int(array[1]) > 59)):
        return False

    return True

if __name__ == '__main__':
    result = main("10:61")
    print(result)

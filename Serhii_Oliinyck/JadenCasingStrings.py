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
    result = ""

    array = string.split(" ")
    for i in array:
        result += i.capitalize() + " ";

    print(result)

if __name__ == '__main__':
    main("hello world")

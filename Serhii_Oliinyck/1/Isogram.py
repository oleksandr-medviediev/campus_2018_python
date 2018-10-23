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
    if(string == ""):
        return False

    for i in string:
        if(string.count(i) > 1):
            return False

    return True

if __name__ == '__main__':
    result = main("abolishment")
    print(result)

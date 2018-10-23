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
    if((len(string) != 4) and (len(string) != 6)):
        return False

    return string.isdigit()

if __name__ == '__main__':
    result = main("1234")
    print(result)

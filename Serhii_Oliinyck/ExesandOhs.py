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
    xCount = oCount = 0

    for i in string:
        if((i == 'x') or (i == 'X')):
            xCount = xCount + 1
        elif((i == 'o') or (i == 'O')):
            oCount = oCount + 1

    print(xCount == oCount)

if __name__ == '__main__':
    main("ooxx")

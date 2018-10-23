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
    if(len(string) % 2 == 0):
        index = int(len(string) / 2)
        print(string[index : index + 2 : 1])
    else:
        print(string[int(len(string) / 2)])

if __name__ == '__main__':
    main("tesst")

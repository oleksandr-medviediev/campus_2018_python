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
        return "Fine. Be that way!"
    elif(string.isupper() and (string[len(string) - 1] == "?")):
        return "Calm down, I know what I'm doing!"
    elif(string.isupper()):
        return "Whoa, chill out!"
    elif(string[len(string) - 1] == "?"):
        return "Sure."
    else:
        return "Whatever."

if __name__ == '__main__':
    result = main("How are you")
    print(result)

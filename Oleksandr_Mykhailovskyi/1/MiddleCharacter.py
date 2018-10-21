
def MiddleCharacter(inputString):
    if type(inputString) != str:
        raise TypeError("Input is not string")
    else:
        length = len(inputString)
        return inputString[(length + 1) >> 1] if length % 2 != 0 else inputString[length >> 1 : (length >> 1) + 2]

mstr = input("Enter string:\n")
print("Result: " + MiddleCharacter(mstr))
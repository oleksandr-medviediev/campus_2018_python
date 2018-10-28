import string

pin = "0000"

# Checks if PIN 6/4 digits
def ValidatePINStructure(inputPIN):
    if type(inputPIN) != str:
        raise TypeError("Validate PIN accepts string")
    else :
        if len(inputPIN) != 6 and len(inputPIN) != 4:
            print("PIN has to be 4 or 6 digits long")
            return False
        for character in inputPIN :
            if not character in string.digits:
                print("Detected non-digit character, try again")
                return False
        return True
    return False
    


def InitPIN():
    success = False
    while not success:
        inputString = input("Enter init PIN: ")
        success = ValidatePINStructure(inputString)
    print("Success")
    pin = inputString

InitPIN()
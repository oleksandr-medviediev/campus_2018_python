import string

# Slightly modified - all punctuation symbols can be repeated, not only hyphen and space
def IsIsogram(inputString):
    if(type(inputString) != str):
        raise TypeError("IsIsogram takes string")
    else:
        data = inputString.lower()
        for character in data:
            if (not character in string.punctuation) and data.count(character) > 1:
                return False
        return True


mstr = input("Enter string:\n")
print(IsIsogram(mstr))
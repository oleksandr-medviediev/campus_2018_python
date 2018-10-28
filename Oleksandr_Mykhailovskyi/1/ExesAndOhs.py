def XOCount(mstr = "oxox"):
    localStr = mstr.casefold()
    if localStr.count('x') == 0 and localStr.count('o') == 0:
        return True
    elif localStr.count('x') == localStr.count('o'):
        return True
    return False

mstr = input("Enter string:\n")
print(XOCount(mstr))

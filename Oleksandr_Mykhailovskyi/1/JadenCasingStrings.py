import re

def JadenCasing(mstr = "string"):
    mlist = re.split('(\W)', mstr)
    mlist = [i.capitalize() for i in mlist]
    res = str().join(mlist)
    return res

mstr = input("Enter string:\n")
mstrcpy = mstr.title()
print("Title method result: " + mstrcpy)
print("Re result: " + JadenCasing(mstr))
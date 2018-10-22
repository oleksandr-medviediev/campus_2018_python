def ReverseString(mstr = "somestring"):
    res = str().join([i for i in reversed(mstr)])
    return res

mstr = input("Enter string to reverse:\n")
revString = mstr[::-1]
print("Reverse slice result: " + revString)
print("ReverseString result: " + ReverseString(mstr))
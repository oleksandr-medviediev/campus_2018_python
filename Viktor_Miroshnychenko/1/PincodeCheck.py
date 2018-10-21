import sys
pincode = input("Enter a pincode \n")

digits = "1234567890"

if len(pincode) != 4 and len(pincode) != 6:
    print(False)
    sys.exit()

valid = True

for char in pincode:
    if digits.find(char) == -1:
        valid = False
        break;

print(valid)

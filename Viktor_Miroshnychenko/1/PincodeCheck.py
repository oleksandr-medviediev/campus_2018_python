pincode = input("Enter a pincode \n")

valid = True

if len(pincode) != 4 and len(pincode) != 6:
    valid = False

for char in pincode:
    if char.isdigit() == False:
        valid = False
        break;

print(valid)

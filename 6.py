print("ATM machines allow 4 or 6 digit PIN codes")
print("and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.")

user_input = input("Enter PIN: ")
user_input_len = len(user_input)
is_pin_valid = False

if user_input_len == 4 or user_input_len == 6:
    for x in user_input:
        if x.isnumeric() == False:
            is_pin_valid = False
            break
            
        else:
            is_pin_valid = True

print(is_pin_valid)
